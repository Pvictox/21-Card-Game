# Bibliotecas e variáveis
from pygame import mixer
import os
import random
from time import sleep
random.seed()
mixer.init()
mixer.music.load('carddrawn.mp3')
cartas = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
mao = soma = 0
val = 0
frase = ''
main = True
# -------------------
while main:
    os.system('cls')
    fim = False
    flag = True
    print('Bem vindo ao jogo de 21!\n1 - SinglePlayer\n2 - Vs Computador\n3 - Sair')
    op = int(input())
    if op == 1:
        while flag:
            os.system('cls')
            print('Modo SinglePlayer selecionado.\n1 - Jogar\n2 - Voltar')
            op = int(input())
            if op == 1:
                fim = False
                flag = False
                main = False
                os.system('cls')
                while fim == False:
                    if mao == 0:
                        print('Sua mão está vazia. Comprando 3 cartas...')
                        frase = ''
                        while mao < 3:
                            val = random.choice(cartas)
                            mixer.music.play()
                            val = str(val)
                            if 'K' in val:
                                soma += 13
                            elif 'Q' in val:
                                soma +=12
                            elif 'J' in val:
                                soma+=11
                            else:
                                val = int(val)
                                soma+=val
                            mao = mao + 1
                            val = str(val)
                            val = " "+val
                            frase += (val)
                            print(f'{val}', end= ' ') 
                            sleep(1)
                        print(u'\n\u001b[31mSoma: {}\u001b[0m\n'.format(soma))
                    if soma > 21 :
                        print(f'Perdedor\n')
                        fim = True
                    elif soma == 21:
                        print('Vencedor!\n')   
                        fim = True 
                    else:    
                        print(f'1 - Comprar\n')
                        escolha = int(input())
                        if escolha == 1:
                            os.system('cls')
                            frase = frase.lstrip()
                            mixer.music.play()
                            val = random.choice(cartas)
                            val = str(val)
                            if 'K' in val:
                                soma += 13
                            elif 'Q' in val:
                                soma +=12
                            elif 'J' in val:
                                soma+=11
                            else:
                                val = int(val)
                                soma+=val
                            val = str(val)
                            val = " "+val
                            frase += (val)
                            print(f'{frase}', end= ' ') 
                            print(f'Soma: {soma}')
                            sleep(1)      
                    if fim == True:
                        op2 = 4
                        while op2 <1 or op2>3:
                            print('O que deseja fazer?\n1 - Jogar denovo\n2 - Voltar ao menu inicial\n3 - Sair')
                            op2 = int(input())
                            if op2 == 1:
                                os.system('cls')
                                fim = False
                                mao = 0
                                soma = 0
                            elif op2 == 2:
                                main = True
                                mao = 0
                                soma = 0
                            elif op2 <1 or op2 >3:
                                os.system('cls')
                                print('Selecione um opção válida\n')
                                sleep(2)
            elif op <= 0 or op > 2:
                os.system('cls')
                print('Selecione um opção válida\n')
                sleep(2)
    elif op == 2:
            os.system('cls')
            print('Modo vs Computador selecionado.\n1 - Jogar\n2 - Voltar')
            sleep(2)
    elif op > 3 or op < 1:
            os.system('cls')
            print('Selecione um opção válida\n')
            sleep(2)
    else:
        main = False



          

      
