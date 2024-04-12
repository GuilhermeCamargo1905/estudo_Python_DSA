# %%
print('Bem-vindo ao Calculador de Área de Paralelograma')

comprimento = float(input('Escreva o comprimento da base: '))
altura = float(input('Escreva a altura: '))

formula = float(comprimento * altura)
print(formula)
# %%

print('Bem vindo a calculadora')

num1 = float(input('Digite o primeiro numero'))
num2 = float(input('Digite o segundo numero'))

operacao = input("Selecione uma operação (+, -, *, /): ")

if operacao == "+":
  resultado = num1 + num2
  print('O resultado é: ', resultado)
elif operacao == "-":
  resultado = num1 - num2
  print('O resultado é: ', resultado)
elif operacao == "*":
  resultado = num1 * num2
  print('O resultado é: ', resultado)
elif operacao == '/':
  resultado = num1 / num2
  print('O resultado é: ', resultado)
else:
  print('Operacao invalida')

# %%

lista = [32, 20, 11, 21, 40, 32, 21, 45, 32, 56, 78]

def bubble_sort(arr):
  n = len(arr)

  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

print(bubble_sort(lista))