'''
Exercicio teste do moodle 
Nome: Guilherme Alves Carvalho
RA: 11202420981 
Data: 28/02/25
'''
def maior_2num(a, b):
    return (a + b + abs (a - b)) / 2

def calcula_3num(x, y, z):
    m = maior_2num(x, y)
    return maior_2num(m, z)
    

x = int(input())
y = int(input())
z = int(input())

print(f"O numero maior é {calcula_3num(x, y, z)}")
