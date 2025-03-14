#while 
#estrututura do codigo 

'''while <expressão booleana>:
    instrução_1 
    instrução_2
'''

#UM PROGRAMA QUE IMRPRIME OS N PRIMEIROS NUMEROS NATURAIS
#EXEMPLO DE ESTRUTURA BÁSICA DO WHILE 

'''n = int(input())
i = 1
while i <= n:
    print(i)
    i =  i + 1
print('fim')
'''


'''n = int(input())
i = 1 
media = 0
soma = 0
while i < n: 
    val = float(input())
    media += (val/n)
    i =+ 1
print('média{:.2f}'.format(media))'''

n = int(input())
i = 2
primo = True

while i < n:
    if n % i == 0:
        primo = False
    i = i + 1

if primo and n != 1:
    print('{} é primo'.format(n))
else: 
    print('{} não e primo'.format(n))



