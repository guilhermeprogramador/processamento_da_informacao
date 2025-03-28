'''
programa que dá o maior divisor comum entre dois numeros

'''

def calcula_divisor(x, y):
    if y == 0:
        return x
    return(calcula_divisor(y, x % y))

num1 = int(input())
num2 = int(input())

print(calcula_divisor(num1, num2))
