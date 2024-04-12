# %%

print('Hello World')

# %%

numeros = list(range(1, 101))

# %%
# Percorre a lista de 4 em 4
for numero in numeros:
  if numero % 2 == 0 and numero % 4 == 0:
    print(numero)
# %%
# Utilizando List compreension podemos saber que é por conta das chaves
# Vai gerar o resultado com formato de lista
pares_div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]

print(pares_div4)