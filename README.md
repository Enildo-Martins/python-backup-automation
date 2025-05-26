# Python Backup Automation

Este projeto é um script simples em Python para **automação de backups locais**, com organização por data, tratamento de exceções e geração de logs. Ideal para tarefas cotidianas de manutenção de arquivos e aprendizado de automação com Python.

---

## Funcionalidades

- Copia todos os arquivos de uma pasta de origem para uma pasta de destino.
- Organiza os backups em subpastas com data e hora.
- Gera logs das operações realizadas.
- Trata erros durante o processo de backup.

---

## Requisitos
Python 3.10+

---

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/python-backup-automation.git
   cd python-backup-automation
   python -m venv venv
   .\venv\Scripts\activate  # Windows
## ou
    source venv/bin/activate  # Mac/Linux

## Instale as depedencias
    pip install -r requirements.txt

Copie o arquivo `.env.example` para `.env` e personalize conforme seu ambiente:
    copy .env.example .env  # Windows (cmd)

ou

    cp .env.example .env  # Linux/macOS

## Execute:
    python backup.py
