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
fim = False
frase = ''
print('Bem vindo ao jogo de 21\n1 - Jogar\n2 - Sair')
op = int(input())
if op == 1:
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
            print(f'Soma: {soma}\n')
        if soma > 21 :
            print(f'Perdedor\n')
            fim = True
        else:    
            print(f'1 - Comprar\n2 - Ficar')
            escolha = int(input())
            if escolha == 2:
                if soma == 21:
                    print(f'VENCENDOR!\n')
                else:
                    print(f'PERDEDOR\n')
                fim = True   
            else:
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

      

          

      
