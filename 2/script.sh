#!/bin/bash
echo "Actualizando sistema..."
sudo apt update
echo "Instalando paquetes..."
sudo apt install -y git vim docker.io python3 python3-pip
echo "Proceso terminado"