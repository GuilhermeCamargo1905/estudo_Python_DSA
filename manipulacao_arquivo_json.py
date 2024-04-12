# %%
# Criando um dicionário
dict_guido = {'nome': 'Guido van Rossum',
              'linguagem': 'Python',
              'similar': ['c', 'Modula-3', 'lisp'],
              'users': 1000000}
# %%
for k, v in dict_guido.items():
  print(k,v)
# %%
# Importando modulo Json
import json
# %%
# Convertendo o dicionario para um arquivo json
json.dumps(dict_guido)

# %%
with open('arquivos/dados.json', 'w') as arquivo:
  arquivo.write(json.dumps(dict_guido))
# %%
