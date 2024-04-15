# %%

#Função Map
# A função map() em Python é uma função que aplica uma determinada função a cada elemento de uma estrutura de dados iterável 
#(Como uma lista, tupla ou outro objeto iteravel)
# A função map() retorna um objeto que pode ser convertido em outra estrutura de dados
# como uma lista, se necessário

# %%

def potencia(x):
  return x ** 2
# %%
numeros = [1, 2, 3, 4, 5]
# %%
numeros_ao_quadrado = list(map(potencia, numeros))
# %%
print(numeros_ao_quadrado)
# %%
def fahrenheit(T):
  return ((float(9)/5)* T + 32)
def celsius(T):
  return((float(5)/9)*(T - 32))

temperaturas = [0,22.5, 40, 100]

# %%
#em python 3 a função map retorna um iterator
map(fahrenheit, temperaturas)

# %%
#transformando em lista
list(map(fahrenheit, temperaturas))
# %%
#usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
  print(temp)
# %%
#convertendo para celsius
map(celsius, temperaturas)
# %%
list(map(celsius, temperaturas))
# %%
#usando expressão lambda
map(lambda x:(5/9) * (x - 32), temperaturas)
# %%
list(map(lambda x:(5/9) * (x - 32), temperaturas))

# %%
#somando os elementos de 2 linhas
a = [1,2,3,4]
b = [5,6,7,8]

# %%
list(map(lambda x,y:x+y, a, b))
# %%
#Somando os elementos de 3 listas
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

# %%
list(map(lambda x , y, z : x + y + z, a, b, c))
# %%
