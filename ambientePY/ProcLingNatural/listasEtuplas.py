# # lista. É mutável, ou seja, pode ser alterada depois de criada.
# x = [0,1,2,3,4]
# x[0] = 5


# #tupla. É imutável
# y = ("Fundamental", "Media", "Superior")
# #y[0] = 5 #erro


# #lista
# l = list(range(5)) #gera uma lista com os números de 0 a 4
# print(l)
# l.append(10) #adiciona o valor 10 no final da lista
# print(l)
# l.insert(0, 5) #adiciona o valor 5 na posição 0
# print(l)
# l.reverse() #inverte a ordem dos elementos da lista
# print(l)
# l.sort() #ordena a lista
# print(l)
# l.remove(1) #remove o valor 1 da lista
# l.index(5) #retorna o índice do valor 5 na lista
# l.count(10) #numero de vezes que o 10 aparece na lista


# #slice -- fatia [2;5]
# l = list(range(10))
# print(l)
# print(l[2:5]) #imprime os elementos de índice 2, 3 e 4

# print(l[2:8:2]) #imprime os elementos de índice 2, 4 e 6 (passo 2)
# print(l[-5:]) #imprime os últimos 5 elementos da lista
# print(l[:-1]) #imprime todos os elementos da lista, exceto o último


#tupla
# meses = ('jan', 'fev', 'mar')
# print(meses.index('mar')) #retorna o índice do valor 'mar' na tupla
# print(meses.count('jan')) #numero de vezes que 'jan' aparece na tupla


#exercicio 1
l = list(range(10))
# print(l)

# #exercicio a
# l.append(6)
# print(l)

# #exercicio b
# l.insert(2, 7)
# print(l)

# #exercicio c
# l.remove(l[3])
# print(l)

# l.append(4)
# print(l.count(4))

# exercicio 5
print(l)

print(l[0:3])
print(l[2:7])
print(l[0:10:3]) #inicio: 0, fim: 10, passo: 3
print(l[-3:])
print(l[:-4])

# exercicio 6
print(l[5])

# exercicio 7
l[6] = 12
print(l)

# exercicio 8
l.reverse()
print(l)

# exercicio 9
l.sort()
print(l)

