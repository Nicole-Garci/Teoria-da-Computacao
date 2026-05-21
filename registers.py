class Registers:

    def __init__(self):

        self.regs = {

            "$zero": 0,

            "$t0": 5,
            "$t1": 10,
            "$t2": 3,
            "$t3": 2,

            "$s0": 0,
            "$s1": 0,

            "$a0": 7,
            "$a1": 12,
            "$a2": 15,

            "$v0": 0,
            "$v1": 0
        }

    # ---------------------------------------------

    def read(self, reg):

        return self.regs.get(reg, 0)

    # ---------------------------------------------

    def write(self, reg, value):

        if reg != "$zero":
            self.regs[reg] = value

    # ---------------------------------------------

    def dump(self):

        for reg, value in self.regs.items():

            print(f"{reg}: {value}")