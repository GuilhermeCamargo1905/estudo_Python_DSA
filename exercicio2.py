# %%

def pares():
  for i in range(2, 21, 2):
    print(i)

pares()

# %%
def maiuscula(nome):
  print(nome.upper())
  return

nome = input('Digite o seu nome: ')
maiuscula(nome)


# %%

lista = ['maça', 'banana', 'laranja', 'pêra']
print(lista)
lista.append('abacaxi')
lista.append('mexerica')
print(lista)
# %%
def printNum(arg1, *lista ):
  print(arg1)
  for i in lista:
    print(i)
  return;

printNum(100)
printNum('A', 'B', 'C')
# %%
soma = lambda arg1, arg2: arg1 + arg2
print('A soma é: ', soma(22, 43))
# %%
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)
# %%
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print (list(Fahrenheit))
# %%
[x**2 for x in range(1,11)]
# %%
palavras = ["maça", "coiote", "banana", "terreno", "Python"]
resultado = [x for x in palavras if "a" in x]
print(resultado)
# %%
resultado = [x for x in range(10) if x < 5]
print(resultado)
# %%

dia_da_semana = input('Que dia da semana é estamos: ')

if dia_da_semana == 'Domingo' or dia_da_semana == 'Sábado':
  print('Hoje é dia de descanso')
else:
  print('Você precisa trabalhar!')
# %%
lista = ['Morango', 'Maça', 'Pera', 'Manga']

for fruta in lista:
  if fruta == 'Morango':
    print('Morango está na lista')
  else:
    print('Morango não está da lista')
# %%
tup1 = (1, 2, 3, 4)
lista = []

for i in tup1:
  novo_valor = i * 2
  lista.append(novo_valor)
print(lista)
# %%
for i in range(100, 150, 2):
  print(i)
# %%
temp = 40
while temp > 35:

  print(temp)
  temp = temp - 1
# %%
contador = 0

while contador < 100:
  if contador == 23:
    break
  print(contador)
  contador += 1
# %%
numeros = list()
i = 4
while (i <= 20):
  numeros.append(i)
  i = i+2
print(numeros)
# %%
nums = range(5, 35, 2)
print(list(nums))
# %%
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
  print('Vista roupas leves.')
else:
  print('Busque seus casacos.')
# %%
frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 

count = 0
for caracter in frase:
  if caracter == 'r':
    count += 1
print('O carcter r aparece %s vezes na frase.'%(count))