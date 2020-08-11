Drop table if exists dim_data_simple;
create table if not exists dim_data_simple as SELECT
    datum AS DATE,
    to_char(datum, 'yyyymmdd') AS Formatted_CHAR_DATE,
    to_number(to_char(datum, 'yyyymmdd'),'99999999') AS Formatted_INTEGER_DATE,
    EXTRACT(YEAR FROM datum) AS YEAR,
    EXTRACT(MONTH FROM datum) AS MONTH,
    -- Localized month name
    to_char(datum, 'TMMonth') AS MonthName,
    EXTRACT(DAY FROM datum) AS DAY,
    EXTRACT(doy FROM datum) AS DayOfYear,
    -- Localized weekday
    to_char(datum, 'TMDay') AS WeekdayName,
    -- ISO calendar week
    EXTRACT(week FROM datum) AS CalendarWeek,
    to_char(datum, 'dd. mm. yyyy') AS FormattedDate,
    'Q' || to_char(datum, 'Q') AS Quartal,
    to_char(datum, 'yyyy/"Q"Q') AS YearQuartal,
    to_char(datum, 'yyyy/mm') AS YearMonth,
    -- ISO calendar year and week
    to_char(datum, 'iyyy/IW') AS YearCalendarWeek,
    -- Weekend
    CASE WHEN EXTRACT(isodow FROM datum) IN (6, 7) THEN 'Weekend' ELSE 'Weekday' END AS Weekend
FROM (
    -- There are 3 leap years in this range, so calculate 365 * 10 + 3 records
    SELECT '2015-01-01'::DATE + SEQUENCE.DAY AS datum
    FROM generate_series(0,3652) AS SEQUENCE(DAY)
    GROUP BY SEQUENCE.DAY
 	) DQ
ORDER BY 1
