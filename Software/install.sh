#!/bin/bash

# Verifique se o Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não está instalado. Instale-o para continuar."
    exit
fi

# Verifique se o pip está instalado
if ! command -v pip3 &> /dev/null
then
    echo "pip3 não está instalado. Instalando pip3..."
    sudo apt update
    sudo apt install python3-pip -y
fi

# Instalar dependências
echo "Instalando dependências..."
pip3 install -r requirements.txt

echo "Dependências instaladas com sucesso."

# Executar o programa
echo "Executando o programa..."
python3 software.py
