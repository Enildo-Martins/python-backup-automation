import os
import shutil
from datetime import datetime

# Caminhos
ORIGEM = r'C:\Users\User\Desktop\origem'       # Substitua com sua pasta de origem
DESTINO = r'C:\Users\User\Desktop\backup'      # Substitua com sua pasta de destino
LOGS_DIR = 'logs'

# Garante que a pasta de destino e logs existem
os.makedirs(DESTINO, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Data e hora atual para organização
agora = datetime.now()
data_str = agora.strftime("%Y-%m-%d_%H-%M-%S")
destino_data = os.path.join(DESTINO, f'backup_{data_str}')
os.makedirs(destino_data, exist_ok=True)

# Log
log_file = os.path.join(LOGS_DIR, f'log_{data_str}.txt')

def log(mensagem):
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now()} - {mensagem}\n")

def realizar_backup():
    try:
        arquivos = os.listdir(ORIGEM)
        log(f"Iniciando backup de {len(arquivos)} arquivos.")
        
        for arquivo in arquivos:
            origem_arquivo = os.path.join(ORIGEM, arquivo)
            destino_arquivo = os.path.join(destino_data, arquivo)

            if os.path.isfile(origem_arquivo):
                shutil.copy2(origem_arquivo, destino_arquivo)
                log(f"Copiado: {arquivo}")
        
        log("Backup finalizado com sucesso.")
    except Exception as e:
        log(f"Erro ao realizar backup: {str(e)}")

if __name__ == '__main__':
    realizar_backup()
