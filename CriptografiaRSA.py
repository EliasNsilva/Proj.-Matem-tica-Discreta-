import math 
import time


#Funções para gerar a barra de progresso
def progress_bar(done):
    print("\rProcessando: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')


def test():
    for n in range(4):
        progress_bar(n/3)
        time.sleep(1)
    print('\n')

#########################################

def e_primo(x):#função para descobrir se o número é primo ou não
    i = 2

    while(1):
        if i > math.sqrt(x):#Limitando até a raiz do número
            return 1  
        if x % i == 0:#verificando se existem divisores exatos
            return 0   
        i = i + 1 

def mdc(x,y):#função para achar o MDC entre dois números, usando o algoritimo de Euclides
    while(1):
        if y == 1:#se y = 1 logo eles são primos entre si
            return 1
        if y == 0:#caso y chegue a ser igual a zero não são primos entre si
            return 0

        aux = y
        y = x % y
        x = aux 


def calcular_inverso(e,totiente_de_euler):#função para achar o inverso
    divisores = [0]
    contador = 0

    #achando o inverso utilizando o algoritimo de Euclides

    if totiente_de_euler > e:
        aux = e
        e = totiente_de_euler
        totiente_de_euler = aux

    mod = e

    while totiente_de_euler > 0:
        divisores.append(int(e/totiente_de_euler))

        resto = e % totiente_de_euler
        e = totiente_de_euler
        totiente_de_euler =  resto

        contador += 1

    verificar_negatividade = contador
    n_anterior = 0
    n_atual = 1
    contador -= 1

    while contador > -1:
        n_substituto = n_atual
        n_atual = divisores[contador] * n_atual + n_anterior
        n_anterior = n_substituto
        contador -= 1

    if verificar_negatividade % 2 == 0:
        n_anterior = n_anterior * (-1)
        n_anterior = mod + n_anterior

    return n_anterior



def desencriptar(inverso, chave1):
    arquivo = open('Mensagem_Encriptada.txt', 'r')#abrindo o arquivo Mensagem_Encriptada.txt 
    mensagem_encrip = arquivo.read()#colocando os dados de Mensagem_Encriptada.txt em uma variavel
    des_encrip = open('Mensagem_Desencriptada.txt', 'w')#criando ou limpando o arquivo Mensagem_Desencriptada.txt
    arquivo.close()


    i = 0

    while(i < len(mensagem_encrip)):
        n = ''
        while(1):
            if mensagem_encrip[i] == " ":
                letra = pow(int(n), inverso)%chave1#desencriptando
                if letra == 28:#caso especial do espaço
                    des_encrip.write(' ')
                else:
                    des_encrip.write(chr(letra + 63))#convertendo para string pela tabela ASCII e salvando no arquivo
                break
            n = n + str(mensagem_encrip[i])
            i = i + 1
        i = i +1

    arquivo.close()
    des_encrip.close()



def encriptar(mensagem, chave_publi1, chave_publi2):
    i = 0

    open('Mensagem_Encriptada.txt', 'w')
    arquivo = open('Mensagem_Encriptada.txt', 'a')#atribuindo os dados do arquivo Mensagem_Encriptada.txt para uma variavel
    
    while(i < len(mensagem)):

        if ord(mensagem[i]) == 32:#função ord retorna a posição da tabela ASCII
            cript = 28#caso especial do caractere "espaço"
        elif ord(mensagem[i]) > 64 and ord(mensagem[i]) < 97:#caso seja letra maiuscula
            cript = ord(mensagem[i]) - 63#utilizando as posiçôes da tabala ASCII que fique no intervalo desejado(a=2, z=27)
        elif ord(mensagem[i]) > 96:#caso seja letra minuscula
            cript = ord(mensagem[i]) - 95

        cript = pow(cript,chave_publi2)%chave_publi1 #encripitando a letra  
        
        arquivo.write(str(cript))#salvando no arquivo
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
        
        #lendo e verificando se os valores são primos

        primo1 = int(input())
        if e_primo(primo1) == 0:
            print('\nEsse número não é primo, tente novamente!')
            print('_____________________________________\n')
            continue

        primo2 = int(input())
        if e_primo(primo2) == 0:
            print('\nEsse número não é primo, tente novamente!')
            print('_____________________________________\n')
            continue

        #gerando o tontiente de euler e a chave 1    
        tontiente = (primo1 - 1) * (primo2 - 1)
        chave1 = primo1 * primo2

        #lendo a chave 2

        print('\nDigite um número expoente que seja relativamente primo a', tontiente)
        chave2 = int(input())

        if mdc(chave2, tontiente) == 0:#verificando se ela é relativamente prima ao tontiente de euler 
            print('\nEsse número não é válido, tente novamente!')
            print('_____________________________________\n')
            continue
        
        arquivo = open('Chave_Pública.txt', 'w')
        arquivo.write(str(chave1))
        arquivo.write('\n')
        arquivo.write(str(chave2))
        arquivo.close()
        test()
        print('\nChaves geradas com sucesso!\n')
        print('_____________________________________\n')

    
    elif opcao == 2:
        print('\nDigite mensagem que deseja encriptar, sem acentos e caracteres especiais:')
        mensagem = input()
        
        print('Digite as chaves públicas:')
        chave_publi1 = int(input())
        chave_publi2 = int(input())

        encriptar(mensagem, chave_publi1, chave_publi2)#função para encriptar
        test()
        print('\nMensagem Encriptada com sucesso!\n')
        print('_____________________________________\n')



    elif opcao == 3:
        print('Digite p:')
        p = int(input())
        print('Digite q:')
        q = int(input())
        print('Digite e:')
        e = int(input())

        tontiente = (p - 1) * (q - 1)
        chave1 = p*q
        inverso = calcular_inverso(e,tontiente)#função para achar o inverso utilizado para desencriptar a mensagem

        desencriptar(inverso, chave1)#função para desencriptar
        print('\n')
        test() 
        print('Mensagem Desencriptada com sucesso!\n')
        print('_____________________________________\n')

    elif opcao == 0:
        break
