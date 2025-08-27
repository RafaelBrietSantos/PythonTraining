# Importações necessárias para o jogo
import pyfiglet 
import random 
from time import sleep

# --- Definição das Classes e Funções de Jogo ---

# Dicionários que armazenam os atributos e ataques de cada classe.
# Usar dicionários deixa o código muito mais limpo e fácil de expandir!
classe_atributos = {
    'Mago': {'vida': 50, 'ataque': 20},
    'Guerreiro': {'vida': 80, 'ataque': 34},
    'Arqueiro': {'vida': 60, 'ataque': 15}
}

ataques_por_classe = {
    'Mago': {
        'Bola de Fogo': 20,
        'Raio Congelante': 15,
        'Névoa Venenosa': 10
    },
    'Guerreiro': {
        'Espadada': 18,
        'Soco': 10,
        'Investida': 15
    },
    'Arqueiro': {
        'Flecha Precisa': 17,
        'Lamina Curta': 12,
        'Disparo Multiplo': 16
    }
}



# --- Definição dos Inimigos ---
# Dicionário com os atributos de cada inimigo.
inimigo_atributos = {
    'Sombra do Medo': {'classe': 'Mago', 'vida': 30, 'ataque': 10},
    'Sombra da Perda': {'classe': 'Guerreiro', 'vida': 45, 'ataque': 8},
    'Sombra do Arrependimento': {'classe': 'Arqueiro', 'vida': 35, 'ataque': 12},
    'Sombra do Vazio': {'classe': 'Mago', 'vida': 50, 'ataque': 15},
    'O Criador do Silêncio': {'classe': 'Guerreiro', 'vida': 100, 'ataque': 25}
}


# Este dicionário representa o mapa do jogo.
# 'descricao': A história e a atmosfera do local.
# 'saidas': As direções possíveis e para qual local elas levam.
# 'itens': Os objetos que o jogador pode encontrar.
# 'inimigo': A manifestação de uma Sombra que o jogador deve enfrentar.

mapa = {
    'caverna_do_inicio': {
        'descricao': 'Você desperta no chão frio de uma caverna, com a mente vazia, como se um pedaço de você tivesse sido arrancado. O eco de uma memória recém-perdida reverbera nas paredes de pedra, brilhando com uma luz fraca. A única direção que parece real é um caminho iluminado ao leste.',
        'saidas': {'leste': 'sala_central_dos_ecos'},
        'itens': ['lanterna_de_eco'],
        'inimigo': None
    },
    'sala_central_dos_ecos': {
        'descricao': 'Você adentra a Sala Central dos Ecos. O ar vibra e ressoa com a sinfonia caótica de risadas, sussurros e lamentações de milhares de almas. Fragmentos de memórias flutuam ao seu redor como poeira brilhante. Quatro corredores se abrem: um ao norte, um ao sul, um a leste e um de volta para o oeste.',
        'saidas': {'oeste': 'caverna_do_inicio', 'norte': 'corredor_do_desespero', 'leste': 'sala_da_melancolia', 'sul': 'labirinto_do_arrependimento'},
        'itens': [],
        'inimigo': None
    },
    'corredor_do_desespero': {
        'descricao': 'Um corredor longo e claustrofóbico. A cada passo, murmúrios de desespero se tornam mais altos, como se fossem a sua própria voz. O ar é frio e pesado, e a sensação de que algo te persegue é forte. O caminho continua apenas para o norte.',
        'saidas': {'sul': 'sala_central_dos_ecos', 'norte': 'sala_das_lagrimas_esquecidas'},
        'itens': [],
        'inimigo': 'Sombra do Medo'
    },
    'sala_das_lagrimas_esquecidas': {
        'descricao': 'O chão está úmido com um líquido salgado. Pequenos cristais de luz cintilam, refletindo imagens distorcidas de pessoas chorando por algo que não se lembram. Um pequeno lago de águas turvas se forma no centro. O único caminho de volta é para o sul.',
        'saidas': {'sul': 'corredor_do_desespero'},
        'itens': ['frasco_de_lagrimas'],
        'inimigo': 'Sombra da Perda'
    },
    'sala_da_melancolia': {
        'descricao': 'Você chega a um jardim de flores murchas. Suas pétalas secas parecem carregar o peso de mil anos de tristeza. A melancolia no ar é tão densa que sufoca. Para o oeste, você vê a Sala Central. Para o leste, há uma porta de madeira com o símbolo de uma lágrima.',
        'saidas': {'oeste': 'sala_central_dos_ecos', 'leste': 'galeria_da_esperanca'},
        'itens': [],
        'inimigo': None
    },
    'galeria_da_esperanca': {
        'descricao': 'Feixes de luz dourada perfuram o teto rachado da galeria, iluminando o caminho à frente. Pássaros azuis, feitos de puro eco, cantam uma melodia que enche seu coração de uma esperança quase esquecida. O caminho para o oeste leva de volta à Sala da Melancolia.',
        'saidas': {'oeste': 'sala_da_melancolia'},
        'itens': ['pluma_dourada'],
        'inimigo': 'Sombra do Arrependimento'
    },
    'labirinto_do_arrependimento': {
        'descricao': 'A entrada do labirinto se fecha atrás de você. Os caminhos se retorcem e se sobrepõem, e você sente o peso de cada erro que já cometeu. Ao sul, o ar fica pesado; a leste, você sente um calor intenso. A única certeza é que o norte leva de volta à Sala Central.',
        'saidas': {'norte': 'sala_central_dos_ecos', 'leste': 'cratera_da_perdicao', 'sul': 'camara_do_silencio_eterno'},
        'itens': [],
        'inimigo': None
    },
    'cratera_da_perdicao': {
        'descricao': 'Uma cratera escura e gigante domina o local, soltando um calor opressor. Do seu fundo, um sussurro vazio e frio se levanta, como se estivesse te convidando a se juntar ao esquecimento total. O caminho de volta é para o oeste.',
        'saidas': {'oeste': 'labirinto_do_arrependimento'},
        'itens': ['fragmento_de_memoria'],
        'inimigo': 'Sombra do Vazio'
    },
    'camara_do_silencio_eterno': {
        'descricao': 'Você chegou ao centro do Silêncio. É um lugar onde a luz não brilha e o som não viaja. A única coisa que existe é uma figura solitária no centro da sala, a fonte de todo o caos. Você sente que a batalha final está prestes a começar. Para o norte, você sente uma fenda que pode ser sua única saída.',
        'saidas': {'norte': 'labirinto_do_arrependimento'},
        'itens': [],
        'inimigo': 'O Criador do Silêncio'
    },
}
# Função de animação para dar um toque de RPG.
def animar_acao(texto, pontinhos=3, intervalo=0.5):
    print(texto, end='', flush=True)
    for _ in range(pontinhos):
        sleep(intervalo)
        print('.', end='', flush=True)
    print()

# Função que verifica se um dos personagens foi derrotado.
# Foi movida para fora da classe para ser uma função global,
# pois ela não depende de um objeto 'personagem' específico.
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


class Personagem:
    # O método '__init__' inicializa as propriedades do objeto.
    def __init__(self, nome, classe, vida, ataque, ):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque 
        
    
    # O método 'status' exibe as informações do personagem.
    def status(self):
        print(f'\nNome: {self.nome} \nClasse: {self.classe} \nDano: {self.ataque} \nVida: {self.vida}') 

    # Método para o ataque do jogador (escolha manual).
    def escolher_ataque(self, inimigo):
        print('Escolha um ataque:')
        
        # Acessa o dicionário de ataques da classe do herói.
        ataques_disponiveis = ataques_por_classe[self.classe]
        
        # Mostra os ataques disponíveis de forma automática, usando um loop.
        for i, (nome_ataque, dano) in enumerate(ataques_disponiveis.items(), 1):
            print(f"[{i}] {nome_ataque} (Dano: {dano})")
        
        # Pega a escolha do usuário.
        escolha = int(input('\nQual ataque você deseja? ')).strip()
        
        animar_acao(f"{self.nome} preparando um ataque")
        sleep(1)
        
        # Usa a escolha para encontrar o ataque e o dano no dicionário.
        nomes_ataques = list(ataques_disponiveis.keys())
        ataque_escolhido = nomes_ataques[escolha - 1]
        dano_causado = ataques_disponiveis[ataque_escolhido]
        
        print(f'O {self.nome} usou {ataque_escolhido} e causou {dano_causado} de dano em {inimigo.nome}!')
        inimigo.vida -= dano_causado
        print(f'Vida de {inimigo.nome}: {inimigo.vida}')

    # Método para o ataque do inimigo (aleatório).
    def ataque_aleatorio(self, inimigo):
        # Pega o dicionário de ataques da classe do inimigo.
        ataques_disponiveis = ataques_por_classe[self.classe]
        
        # Escolhe um ataque aleatório do dicionário.
        nome_ataque, dano = random.choice(list(ataques_disponiveis.items()))
        
        animar_acao(f"{self.nome} prepara um ataque")
        sleep(1)
        
        print(f'\n{self.nome} usou {nome_ataque} contra {inimigo.nome} causando {dano} de dano!')
        inimigo.vida -= dano
        print(f'Vida de {inimigo.nome}: {inimigo.vida}')

def Batalha(heroi, inimigo):
    # ---- Batalha ---- 
    print('\n--- Batalha Iniciada contra ' + inimigo.nome + ' ---\n')
    sleep(1)

    turno = 1 
    while heroi.vida > 0 and inimigo.vida > 0:
        animar_acao(f"\n🔁 Turno {turno} iniciando")
        turno += 1

        # Ataque do Herói
        heroi.escolher_ataque(inimigo)
        sleep(1)
        # Checar se a batalha terminou
        if verificar_derrota(heroi, inimigo):
            break
        # Ataque do Inimigo
        inimigo.ataque_aleatorio(heroi)
        sleep(1)
        
        # Checar se a batalha terminou
        if verificar_derrota(heroi, inimigo):
            break

        # Status dos personagens após o turno
        print('\n📊 STATUS ATUAL:')
        heroi.status()
        print('---------------------')
        inimigo.status()
        sleep(2)




# --- Fluxo Principal do Jogo ---

'''print(pyfiglet.figlet_format('Bem Vindo!', font='slant'))
sleep(1)
print(pyfiglet.figlet_format('A...', font='slant'))
sleep(2)
print(pyfiglet.figlet_format('O Silêncio dos Ecos', font='slant'))'''


# Entrada do jogador para escolher nome e classe.
nome = input('Qual o seu nome? ').strip().title() 

while True:
    classe = input('Qual classe você deseja? (Guerreiro, Mago, Arqueiro) ').strip().title()
    if classe not in classe_atributos:
        print('Classe não encontrada. Tente novamente.')
    else:
        break
# --- Fluxo Principal do Jogo ---
# Criação dos personagens usando os dados dos dicionários.
atributos_heroi = classe_atributos[classe]

heroi = Personagem(nome, classe, atributos_heroi['vida'], atributos_heroi['ataque'])
inventario = [] 

# Inimigo fixo para o teste.
# fulano = Personagem(nome='Fulano', classe='Mago', **classe_atributos['Mago'])

heroi.status()

# --- Localização ---

localizacao_atual = 'caverna_do_inicio'

local_anterior = ''
locais_visitados = set()

# --- Loop Principal ---
while True:
    
    
    # Acessa o dicionário do mapa usando a chave 'localizacao_atual'
    local_atual_info = mapa[localizacao_atual]

    # 1. VERIFICAR SE O LOCAL MUDOU
    # Verifique se a string da localizacao_atual é diferente da anterior.
    if local_atual_info != local_anterior:
        # O jogo se pergunta: "Eu já estive aqui antes?"
        if localizacao_atual in locais_visitados:
            print(f'Voce voltou para {localizacao_atual}')
        else:
            # Se a resposta for "não", imprima a descrição completa
            # e ADICIONE o local à sua memória.
            print('\n' + local_atual_info['descricao'])
            locais_visitados.add(localizacao_atual)

    





    # Agora local_atual_info é um dicionário e você pode acessar 'descricao'
    

#           --- COMBATE ---
    if local_atual_info['inimigo']:
        inimigo_nome = local_atual_info['inimigo']

        # Acessa os atributos do inimigo usando o nome 
        atributos_inimigo = inimigo_atributos[inimigo_nome]

        # Criar objeto Inimigo com os atributos corretos
        inimigo_do_local = Personagem(
            nome=inimigo_nome,
            classe=atributos_inimigo['classe'],
            vida=atributos_inimigo['vida'],
            ataque=atributos_inimigo['ataque']
        )
        # --- Reaçao apos ver um inimigo ---
                                                                                              
       
        while True: 
            acão_personagem = input('Voce encontrou um inimigo! O que dezeja fazer?(lutar/escorder/analisar)') .lower().strip()
            if acão_personagem == 'lutar': 
                Batalha(heroi, inimigo_do_local)
                break
           
           

            elif acão_personagem == 'escorder':
                chance_de_acerto = random.random()
                animar_acao('Você tenta passar despercebidosim ')
                sleep(1)
                if chance_de_acerto >= 0.5:
                    print(f'Você conseguiu se esconder e {inimigo_do_local.nome} não te viu. Por enquanto, a sala está segura.')
                # Saia do loop de escolha, pois a ação foi bem-sucedida
                    break
                else:
                    print(f'Você falhou! {inimigo_do_local.nome} te viu e se prepara para lutar!')
                    Batalha(heroi, inimigo_do_local)
                    break
        
            elif acão_personagem == 'analisar':
                inimigo_do_local.status()
                

            else:
                print("Ação inválida. Tente novamente.")
                


        # VERIFICAÇÃO ADICIONADA AQUI!
        # Se o herói for derrotado na batalha, encerra o loop principal do jogo.
        if heroi.vida <= 0:
            break
    



    acao = input('Para onde você deseja ir? (ou "pegar [item]" ou "ver inventário") ').lower().strip()

    
    if acao in local_atual_info['saidas']:
        localizacao_atual = local_atual_info['saidas'][acao]
    
    elif acao == 'ver inventario':
        if inventario: # Se a lista não estiver vazia
            print("\nSeu inventário:")
            # fa um loop que passa nos itens do inventario 
            for item in inventario:
                print(f"- {item}")
        else:
            print("\nSeu inventário está vazio.")

    elif acao == 'pegar':
        item_para_pegar = acao.replace('pegar ', '')
        # verifica c o item existe
        if item_para_pegar in local_atual_info['itens']:
            # Adiciona o item ao inventario
            inventario.append(item_para_pegar)

            # Remove o item do local
            local_atual_info['itens'].remove(item_para_pegar)

            print(f'Você pegou {item_para_pegar} e guardou no inventario')
        else:
            print('Item não existente')

    
    else:
        print('Caminho não encontrado. Tente outra direção')

    # atualiza o local
    local_anterior = localizacao_atual
    




# ---- Batalha ---- 
'''print('\n--- Batalha Iniciada ---\n')
sleep(1)

turno = 1 
while heroi.vida > 0 and fulano.vida > 0:
    animar_acao(f"\n🔁 Turno {turno} iniciando")
    turno += 1

    # Ataque do Herói
    heroi.escolher_ataque(fulano)
    sleep(1)
    
    # Ataque do Inimigo
    fulano.ataque_aleatorio(heroi)
    sleep(1)
    
    # Checar se a batalha terminou
    if verificar_derrota(heroi, fulano):
        break

    # Status dos personagens após o turno
    print('\n📊 STATUS ATUAL:')
    heroi.status()
    print('---------------------')
    fulano.status()
    sleep(2)'''


