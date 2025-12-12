# -- coding: utf-8 --
import random
import string

try:
    import pyperclip  # Usado para copiar automaticamente a senha
except ImportError:
    pyperclip = None


def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True,
                usar_numeros=True, usar_especiais=True):
    """
    Gera uma senha aleatória com base nas preferências do usuário.
    """

    caracteres = ""

    if usar_maiusculas:
        caracteres += string.ascii_uppercase

    if usar_minusculas:
        caracteres += string.ascii_lowercase

    if usar_numeros:
        caracteres += string.digits

    if usar_especiais:
        caracteres += "!@#$%&*()-_=+/?"

    if not caracteres:
        raise ValueError("Nenhum grupo de caracteres foi selecionado!")

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def copiar_para_area_de_transferencia(texto):
    """
    Copia automaticamente a senha, caso o módulo pyperclip esteja instalado.
    """
    if pyperclip:
        pyperclip.copy(texto)
        print("📋 Senha copiada automaticamente para a área de transferência!")
    else:
        print("⚠ pyperclip não instalado. Instale com: pip install pyperclip")
        print("Senha *não* foi copiada automaticamente.")


def menu():
    print("\n===============================")
    print(" 🔐 GERADOR DE SENHAS FORTES ")
    print("===============================")

    try:
        tamanho = int(input("\nDigite o tamanho da senha (ex: 12): "))
    except ValueError:
        print("❌ Entrada inválida. Usando tamanho padrão: 12.")
        tamanho = 12

    usar_maiusculas = input("Usar letras MAIÚSCULAS? (s/n): ").lower() == "s"
    usar_minusculas = input("Usar letras minúsculas? (s/n): ").lower() == "s"
    usar_numeros = input("Usar números? (s/n): ").lower() == "s"
    usar_especiais = input("Usar caracteres especiais? (s/n): ").lower() == "s"

    senha = gerar_senha(
        tamanho=tamanho,
        usar_maiusculas=usar_maiusculas,
        usar_minusculas=usar_minusculas,
        usar_numeros=usar_numeros,
        usar_especiais=usar_especiais
    )

    print("\n🔑 SENHA GERADA:")
    print("----------------------------")
    print(senha)
    print("----------------------------")

    copiar_para_area_de_transferencia(senha)


if __name__ == "__main__":
    menu()
