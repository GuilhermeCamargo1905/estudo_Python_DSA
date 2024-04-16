# %%

#Erros e exceções
#Sempre leia as mensagens de erro. Erros fazem parte do processo de aprendizagem e vão nos acompanhar
#em toda jornada de programação, em qualquer linguagem

# %%
#Erro (leia a mensagem)
print('Hello') #print('Hello)
# %%
#Erro (leia mensagem de erro)
print(8 + 8) # 8 + 's'
# %%
#Vamos criar uma função

def numDiv(num1, num2):
  resultado = num1 / num2
  print(resultado)

#execução não gera errp
numDiv(4,2)
# %%
#Execução gerando erro
numDiv(4,0)
# %%

#Utilizando try e except
try:
  print(8 + 's')
except TypeError:
  print('Operação inválida')
# %%
try:
  f = open('./arquivos/testandoerros.txt', 'w')
  f.write('Gravando no arquivo')
except IOError:
  print('Erro: arquivo não encontrado ou não pode ser salvo.')
else:
  print('Conteúdo gravado com sucesso')
  f.close
# %%
try:
    f = open('./arquivos/testandoerros', 'r')
except IOError:
  print('Erro: arquivo não encontrado ou não pode ser lido')
else:
  print('Conteúdo gravado com sucesso')
  f.close()
# %%

try:
  f = open('./arquivos/testandoerros.txt', 'w')
  f.write('Gravando no arquivo')
except IOError:
  print('Erro: arquivo não encontrado ou não pode ser salvo')
else:
  print('Conteúdo gravado com sucesso')
  f.close()
finally:
  print('Comandos no bloco finally são sempre executados')
# %%
def askint():
  try:
    val = int(input('Digite um número: '))
  except:
    print('Você não digitou um número')
    val = int(input('tente novamente, Digite um número: '))
  finally:
    print('Obrigado')
  print(val)

askint()
# %%
def askint():
  while True:
    try:
      val = int(input('Digite um número: '))
    except:
      print('Você não digitou um número')
      continue
    finally:
      print('Obrigado')
    print(val)

askint()
# %%
