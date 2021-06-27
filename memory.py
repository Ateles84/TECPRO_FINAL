"""
Mòdul Memory

"""

class Memory(object): #falta saber on va
    """
    Classe Memory

    """
    #llista de Word o Byte que representa el banc de memòria
    def __init__(self):
        """
        Mètode constructor

        """
        self._m = []
        self._trace = False

    def trace_on(self):
        """
        Activa la funcionalitat de trace

        """
        self._trace = True

    def trace_off(self):
        """
        Desactiva la funcionalitat de trace

        """
        self._trace = False

    def __len__(self):
        """
        Retorna el nombre de cel·les de la memòria

        """
        return len(self._m)

    def __repr__(self):
        """
        Retorna un str que conté un bolcat del banc de memòria en un format exactament com el que segueix (en el cas que les cel·les siguin Byte):
        0000: 00
        0001: 01

        """
        for x,y in enumerate(self._m):
            x = str(x)
            while len(x) < 4:
                x = "0" + x
            print(str(x) + ": " + str(hex(y[-2:])[2:].upper()))

    def dump(self, f = 0, t = 5):
        """
        Retorna un str que conté un bolcat del banc de memòria exactament com en el cas de __repr__ però únicament de les cel·les que estan en l’interval d’adreces [f, t).

        """
        #print(self._m)
        #print(len(self._m))
        for x,y in enumerate(self._m):
            if x >= f and x < t:
                x = str(x)
                while len(x) < 4:
                    x = "0" + x
                print(str(x) + ": " + str(hex(y[-2:])[2:].upper()))
            else:
                pass

    def __getitem__(self, addr):
        """
        Accés a memòria

        """
        if self._trace:
            try:
                print("Read " + str(hex(self._m[addr])[2:].upper()) + " from " + str(hex(addr)[2:].upper()))

            except OutOfMemError:
                raise OutOfMemError("Read from " + str(hex(addr)[2:].upper()) + " out of range")

        else:
            pass

        return int(self._m[addr])

    def __setitem__(self, addr, val):
        """
        Accés a memòria

        En cas que addr estigui fora de rang, aquestes operacions aixequen l’excepció OutOfMemError
        tot indicant com a missatge quelcom similar a "Read from 0005 out of range" o
        bé "Write to 0005 out of range" segons escaigui.

        """
        if self._trace:
            try:
                self._m[addr] = val
                print("Write " + str(hex(val)[2:].upper()) + " to " + str(hex(addr)[2:].upper()))

            except OutOfMemError:
                raise OutOfMemError("Write to " + str(hex(addr)[2:].upper()) +" out of range")


        else:
            self._m[addr] = val

class ProgramMemory(Memory):
    """
    Classe ProgramMemory

    """
    def __init__(self, ncells = 1024):
        """
        Inicialitza un banc de memòria d’amplada Word i ncells cel·les

        """
        a = Memory()
        self._m = a._m
        self._trace = a._trace
        #Amplada Word: 16 bits
        for x in range(ncells):
            a._m.append("0000000000000000") #16 bits

class DataMemory(Memory):
    """
    Classe DataMemory

    """
    #a = Memory()
    def __init__(self, ncells = 1024):
        """
        Inicialitza un banc de memòria d’amplada Byte i ncells cel·les. Si ncells és menor de 32, el banc serà de 32 cel·les

        """
        a = Memory()
        #print(a._m)
        self._m = a._m
        self._trace = a._trace
        #Amplada Byte: 8 bits
        if ncells < 32:
            truencells = 32
        else:
            truencells = ncells

        for x in range(truencells):
            a._m.append("00000000") #8 bits

        #print("Largada: " + str(len(a._m)))
        #print(a._m)

    def dump_reg(self):
        """
        Retorna un str que representa els registres continguts en el banc de memòria en un format com el següent:
        R00: 00
        R01: 00
        ...
        R31: 00
        X(R27:R26): 0000
        Y(R29:R28): 0000
        Z(R31:R30): 0000
        """
        lenght = len(a._m)
        #print(lenght)

        for x,y in enumerate(a._m):
            if (x > 31):
                pass
            else:
                while len(str(x)) < 2:
                    x = "0" + str(x)

                print("R" + str(x) + ": " + str(y))

        print("X(R" + str(lenght-5) + ":R" + str(lenght-6) + "): " + str(str(a._m[-5])[-2:]) + str(str(a._m[-6])[-2:]))
        print("Y(R" + str(lenght-3) + ":R" + str(lenght-4) + "): " + str(str(a._m[-3])[-2:]) + str(str(a._m[-4])[-2:]))
        print("Z(R" + str(lenght-1) + ":R" + str(lenght-2) + "): " + str(str(a._m[-1])[-2:]) + str(str(a._m[-2])[-2:])) #8 bits

if __name__=='__main__':
    a = DataMemory(45)
    #a.dump(0 , 33)
    a.dump_reg()
    a.trace_on()
    a.__setitem__(1 , 3)
    a.__setitem__(4 , 76)
    a.trace_off()
    a.__setitem__(34 , 8888)
    a.trace_on()
    a.__setitem__(21 , 2)
    a.__setitem__(19 , 87)
    a.dump_reg()
    print(a.__getitem__(4))
    #a.__getitem__(43)    Errors no definits encara
