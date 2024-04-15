# %%
# A função reduce() em python é uma função da biblioteca functools que aplica uma determinada função binária a pares consecutivos
# de elementos em uma estrutura de dados iterável
#(como uma lista, tupla ou outro objeto iteravel), reduzindo-a um único valor
# %%

from functools import reduce
# %%
from IPython.display import Image
Image ('arquivos/reduce.png')
# %%
lista = [47, 11, 42, 13]
print(lista)
# %%
def soma(a,b):
  x = a + b
  return x
# %%
#Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
reduce(soma, lista)
# %%
#Usando reduce com lambdda

lst = [47, 11, 42, 13]

reduce(lambda x,y: x+y, lst)
# %%
#Podemos atribuir a função lambda a uma variáveç
max_find2 = lambda a,b: a if (a > b) else b
# %%
type(max_find2)
# %%
#Reduzindo a lista até o valor máximo, através da função criada com a expressão lambda
reduce(max_find2, lst)
# %%
