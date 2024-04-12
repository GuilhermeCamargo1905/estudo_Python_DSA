# %%
# Abrir o arquivo para leitura
arq1 = open("arquivos/arquivo1.txt", "r") # R = read
# %%
type(arq1)
# %%
#Lendo o arquivo
print(arq1.read())
# %%
#Contar o número de caracteres
print(arq1.tell())
# %%
#Retornar para o inicio do arquivo
print(arq1.seek(0,0))
# %%
arq2 = open("arquivos/arquivo2.txt", "w") # W = para gravar no documento
# %%
#Como abrimos o arquivo apenas para gravação não podemos dar comandos de leitura
print(arq2.read())
# %%
#Gravando arquivo
arq2.write("Aprendendno a programar em Python")
# %%
arq2.close()
# %%
arq2 = open("arquivos/arquivo2.txt", "r")
# %%
print(arq2.read())
# %%
#Acrescentando conteúdo
arq2 = open("arquivos/arquivo2.txt", "a") #A = appen
# %%
arq2.write(" E a metodologia de ensino da Data Science Academy facilita o aprendizado")
# %%
arq2 = open("arquivos/arquivo2.txt", "r")
# %%
print(arq2.read())
# %%
# Dividindo arquivo em linhas
f = open("arquivos/salarios.csv", "r")

data = f.read()

rows = data.split('\n')

print(rows)
# %%
#Dividno o arquivo em colunas
f = open("arquivos/salarios.csv", "r")

data = f.read()

rows = data.split('\n')

full_data = []

for row in rows:
  split_row = row.split(',')
  full_data.append(split_row)
print(full_data)
# %%
#Contando as linhas de um arquivo

f = open("arquivos/salarios.csv", "r")

data = f.read()

rows = data.split('\n')

for row in rows:
  split_row = row.split(',')
  full_data.append(split_row)

count = 0
for row in full_data:
  count += 1
print(count)
# %%
#Contando o número de colunas de um arquivo
f = open("arquivos/salarios.csv", "r")

data = f.read()

rows = data.split('\n')

full_data = []

for row in rows:
  split_row = row.split(',')
  full_data.append(split_row)
  first_row = full_data[0]
count = 0

for column in first_row:
  count = count + 1
print(count)
# %%
#Importando dataset com pandas

import pandas as pd

pd.__version__

arquivo = "arquivos/salarios.csv"

df = pd.read_csv(arquivo)
df.head()