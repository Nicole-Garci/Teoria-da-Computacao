class ULA:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def logical_and(self, a, b):
        return a & b

    def logical_or(self, a, b):
        return a | b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):

        if b == 0:
            return 0

        return a // b

    def slt(self, a, b):

        if a < b:
            return 1

        return 0

    def sll(self, a, shift):
        return a << shift

    def srl(self, a, shift):
        return a >> shift