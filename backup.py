import os
import shutil
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

ORIGEM = os.getenv("ORIGEM")
DESTINO = os.getenv("DESTINO")
INTERVALO_MINUTOS = int(os.getenv("INTERVALO_MINUTOS", 5))
LOGS_DIR = 'logs'

# Criar pasta de logs, se não existir
os.makedirs(LOGS_DIR, exist_ok=True)

def log(mensagem):
    """Registra mensagens no log com timestamp."""
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(LOGS_DIR, f"log_{agora}.txt")
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now()} - {mensagem}\n")

def realizar_backup():
    """Executa o backup dos arquivos da origem para o destino."""
    try:
        agora = datetime.now()
        data_str = agora.strftime("%Y-%m-%d_%H-%M-%S")
        destino_data = os.path.join(DESTINO, f'backup_{data_str}')
        os.makedirs(destino_data, exist_ok=True)

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

def job():
    """Tarefa agendada a ser executada."""
    log("Iniciando tarefa agendada...")
    realizar_backup()
    log("Tarefa agendada finalizada.")

if __name__ == '__main__':
    log(f"Agendamento configurado: a cada {INTERVALO_MINUTOS} minutos.")
    schedule.every(INTERVALO_MINUTOS).minutes.do(job)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        log("Execução interrompida manualmente.")
        print("\nExecução finalizada pelo usuário.")