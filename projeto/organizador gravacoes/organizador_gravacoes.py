import os
import shutil
from datetime import datetime
import time


# Caminho da pasta onde os vídeos são salvos
PASTA_ORIGEM = r"C:\Users\briet\Videos"  # Altere aqui
PASTA_DESTINO = r"G:\videos"  # Altere aqui

# Lista pra guardar arquivos já processados
arquivos_processados = set()

def organizar_arquivos():
    for arquivo in os.listdir(PASTA_ORIGEM):
        if arquivo.endswith(".mkv") and arquivo not in arquivos_processados:
            caminho_arquivo = os.path.join(PASTA_ORIGEM, arquivo)

            # Obtem a data e hora atual
            agora = datetime.now()
            data_str = agora.strftime("%Y-%m-%d")
            hora_str = agora.strftime("%Hh%M")

            # Cria pasta de destino por data
            pasta_data = os.path.join(PASTA_DESTINO, data_str)
            os.makedirs(pasta_data, exist_ok=True)

            # Novo nome do arquivo
            novo_nome = f"valorant_{hora_str}.mkv"
            novo_caminho = os.path.join(pasta_data, novo_nome)

            # Move e renomeia
            shutil.move(caminho_arquivo, novo_caminho)
            arquivos_processados.add(arquivo)

            print(f"🎥 Arquivo movido para: {novo_caminho}")
            arquivos_processados.add(arquivo)

print("📂 Monitorando gravações... Pressione Ctrl+C para parar.")
try:
    while True:
        organizar_arquivos()
        time.sleep(5)  # verifica a cada 5 segundos
except KeyboardInterrupt:
    print("🛑 Monitoramento encerrado.")
