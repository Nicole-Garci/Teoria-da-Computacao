from tape import TuringTape
from registers import Registers
from memory import Memory
from ula import ULA
from utils import to_binary


class MIPS:

    def __init__(self, instructions):

        self.instructions = instructions

        self.pc = 0

        self.tape = TuringTape()

        self.registers = Registers()

        self.memory = Memory()

        self.ULA = ULA()

    # =================================================

    def simulate_tape(self, content):

        self.tape.reset()

        print("\nEstado inicial:")
        print(self.tape.get_tape_with_head())

        for symbol in content:

            read_symbol = self.tape.read()

            print(f"\nLendo símbolo: {read_symbol}")

            self.tape.write(symbol)

            print(f"Escrevendo: {symbol}")

            print(self.tape.get_tape_with_head())

            self.tape.move_right()

            print("Movendo cabeça ->")

            print(self.tape.get_tape_with_head())

        print("\nEstado final da fita:")

        print(self.tape.get_tape())

    # =================================================

    def execute_add(self, rd, rs, rt):

        a = self.registers.read(rs)
        b = self.registers.read(rt)

        result = self.ULA.add(a, b)

        a_bin = to_binary(a)
        b_bin = to_binary(b)
        r_bin = to_binary(result)

        print("\nMemória de registradores:")

        print(f"Leitura: {rs}={a} ({a_bin})")
        print(f"Leitura: {rt}={b} ({b_bin})")

        expression = f"{a_bin}+{b_bin}={r_bin}"

        print("\nULA:")

        self.simulate_tape(expression)

        self.registers.write(rd, result)

        print("\nEscrita em registrador:")

        print(f"{rd} = {result} ({r_bin})")

    # =================================================

    def execute_sub(self, rd, rs, rt):

        a = self.registers.read(rs)
        b = self.registers.read(rt)

        result = self.ULA.sub(a, b)

        a_bin = to_binary(a)
        b_bin = to_binary(b)
        r_bin = to_binary(result)

        expression = f"{a_bin}-{b_bin}={r_bin}"

        print("\nULA:")

        self.simulate_tape(expression)

        self.registers.write(rd, result)

        print(f"\n{rd} = {result}")

    # =================================================

    def execute_and(self, rd, rs, rt):

        a = self.registers.read(rs)
        b = self.registers.read(rt)

        result = self.ULA.logical_and(a, b)

        expression = (
            f"{to_binary(a)}AND"
            f"{to_binary(b)}="
            f"{to_binary(result)}"
        )

        self.simulate_tape(expression)

        self.registers.write(rd, result)

    # =================================================

    def execute_or(self, rd, rs, rt):

        a = self.registers.read(rs)
        b = self.registers.read(rt)

        result = self.ULA.logical_or(a, b)

        expression = (
            f"{to_binary(a)}OR"
            f"{to_binary(b)}="
            f"{to_binary(result)}"
        )

        self.simulate_tape(expression)

        self.registers.write(rd, result)

    # =================================================

    def execute_mult(self, rd, rs, rt):

        a = self.registers.read(rs)
        b = self.registers.read(rt)

        result = self.ULA.multiply(a, b)

        expression = (
            f"{to_binary(a)}*"
            f"{to_binary(b)}="
            f"{to_binary(result)}"
        )

        self.simulate_tape(expression)

        self.registers.write(rd, result)

    # =================================================

    def execute_div(self, rd, rs, rt):

        a = self.registers.read(rs)
        b = self.registers.read(rt)

        result = self.ULA.divide(a, b)

        expression = (
            f"{to_binary(a)}/"
            f"{to_binary(b)}="
            f"{to_binary(result)}"
        )

        self.simulate_tape(expression)

        self.registers.write(rd, result)

    # =================================================

    def execute_lw(self, rd, address):

        print("\nMemória de dados:")

        print(f"Endereço solicitado: {address}")

        address_bin = to_binary(address)

        value = self.memory.load(address)

        value_bin = to_binary(value)

        # -----------------------------------------
        # SIMULA ACESSO À MEMÓRIA NA FITA
        # -----------------------------------------

        expression = (
            f"ADDR:{address_bin}"
            f"->DATA:{value_bin}"
        )

        print("\nFita da memória:")

        self.simulate_tape(expression)

        # -----------------------------------------
        # ESCREVE NO REGISTRADOR
        # -----------------------------------------

        self.registers.write(rd, value)

        print("\nBanco de registradores:")

        print(
            f"Escrita: "
            f"{rd} = {value} ({value_bin})"
        )

        # =================================================

    def execute_instruction(self, instruction, number):

        parts = instruction.split()

        op = parts[0].upper()

        print("\n================================================")
        print(f"Operação {number}")
        print("================================================")

        print("\nMemória de instruções:")

        print(
            instruction.replace(" ", "|") + "#"
        )

        # ---------------------------------------------

        if op == "ADD":

            self.execute_add(
                parts[1],
                parts[2],
                parts[3]
            )

        # ---------------------------------------------

        elif op == "SUB":

            self.execute_sub(
                parts[1],
                parts[2],
                parts[3]
            )

        # ---------------------------------------------

        elif op == "AND":

            self.execute_and(
                parts[1],
                parts[2],
                parts[3]
            )

        # ---------------------------------------------

        elif op == "OR":

            self.execute_or(
                parts[1],
                parts[2],
                parts[3]
            )

        # ---------------------------------------------

        elif op == "MULT":

            self.execute_mult(
                parts[1],
                parts[2],
                parts[3]
            )

        # ---------------------------------------------

        elif op == "DIV":

            self.execute_div(
                parts[1],
                parts[2],
                parts[3]
            )

        # ---------------------------------------------

        elif op == "LW":

            self.execute_lw(
                parts[1],
                int(parts[2])
            )

        # ---------------------------------------------

        else:

            print("\nInstrução não implementada.")

    # =================================================

    def run(self):

        instruction_number = 1

        while self.pc < len(self.instructions):

            instruction = self.instructions[self.pc]

            self.execute_instruction(
                instruction,
                instruction_number
            )

            self.pc += 1

            instruction_number += 1