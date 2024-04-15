# %%
# A função zip() em Python é uma função que agrupa elementos de múltiplas estruturas de dados iteráveis (como listas, tuplas ou outros objetos iteráveis) juntos em pares.
# A função zip() retorna um objeto, zip que pode ser convertido em outra estrutura de dados
# Como uma lista ou dicionário, se necessário

# %%

x = [1,2,3]
y = [4,5,6]
# %%
#Em python retorna um itrator
zip(x, y)
# %%
#ércepa que zip retorna tuplas. Neste caso, uma lista de tuplas
list(zip(x, y))
# %%

#Atenção quando as sequências tiverem números diferentes de elementos
list(zip('ABCD', 'xy'))
# %%

a = [1, 2, 3]
b = [4, 5, 6, 7, 8]

list(zip(a, b))
# %%
d1 = {'a': 1, 'b':2}
d2 = {'c': 4, 'd':5}
# %%
#zip vai unir as chaves
list(zip(d1, d2))
# %%
#zip pode unir os valores (itens)
list(zip(d1, d2.values()))
# %%
#Criando uma função para trocar valores entre 2 dicionários
def trocarValores(d1, d2):

  dictTemp = {}

  for d1key, d2val in zip(d1, d2.values()):
    dictTemp[d1key] = d2val

  return dictTemp

trocarValores(d1, d2)
# %%
