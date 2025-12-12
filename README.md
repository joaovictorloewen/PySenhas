# 🔐 Gerador de Senhas Fortes em Python
# 📌 Sobre o Projeto

Este projeto é um gerador de senhas fortes em Python, simples de usar e perfeito para incluir no seu portfólio (GitHub / LinkedIn).

Com ele, você pode:

Definir o tamanho da senha

Escolher se deseja incluir:

Letras maiúsculas

Letras minúsculas

Números

Caracteres especiais

Gerar senhas aleatórias e seguras

Copiar automaticamente a senha para a área de transferência (caso tenha o módulo pyperclip instalado)

# 🛠 Tecnologias Utilizadas

Python 3

Módulos padrão:

random

string

Módulo opcional:

pyperclip (para copiar a senha automaticamente)

# ▶ Como Usar
1. Clonar o repositório
git clone https://github.com/joaovictorloewen/PySenhas.git
cd gerador-senhas


Ajuste a URL acima para o nome do seu repositório real.

2. (Opcional) Criar ambiente virtual
python -m venv venv


Ativar:

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

3. Instalar dependência opcional
pip install pyperclip


O script funciona normalmente sem o pyperclip, apenas não copiará a senha automaticamente.

4. Executar o gerador
python generator.py

# 💻 Exemplo de Execução
===============================
 # 🔐 GERADOR DE SENHAS FORTES 
===============================

Digite o tamanho da senha (ex: 12): 16

Usar letras MAIÚSCULAS? (s/n): s

Usar letras minúsculas? (s/n): s

Usar números? (s/n): s

Usar caracteres especiais? (s/n): s

# 🔑 SENHA GERADA:
----------------------------
A1f$d92!GkF#vpQ0
----------------------------
# 📋 Senha copiada automaticamente para a área de transferência!

📎 Estrutura do Código
gerar_senha(...)

Responsável por montar a senha com base nas escolhas do usuário (tamanho e tipos de caracteres).

copiar_para_area_de_transferencia(texto)

Copia a senha automaticamente para o clipboard usando pyperclip, se disponível.

menu()

Interface interativa no terminal que guia o usuário.

if __name__ == "__main__":

Ponto de entrada do programa.
Chama a função menu().

# ⭐ Possíveis Melhorias Futuras

Interface gráfica com Tkinter

Barra de força da senha (Fraca / Média / Forte)

Opção de gerar múltiplas senhas de uma vez

Exportar senhas para um arquivo .txt

Versão web usando Flask ou FastAPI
