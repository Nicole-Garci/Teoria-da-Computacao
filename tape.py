class TuringTape:

    def __init__(self):

        self.tape = ["β"]
        self.head = 0

    # ---------------------------------------------

    def ensure_position(self):

        if self.head < 0:

            self.tape.insert(0, "β")
            self.head = 0

        elif self.head >= len(self.tape):

            self.tape.append("β")

    # ---------------------------------------------

    def read(self):

        self.ensure_position()

        return self.tape[self.head]

    # ---------------------------------------------

    def write(self, symbol):

        self.ensure_position()

        self.tape[self.head] = symbol

    # ---------------------------------------------

    def move_right(self):

        self.head += 1
        self.ensure_position()

    # ---------------------------------------------

    def move_left(self):

        self.head -= 1
        self.ensure_position()

    # ---------------------------------------------

    def reset(self):

        self.tape = ["β"]
        self.head = 0

    # ---------------------------------------------

    def get_tape(self):

        return "".join(self.tape)

    # ---------------------------------------------

    def get_tape_with_head(self):

        resultado = ""

        for i, c in enumerate(self.tape):

            if i == self.head:
                resultado += f"[{c}]"
            else:
                resultado += c

        return resultado