# %%

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_list[0:]
# %%
objeto_list = ['candelabro', 'vela', 'mesa', 'relógio', 'piano']
objeto_list[0:]
# %%
nome = 'Guilherme'
sobrenome1 = 'Camargo'
sobrenome2 = 'da Silva'
concatenada = nome + ' ' + sobrenome1 + ' ' + sobrenome2
print(concatenada)
# %%
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
tupla.count(4)
# %%
dicio = {

}
# %%
dicio_2 = {'primeiro': 1, 'segundo':  2, 'terceiro': 3}
print(dicio_2)
# %%
dicio_2 = {'primeiro': 1, 'segundo':  2, 'terceiro': 3}
dicio_novo = {'quarto': 4}
dicio_2.update(dicio_novo)
print(dicio_2)
# %%
dicio_3 = {
  'Primeiro_nome': 'Guilherme', 'Segundo_nome': 'Victoria', 'Estado': 'Sao Paulo',
  'idade': [19, 22]
  }
print(dicio_3)
# %%

lista = ['Nomes', 
        ('Alberto', 'Nathalia'), 
        {'idade1': 23, 'idade2': 34},
        30.00
]
print(lista)
# %%
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:19]