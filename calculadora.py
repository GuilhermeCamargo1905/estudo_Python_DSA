# %%
def soma():
  num1 = float(input('Digite o primeiro numero: '))
  num2 = float(input('Digite o segundo numero: '))
  somar = num1 + num2
  print('O resultado da soma entre ', num1, ' e ', num2, 'é de: ', somar)

def sub():
  num1 = float(input('Digite o primeiro numero: '))
  num2 = float(input('Digite o segundo numero: '))
  subtracao = num1 - num2
  print('O resultado da subtração entre ', num1, ' e ', num2, 'é de: ', subtracao)

def multi():
  num1 = float(input('Digite o primeiro numero: '))
  num2 = float(input('Digite o segundo numero: '))
  multiplicacao = num1 * num2
  print('O resultado da multiplicação entre ', num1, ' e ', num2, 'é de: ', multiplicacao)

def divi():
  num1 = float(input('Digite o primeiro numero: '))
  num2 = float(input('Digite o segundo numero: '))
  divisao = num1 / num2
  print('O resultado da divisão entre ', num1, ' e ', num2, 'é de: ', divisao)

opcao = 0
print('Bem vindo a calculadora')
while opcao != 5:

  opcao = float(input('Digite a operação: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n 5 - Sair'))

  if opcao == 1:
    soma()
  elif opcao == 2:
    sub()
  elif opcao == 3:
    multi()
  elif opcao == 4:
    divi()
  else:
    print('Fechando a calculadora')
# %%

