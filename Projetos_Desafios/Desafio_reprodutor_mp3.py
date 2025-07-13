# Importa a biblioteca Pygame.
# Pygame é uma biblioteca popular para desenvolvimento de jogos em Python,
# e uma de suas funcionalidades é a manipulação de áudio (mixer).
import pygame

# Inicializa o módulo 'mixer' do Pygame.
# Isso é essencial para que as funções de áudio (como carregar e tocar música) funcionem.
pygame.mixer.init()

# Carrega o arquivo de música.
# Certifique-se de que o arquivo '07-Né.mp3' esteja na mesma pasta do seu script Python,
# ou forneça o caminho completo para o arquivo.
pygame.mixer.music.load('07-Né.mp3')

# Inicia a reprodução da música.
# A música começará a tocar em segundo plano.
pygame.mixer.music.play()

# Mantém o programa rodando e a música tocando até que o usuário pressione Enter.
# Sem essa linha, o programa terminaria imediatamente após iniciar a música, e você não a ouviria.
input('Pressione Enter para parar a música...')

# Para a reprodução da música.
pygame.mixer.music.stop()