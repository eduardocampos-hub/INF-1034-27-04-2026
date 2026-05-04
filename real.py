import random

def pedraPapelTesoura():
    pontos = 0
    pontosbot = 0
    while True:
    
        opcoes = ['pedra','papel','tesoura']
        escolha = input('Escolha sua jogada (pedra,papel ou tesoura): ')
        escolhabot = random.choice(opcoes)

        print(f'A escolha do bot é: {escolhabot}')

        if escolha == escolhabot:
            print('------EMPATE-----')
        elif escolha == 'papel' and escolhabot == 'pedra' or \
        escolha == 'pedra' and escolhabot == 'tesoura' or \
        escolha == 'tesoura' and escolhabot == 'papel':
            print('----VOCÊ GANHOU!-----')
            pontos += 1
        else:
            print('-----VOCÊ PERDEU!-----')
            pontosbot += 1
        print('=' * 50)
        print('Pontuaçao final:')
        print(f'pontos bot: {pontosbot}')
        print(f'pontos usuario: {pontos}')
        print('=' * 50)
        continuar = input('quer continuar? ')
        if continuar == 'sim':
            print('Boa sorte!')
        else:
            break



def calculadora():
    continuar = "nao"
    while True:
        if  continuar == 'nao':
            
            numero1= float(input("Primeiro número: "))
            operador = input("Operação (+, -, *, /): ")
            numero2= float(input("Segundo número: "))
        else:
            print("Ok!")
            numeronovo=float(input("Qual o proximo numero?"))
            operacaonova=input("Qual a proxima operação?")
            operador=operacaonova
            numero1=resultado
            numero2=numeronovo
        
        if operador == '+':
            resultado = numero1 + numero2
            print (f'{resultado}')   
        elif operador == '-':
            resultado = numero1 - numero2
        
            print (f'{resultado}')
        elif operador == '*':
            resultado = numero1 * numero2
        
            print (f'{resultado}')    
        elif operador == '/' and numero2!=0:
            resultado = numero1 / numero2
            
            print (f'{resultado}')    
        else:   
            print("Erro: Divisão por zero não existe.")
        
        continuar=input("Quer continuar com esse numero? (sim/nao): ")    
calculadora()
