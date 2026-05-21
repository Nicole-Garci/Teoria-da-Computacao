import sys
from cpu import MIPS


def main():

    if len(sys.argv) != 2:

        print("Uso:")
        print("python3 main.py NomeDoArquivo.txt")
        return

    arquivo = sys.argv[1]

    try:

        with open(arquivo, "r") as f:
            instrucoes = [
                linha.strip()
                for linha in f.readlines()
                if linha.strip()
            ]

    except FileNotFoundError:

        print("Arquivo não encontrado.")
        return

    cpu = MIPS(instrucoes)

    cpu.run()


if __name__ == "__main__":
    main()