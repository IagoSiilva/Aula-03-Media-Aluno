# -*- coding: utf-8 -*-
"""aula03MediaAluno.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZrUmovNUtBxNxqUCC2iXKn_LPSVI9ChI
"""

#Média de um aluno
aluno = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1+n2+n3)/3
if media >= 7:
    situacao = 'Foi aprovado'
elif media >= 5:
    situacao = 'Ficou em recuperação'
else:
    situacao = 'Foi reprovado'
print(f'O aluno {aluno} {situacao} com média {media:.2f}' )