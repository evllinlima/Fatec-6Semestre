# x = [1,2,3]
# y = ['a', 'b', 'c']

# dic = {}
# dic['a'] = 1
# dic['b'] = 2

# print(dic)

# dic['Joao'] = 123456

# print(dic.keys()) #imprime as chaves do dicionário
# print(dic.values()) #imprime os valores do dicionário

# for k, v in dic.items(): #imprime as chaves e os valores do dicionário
#     print(k,'valor:', v)

# print(dic['Joao']) #imprime o valor associado à chave 'Joao'


#exercicio 1

dic = {}
dic['Amanda'] = 1
dic['Bianca'] = 2
dic['Carlos'] = 3
dic['Diego'] = 4
dic['Estevam'] = 5

#exercicio a
print("Imprima todas as chaves do dicionario:", list(dic.keys()))

#exercicio b
print("Imprima todos os valores do dicionario:", list(dic.values()))

#exercicio c
print(dic.items())

#exercicio d
dic = list(dic.items())
print(dic[1])

#exercicio e
print(dic)

#exercicio f
for k, v in dic.items(): #imprime as chaves e os valores do dicionário
      print(k,'tem como valor:', v)

