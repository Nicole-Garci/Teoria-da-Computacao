# Fita da Máquina de Turing.

# Responsável por: leitura, escrita, movimentação do "pivô"

class TuringTape:

    def __init__(self, tamanho=100):

        #inicializa a fita "preenchida" com vazio
        self.tape = ["β"] * tamanho

        self.head = 0


    def read(self):

        return self.tape[self.head]


    def write(self, simbolo):

        self.tape[self.head] = simbolo


    def move_right(self):

        self.head += 1


    def move_left(self):

        self.head -= 1


    def reset(self):

        self.tape = ["β"] * len(self.tape)

        self.head = 0


    def write_string(self, texto):

        for caractere in texto:

            self.write(caractere)

            self.move_right()


    def get_tape(self):

        #estado atual da fita
        return "".join(self.tape)