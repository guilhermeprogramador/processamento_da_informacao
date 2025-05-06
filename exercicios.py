def conjunto_intersecao (vetor_a, vetor_b):
    intersecao = []
    for elemento in vetor_a:
        if elemento in vetor_b and elemento not in intersecao:
            intersecao.append(elemento)
    return intersecao

def conjunto_contido(vetor_a, vetor_b):
    for elemento in vetor_a:
        if elemento not in vetor_b:
            return False
    return True

def conjunto_uniao(vetor_a, vetor_b):
    uniao = []
    for elemento in vetor_a:
        if elemento not in vetor_b:
            uniao.append(uniao)
        
            


a = [4, 5, 6]
b = [1, 2, 3, 4, 5]

print(conjunto_intersecao(a, b))
print(conjunto_contido(a, b))
print(conjunto_uniao(a, b))
