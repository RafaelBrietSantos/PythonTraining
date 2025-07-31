import pyfiglet 
import random 
from time import sleep
import time
print(pyfiglet.figlet_format('Bem Vindo!', font='slant'))
sleep(1)
print(pyfiglet.figlet_format('A...', font='slant'))
sleep(2)
print(pyfiglet.figlet_format('Jornada', font='slant'))

# Animiação
def animar_acao(texto, pontinhos=3, intervalo=0.5):
    print(texto, end='', flush=True)
    for _ in range(pontinhos):
        time.sleep(intervalo)
        print('.', end='', flush=True)
    print()


class personagem:
    def __init__(self, nome, classe, vida, ataque):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque 
    
    def status(self):
        print(f'Nome: {self.nome}  \nClasse: {self.classe}  \nDano: {self.ataque} \nVida: {self.vida}') 


    def atacar(self,alvo):
        # Verifica se o alvo e o heroi esta vivo 
        if self.vida > 0 and alvo.vida > 0:
            print(f'O {self.nome} atacou {alvo.nome} e causou {self.ataque}')
            alvo.vida -= self.ataque
    # Fazer que cada classe tenha ataques diferentes.
    def verificar_derrota(p1, p2):
        if p1.vida <= 0:
            print(f'\n💀 {p1.nome} foi derrotado!\n')
            print(pyfiglet.figlet_format('DERROTA'))
            return True
        elif p2.vida <= 0:
            print(f'\n💀 {p2.nome} foi derrotado!\n')
            print(pyfiglet.figlet_format('VITÓRIA'))
            return True
        return False
    


    def escolher_ataque(self,inimigo):
        # -----Mago-----
        if self.classe == 'Mago':
            print('Escolha um ataque. ')
            #Bola de Fogo = 20 Raio Congelante = 15 Névoa Venenos = 10
            print('[1] Bola de fogo \n[2] Raio congelante \n[3] Névoa Venenosa \n\n')
            Atacar = int(input('Qual ataque vc deseja? '))
            animar_acao(f"{self.nome} preparando um ataque")
            sleep(1)

            
            if Atacar == 1:
                print(f'O {self.nome} teve sucesso em arremeçar a Bola de fogo no {inimigo.nome} ')
                dano = 20
                inimigo.vida -= 20
                print (f'vida do inimigo:{inimigo.vida}')
            if Atacar == 2:
                print(f'O {self.nome} teve sucesso em arremeçar a Raio congelant no {inimigo.nome} ')
                dano = 15
                inimigo.vida -= 15
                print (f'vida do inimigo:{inimigo.vida}')
            if Atacar == 3:
                print(f'O {self.nome} teve sucesso em arremeçar a Névoa Venenosa no {inimigo.nome} ')
                dano = 10
                inimigo.vida -= 10
                print (f'vida do inimigo:{inimigo.vida}')





        if self.classe == 'Guerreiro':
            print('Escolha um ataque. ')
            #Bola de Fogo = 20 Raio Congelante = 15 Névoa Venenos = 10
            print('[1] Espadada \n[2] Soco \n[3] Investida\n\n')
            Atacar = int(input('Qual ataque vc deseja? '))
            animar_acao(f"{self.nome} preparando um ataque")
            sleep(1)


            
            if Atacar == 1:
                print(f'O {self.nome} teve sucesso em atacar com a espada o {inimigo.nome} ')
                dano = 18
                inimigo.vida -= dano
                print (f'vida do inimigo:{inimigo.vida}')
            if Atacar == 2:
                print(f'O {self.nome} acertou o soco no {inimigo.nome} ')
                dano = 10
                inimigo.vida -= dano
                print (f'vida do inimigo:{inimigo.vida}')
            if Atacar == 3:
                print(f'O {self.nome} conseguiu acertar a Investida no {inimigo.nome} ')
                dano = 15
                inimigo.vida -= dano
                print (f'vida do inimigo:{inimigo.vida}')



        if self.classe == 'Arqueiro':
            print('Escolha um ataque. ')
            #Bola de Fogo = 20 Raio Congelante = 15 Névoa Venenos = 10
            print('[1] Flecha Precisa \n[2] Lâmina Curta \n[3] Disparo Múltiplo\n\n')
            Atacar = int(input('Qual ataque vc deseja? '))
            animar_acao(f"{self.nome} preparando um ataque")
            sleep(1)

            
            if Atacar == 1:
                print(f'O {self.nome} deu uma fleshada precisa no {inimigo.nome} ')
                dano = 17
                inimigo.vida -= dano
                print (f'vida do inimigo:{inimigo.vida}')
            if Atacar == 2:
                print(f'O {self.nome} atacou com a lamina curta o {inimigo.nome} ')
                dano = 12
                inimigo.vida -= dano
                print (f'vida do inimigo:{inimigo.vida}')
            if Atacar == 3:
                print(f'O {self.nome} fez o Diparo multiplo no {inimigo.nome} ')
                dano = 16 
                inimigo.vida -= dano
                print (f'vida do inimigo:{inimigo.vida}')
   
    def ataque_aleatorio(self,inimigo):
        if self.classe == 'Mago':
            ataques = {
                1: ("Bola de fogo", 20),
                2: ("Raio congelante", 15),
                3: ("Névoa Venenosa", 10)
            }
            escolha = random.choice(list(ataques.keys()))

            nome_ataque, dano = ataques [escolha]
            animar_acao(f"{self.nome} prepara um ataque")
            sleep(1)


            print(f'\n{self.nome} usou {nome_ataque} contra {inimigo.nome} causando {dano} de dano!')
            inimigo.vida -= dano
            print(f'Vida de {inimigo.nome}: {inimigo.vida}')
    

        if self.classe == 'Guerreiro':
            ataques = {
                1: ("Espadada", 18),
                2: ("Soco", 10),
                3: ("Investida", 15)
            }
            escolha = random.choice(list(ataques.keys()))
            animar_acao(f"{self.nome} prepara um ataque")
            sleep(1)

            nome_ataque, dano = ataques [escolha]
            print(f'\n{self.nome} usou {nome_ataque} contra {inimigo.nome} causando {dano} de dano!')
            inimigo.vida -= dano
            print(f'Vida de {inimigo.nome}: {inimigo.vida}')

        if self.classe == 'Arqueiro':
            ataques = {
                1: ("Flecha Precisa", 17),
                2: ("Lamina Curta", 15),
                3: ("Diparo Multiplo", 16)
            }
            escolha = random.choice(list(ataques.keys()))
            animar_acao(f"{self.nome} prepara um ataque")
            sleep(1)
            nome_ataque, dano = ataques [escolha]
            print(f'\n{self.nome} usou {nome_ataque} contra {inimigo.nome} causando {dano} de dano!')
            inimigo.vida -= dano
            print(f'Vida de {inimigo.nome}: {inimigo.vida}')



# Nome do heroi       
nome = input('qual o seu nome? ').strip().title() 

# Clase do heroi
while True:
    classe = input('qual classe vc deseja?(Guerreiro, Mago, Arqueiro) ') .strip() .title() 
 #if classe != 'Guerreiro' 'Mago' 'Arqueiro': isso é um erro pois seria reconhecido assim GuerreiroMagoArqueiro
    classe_validas = ['Guerreiro', 'Mago', 'Arqueiro']
    if classe not in classe_validas:
        print('Classe não encontrada')
    else:
        break

# Vendo o dando 
if classe == 'Mago':
    ataque = 20
elif classe == 'Guerreiro':
    ataque = 34

elif classe == 'Arqueiro':
    ataque = 15

# Atribuindo a vida
if classe == 'Mago':
    vida = 50
elif classe == 'Guerreiro':
    vida = 80

elif classe == 'Arqueiro':
    vida = 60



# Atribuido dados para a classe dele 
heroi1 = personagem(nome, classe, vida, ataque)
fulano = personagem(nome='Fulano', classe='Mago', ataque=20, vida=60)

heroi1.status()


# ----Batalha---- 

print('\n--- Batalha Iniciada ---\n')
sleep(1)

turno = 1 
while heroi1.vida > 0 and fulano.vida > 0:
    animar_acao(f"\n🔁 Turno {turno} iniciando")

    turno += 1

    # Verifica se fulano ta vivo

    #ataque 
    heroi1.escolher_ataque(fulano)
    sleep(1)
    fulano.ataque_aleatorio(heroi1)
    sleep(1)
    
    
    if personagem.verificar_derrota(heroi1, fulano):
        break

    # Verefica se eu to vivo 
    
    



    # Status dos players
    
    print('\n📊 STATUS ATUAL:')
    heroi1.status()
    print('---------------------')
    fulano.status()
    sleep(2)





