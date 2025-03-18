#data a ser calculada
ano = int(input('ano'))
mes = int(input('mes'))
dia = int(input('dia'))

#informação do personagem 
nome = input('nome')
ano_nascimento = int(input('ano nascimento'))
mes_nascimento = int(input('mes nascimento'))
dia_nascimento = int(input('dia nascimento'))

idade_calculada = ano - ano_nascimento

if (mes > mes_nascimento) or (mes == mes_nascimento and dia_nascimento < dia):
    print('{}-{}-{}: {} tem {} anos'.format(ano, mes, dia, nome, idade_calculada))
else: 
    print('{}-{}-{}: {} tem {} anos'.format(ano, mes, dia, nome, idade_calculada - 1))
