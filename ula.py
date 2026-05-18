# ULA - Unidade Lógica e Aritmética.

class ALU:

    #adição
    def add(self, a, b):

        return a + b

    #subtração
    def sub(self, a, b):

        return a - b

    #multiplicação
    def multiply(self, a, b):

        return a * b

    #divisão (inteira não to lembrando se tem que ter tratamento decimal)
    def divide(self, a, b):

        if b == 0:
            return 0

        return a // b

    #"e" lógico (a ^ b)
    def logical_and(self, a, b):

        return a & b

    #"ou" lógico (a v b)
    def logical_or(self, a, b):

        return a | b

    #menor que (Set Less Than)
    def slt(self, a, b):

        if a < b:
            return 1

        return 0

    #shift para a esquerda
    def sll(self, a, shift):

        return a << shift

    #shift para a direita
    def srl(self, a, shift):

        return a >> shift