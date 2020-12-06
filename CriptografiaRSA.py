import math 
import time

def progress_bar(done):
    print("\rProcessando: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')


def test():
    for n in range(4):
        progress_bar(n/3)
        time.sleep(1)
    print('\n')

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

    print('Inverso:', n_anterior)
    return n_anterior



def desencriptar(inverso, chave1):
    arquivo = open('Mensagem_Encriptada.txt', 'r')
    mensagem_encrip = arquivo.read()
    des_encrip = open('Mensagem_Desencriptada.txt', 'w')
    arquivo.close()


    i = 0

    while(i < len(mensagem_encrip)):
        n = ''
        while(1):
            if mensagem_encrip[i] == " ":
                letra = pow(int(n), inverso)%chave1
                if letra == 28:
                    des_encrip.write(' ')
                else:
                    des_encrip.write(chr(letra + 63))
                    break
            n = n + str(mensagem_encrip[i])
            i = i + 1
        i = i +1

    arquivo.close()
    des_encrip.close()



def encriptar(mensagem, chave_publi1, chave_publi2):
    i = 0

    open('Mensagem_Encriptada.txt', 'w')
    arquivo = open('Mensagem_Encriptada.txt', 'a')
    
    while(i < len(mensagem)):

        if ord(mensagem[i]) == 32:
            cript = 28
        elif ord(mensagem[i]) > 64 and ord(mensagem[i]) < 97:
            cript = ord(mensagem[i]) - 63
        elif ord(mensagem[i]) > 96:
            cript = ord(mensagem[i]) - 95

        cript = pow(cript,chave_publi2)%chave_publi1    
        
        arquivo.write(str(cript))
        arquivo.write(' ')

        i = i + 1

    arquivo.close()


while(1):
    print('Escolha uma opção digitando o número corespondente:\n')
    print('1 - Gerar Chave Pública\n')
    print('2 - Encriptar\n')
    print('3 - Desencriptar\n')
    print('0 - Sair do programa\n')

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
        arquivo.close()
        print('\n')
        test()
        print('Chaves geradas com sucesso!\n')
        print('_____________________________________\n')

    
    if opcao == 2:
        print('Digite mensagem que deseja encriptar, sem acentos e caracteres especiais:')
        mensagem = input()
        
        print('Digite as chaves públicas:')
        chave_publi1 = int(input())
        chave_publi2 = int(input())

        encriptar(mensagem, chave_publi1, chave_publi2)
        print('\n')
        test()
        print('Mensagem Encriptada com sucesso!\n')
        print('_____________________________________\n')



    if opcao == 3:
        print('Digite p:')
        p = int(input())
        print('Digite q:')
        q = int(input())
        print('Digite e:')
        e = int(input())

        tontiente = (p - 1) * (q - 1)
        chave1 = p*q
        inverso = calcular_inverso(e,tontiente)

        desencriptar(inverso, chave1)
        print('\n')
        test() 
        print('Mensagem Desencriptada com sucesso!\n')
        print('_____________________________________\n')

    if opcao == 0:
        break
