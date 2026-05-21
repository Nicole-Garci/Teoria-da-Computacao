class Memory:

    def __init__(self):

        self.memory = {

            0: 10,
            4: 20,
            8: 30,
            12: 40
        }

    # ---------------------------------------------

    def load(self, address):

        return self.memory.get(address, 0)

    # ---------------------------------------------

    def store(self, address, value):

        self.memory[address] = value