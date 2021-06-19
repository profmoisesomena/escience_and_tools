#Criando uma lista com multiplos de 5 da lista original
import io
lst =  [1,2,3,4,5]
nwlist = []
for i in lst:
    nwlist.append(i*5)
print(lst)
print(nwlist)
    
# Usando list comprehensions para realizar mesma atividade em uma unica linha


res = [i*5 for i in lst]
print(res)

#outros exemplos com condicao na list comprehensions

res_mod2 = [i*5   for i in lst if i%2==0  ]
print(res_mod2)

res_mod2_else = [i*5 if i%2==0 else ''  for i in lst ]
print(res_mod2_else)

# usando list comprehensions para excluir palavras de um texto com base em uma lista de palavras

stop_words = ['teste','noteste']
list_words = ['teste','noteste2','teste1','noteste','teste2','noteste','teste','noteste2','teste','noteste3','teste','noteste']

ok_list = [word for word in list_words if word not in stop_words]
print(ok_list)

# Exercicio 1
# Crie uma list compreensions a partir de uma lista de um a 1000 que seja multiplicada por 5
print("===================================== Execicio 1  ===================================")
lst = []
for i in range(1000):
    lst.append(i+1)
print(lst)
print([number*5 for number in lst])

# Exercicio 2
# crie uma sublista de valores ond todos os elementos da lista sao divisiveis apenas por 10
print("===================================== Execicio 2  ===================================")
print([number for number in lst if number%10==0])

#Exercicio 3
#Exclua da lista todos os valores cujo numero de elementos esteja presente na lista anterior e sejam maiores que 99
print("===================================== Execicio 3  ===================================")
lst_anterior = [number for number in lst if number%10==0]
print(lst_anterior)
print([number for number in lst if (number not in lst_anterior) and (number <100) ])

#Exercicio 4
#com base na lista anterior subtitua todos os valores multiplos de cinco pela palavra "mlt+numero" caso contrario pela palavra "notmlt+numero"
print("===================================== Execicio 4  ===================================")
lst_anterior_3 = [number for number in lst if (number not in lst_anterior) and (number <100) ]
#observe que neste caso "mlt" é o resultado para mod
print([ "mlt"+str(number) if number%5==0  else "notmlt"+str(number) for number in lst_anterior_3])