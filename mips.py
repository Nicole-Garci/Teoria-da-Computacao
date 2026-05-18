# Processador MIPS simulado utilizando Máquina de Turing.

from tape import TuringTape
from registers import Registers
from memory import Memory
from ula import ALU

class MIPS:

    def __init__(self):

        self.tape = TuringTape()

        self.registers = Registers()

        self.memory = Memory()

        self.alu = ALU()

    
    # =====================================================
    # ESCRITA NA FITA (simular escrita na MT e retorna o estado atual da fita)
    # =====================================================
    def mostrar_fita(self, texto):

        self.tape.reset()

        self.tape.write_string(texto)

        return self.tape.get_tape()


    # =====================================================
    # EXECUÇÃO DAS INSTRUÇÕES (implementar)
    # =====================================================
    #provavelmente def execute(self, instrucao, numero):