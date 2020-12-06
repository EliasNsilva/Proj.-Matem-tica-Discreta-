import math 
import tqdm 

def calcular_inverso(e,totiente_de_euler):
    divisores = [0]
    contador = 0

    if totiente_de_euler > e:
        aux = e
        e = totiente_de_euler
        totiente_de_euler = aux

    while totiente_de_euler > 0:
        divisores.append(int(e/totiente_de_euler))

        resto = e % totiente_de_euler
        e = totiente_de_euler
        totiente_de_euler =  resto

        contador += 1

    n_anterior = 0
    n_atual = 1
    contador -= 1
    verificar_negatividade = contador

    while contador > -1:
        n_substituto = n_atual
        n_atual = divisores[contador] * n_atual + n_anterior
        n_anterior = n_substituto
        contador -= 1

    if verificar_negatividade % 2 == 0:
        n_anterior = n_anterior * (-1)

    return n_anterior

def e_primo(x):
    i = 2

    while(1):
        if i > math.sqrt(x):
            return 1  
        if x % i == 0:
            return 0   
        i = i + 1 

def mdc(x,y):
    while(1):
        if y == 1:
            return 1
        if y == 0:
            return 0

        aux = y
        y = x % y
        x = aux 


while(1):
    print('Escolha uma opção digitando o número corespondente:\n')
    print('1 - Gerar Chave Pública\n')
    print('2 - Encriptar\n')
    print('3 - Desencriptar\n')

    opcao = int(input())

    if opcao == 1:
        print('Digite dois números primos:')
        
        primo1 = int(input())
        if e_primo(primo1) == 0:
            print('Esse número não é primo, tente novamente!')
            continue

        primo2 = int(input())
        if e_primo(primo2) == 0:
            print('Esse número não é primo, tente novamente!')
            continue

        tontiente = (primo1 - 1) * (primo2 - 1)
        chave1 = primo1 * primo2

        print('Digite um número expoente que seja realativamente primo a', tontiente)
        chave2 = int(input())

        if mdc(chave2, tontiente) == 0:
            print('Esse número não é válido, tente novamente!')
            continue
        
        arquivo = open('Chave_Pública.txt', 'w')
        arquivo.write(str(chave1))
        arquivo.write('\n')
        arquivo.write(str(chave2))
        arquivo.close

    
    break
