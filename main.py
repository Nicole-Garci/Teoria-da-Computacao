"""
Arquivo principal do simulador.
"""

import sys

from mips import MIPS


# =========================================================
# FUNÇÃO PRINCIPAL
# =========================================================

def main():

    # Verifica parâmetro da linha de comando
    if len(sys.argv) != 2:

        print("Uso:")
        print("python3 main.py NomeDoArquivo.txt")

        return

    arquivo = sys.argv[1]


    try:

        with open(arquivo, "r") as f:

            instrucoes = f.readlines()

    except:

        print("Erro ao abrir arquivo.")

        return


    cpu = MIPS()

    numero = 1 # n número da instrução

    for instrucao in instrucoes:

        instrucao = instrucao.strip()

        if instrucao != "":

            cpu.execute(instrucao, numero)

            numero += 1


# -----------------------------------------------------
if __name__ == "__main__":

    main()