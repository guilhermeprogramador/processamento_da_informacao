'''
programa que calcula o investimento 
exercicio 2, aula 3

'''

montante_Inicial = float(input("investimento"))

taxa_Juros = float(input("Juros"))

meses_Investimento = int(input("Meses investido"))

montante_final = montante_Inicial * (1 + taxa_Juros) ** meses_Investimento 

print(montante_final)




