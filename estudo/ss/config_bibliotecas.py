from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By


navegador = opcoes.Chrome()

navegador.get('https://www.google.com/?hl=pt_BR')

# A linha abaixo vai pausar o script.
# O navegador só vai fechar quando você apertar Enter no terminal.
input('Pressione Enter para fechar o navegador...')