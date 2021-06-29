"""
Mòdul State

"""
from memory import DataMemory
from memory import ProgramMemory
from memory import Memory
from bitvector import *


class State(object):
    """
    Classe State

    """

    def __init__(self , data = 128 , prog = 128):
        """
        Mètode constructor

        """
        d = DataMemory(data)      #Es el banc de memòria de dades de l’AVR
        self.data = d
        self.dataLL = d._m
        p = ProgramMemory(prog)   #Es el banc de memòria de programa de l’AVR.
        self.prog = p
        self.progLL = p._m
        self.pc =  Word(0)              #Un Word, Program Counter. El 2 es exemple
        self.flags = Byte(0)         #Un Byte, els flags carry(0), zero(1) i neg(2). El 123 es exemple

        #self.pc i self.flags per defecte els iniciem a 0
    def dump_dat(self):
        """
        Retorna un str que representa el bolcat de la memòria de dades.
        """
        #print(len(str(len(self.data))))
        for x,y in enumerate(self.dataLL):

            while len(str(x)) < len(str(len(self.dataLL))):
                x = "0" + str(x)

            print(str(x) + ": " + str(y))
        #print("passo")


    def dump_prog(self):
        """
        Retorna un str que representa el bolcat de la memòria de programa.
        """

        for x,y in enumerate(self.progLL):

            while len(str(x)) < len(str(len(self.progLL))):
                x = "0" + str(x)

            print(str(x) + ": " + str(y))

    def dump_reg(self):
        """
        Retorna un str que representa els registres continguts en l’estat. Això inclou també
        PC i flags. El format ha de ser similar a:
        R00: 00
        R01: 00
        ...
        R31: 00
        X(R27:R26): 0000
        Y(R29:R28): 0000
        Z(R31:R30): 0000
        PC: 0000
        CARRY: 0 ZERO: 0 NEG: 0

        """
        length = 32
        for x,y in enumerate(self.dataLL):
            if (x > 31):
                pass
            else:
                while len(str(x)) < 2:
                    x = "0" + str(x)

                while len(str(y)) < 8:
                    y = "0" + str(y)

                print("R" + str(x) + ": " + str(y)[-2:].upper())

        print("X(R" + str(length-5) + ":R" + str(length-6) + "): " + str(str(self.dataLL[-5])[-2:]) + str(str(self.dataLL[-6])[-2:]))
        print("Y(R" + str(length-3) + ":R" + str(length-4) + "): " + str(str(self.dataLL[-3])[-2:]) + str(str(self.dataLL[-4])[-2:]))
        print("Z(R" + str(length-1) + ":R" + str(length-2) + "): " + str(str(self.dataLL[-1])[-2:]) + str(str(self.dataLL[-2])[-2:])) #8 bits

        aux = bin(self.flags)[2:]
        while(len(aux) < 3):
            aux = "0" + str(aux)

        print("PC: " + str(self.pc))
        print("CARRY: " + aux[0] + " ZERO: " + aux[1] + " NEG: " + aux[2])


if __name__=='__main__':
    a = State(134)
    a.dump_prog()
    a.data.__setitem__(2, 42)
    print(a.data.__getitem__(2))
    #a.dump_dat()
