# %%

texto = 'Cientista de dados pode ser uma excelente alternativa de carreira.\n'
texto = texto + "Esses profissionais precisam saber como programar em Python.\n"
texto += 'E, claro, devem ser proficientes em Data Science.'

print(texto)
# %%
import os

arquivo = open(os.path.join('arquivos/cientista.txt'),'w')
# %%
for palavra in texto.split():
  arquivo.write(palavra + ' ')
arquivo.close()
# %%
arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
# %%
#Usando a expressão with o lose é utilizado automaticamente
with open('arquivos/cientista.txt', 'r') as arquivo:
  conteudo = arquivo.read()
# %%
print(len(conteudo))
# %%
