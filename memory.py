# Memória de dados (LW) leitura na memória

class Memory:

    def __init__(self):

        self.memory = {

            0: 100,
            4: 200,
            8: 300,
            12: 400
        }


    def load(self, endereco):

        return self.memory.get(endereco, 0)