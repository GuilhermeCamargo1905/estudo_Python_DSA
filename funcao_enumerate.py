# %%
#Função enumerate() em Python é uma função que permite iterar sobre uma estrutura de dados
#Como uma lista, tupla ou outro objeto iterável.
#A função enumerate() retorna um objeto enumerado, que pode ser usado em loops para percorrer
# a estrutura de dados e acessar o contador e o valor de cada elemento


# %%
seq = ['a', 'b', 'c']
# %%
enumerate(seq)
# %%
list(enumerate(seq))
# %%
for indice, valor in enumerate(seq):
  print(indice, valor)
# %%
for indice, valor in enumerate(seq):
  if indice >= 2:
    break
  else:
    print(valor)
# %%

lista = ['Marketing', 'Tecnologia', 'Business']

for i, item in enumerate(lista):
  print(i, item)
# %%
for i, item in enumerate(range(10)):
  print(i, item)
# %%
