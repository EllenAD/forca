import random     #Importa uma biblioteca, implementa geradores de números, ou seja, gera números aleatórios.

palavras = [''] #As palavras são escolhidas aleatoriamente.
letrasErradas = '' #Irá aparecer as letras erradas que a pessoa escolher.
letrasCertas = ''  #As letras que acertar da palavra escolhida.
escolha= 'sim'

print('As palavras que você escolher serão sorteadas para jogar A Forca.')
while True:
    palavras.append(input('Qual palavra você deseja adicionar à lista: ')) #Adiciona o que for digitado à lista 'palavras'.
    decidir = input('Quer escolher mais palavras?' )
    if decidir == 'sim':  #Se a pessoa quiser adicionar mais palavras para serem sorteadas para o jogo, vai continuar perguntando, se não, o loop para.
        continue
    else:
        break

    

FORCAIMG = ['''    
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''] #O primeiro desenho aparece na tela, conforme a pessoa erra, vai sendo desenhada uma parte do bonequinho.


def principal():  #O def serve para criar funções.
    """
    Função Princial do programa
    """
    print('F O R C A') #Print: imprime na tela o que estiver dentro dos parênteses.

    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True: #Repete infinitamente.
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            print('Voce Perdeu!!!')
            break  #Break: para a execução do while True.
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo(): #Quando a pessoa tiver errado muitos palpites e o desenho do bonequinho já estiver totalmente formado.
    global FORCAIMG 
    if len(letrasErradas) == len(FORCAIMG): #Len: retorna um valor do tipo inteiro, representando a quantidade de caracteres contido na string.
        return True #Retorna uma questão verdadeira.
    else:
        return False #Retorna uma questão falsa.
    
def ganhouJogo(palavraSecreta): 
    global letrasCertas
    ganhou = True #Se as letrasCertas estiverem de acordo com a palavraSecreta, será verdade que a pessoa ganhou.
    for letra in palavraSecreta: #Para a letra que estiver de acordo com a palavraSecreta.
        if letra not in letrasCertas: #Se letra não estiver dentro de letrasCertas.
            ganhou = False  #A pessoa não terá ganhado.
    return ganhou  #Retorna para a variável "ganhou".      
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ") #Input: captura o que for digitado na tela
    palpite = palpite.upper() #O upper deixará a letra maiúscula.
    if len(palpite) != 1:  #if (se): Verifica se uma condição é verdadeira.
        print('Coloque uma unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.') #O elif é uma mistura de if com else. Usamos quando queremos atribuir uma condição para else; quando o if não é executado, executa o elif.
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:  #else (senão): se a condição do if não for verdadeira, essa instrução é executada.
        return palpite #Retorna para a variável, onde a pessoa dará outro palpite.
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas   
    global letrasErradas  #Global: se refere à uma variável já existente para se tornar global, ou seja, a mesma variável para todo o arquivo.
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)]) #Imprime na tela uma parte do bonequinho pendurado na forca porque a pessoa errou um palpite.
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta: 
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:  #Este bloco de comando serve para preencher o espaço "vazio" com as letras que estiverem dentro de letrasCertas, de acordo com a palvraSecreta.'''
        for x in range(len(palavraSecreta)):  
                if letra == palavraSecreta[x]:
                    vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )   #Irá imprimir na tela as letras certas e erradas. 
    print('Erros: ',letrasErradas)
    print(vazio) #Espaço vazio que ainda não foi preenchido.
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()  #random.choice: Gera uma amostra aleatória de uma determinada matriz.

    
principal()

