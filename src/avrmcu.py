"""
Mòdul AvrMcu

"""
from repertoir import Repertoir
from state import State
from instruction import *

class AvrMcu(object):
    """
    Classe AvrMcu

    """
    def __init__(self):
        """
        Mètode constructor

        """
        llistaInstruccions = [Add(), Adc(), Sub(), Subi(), And(), Or(), Eor(), Lsr(), Mov(), Ldi(), Sts(), Lds(), Rjmp(), Brbs(), Brbc(), Nop(), Out(), In(), Break()]
        self._s = State()
        self._rep = Repertoir(llistaInstruccions)

    def reset(self):
        """
        Fa un reset de l’estat deixant-lo de la mateixa forma que el mètode init .
        """
        self._s = State()

    def set_prog(self , p):
        """
        p és una llista d’enters que representen un programa en llenguatge màquina de l’AVR.
        El mètode instal·la el programa p en la memòria de programa del simulador a partir de l’adreça 0000
        """
        aux = Word(0)
        for i in p:
            self._s.prog.__setitem__(int(aux), i)
            aux += 1

    def dump_reg(self):
        """
        String dels registres
        """
        self._s.dump_reg()

    def dump_dat(self):
        """
        String de la memòria de dades
        """
        self._s.dump_dat()

    def dump_prog(self):
        """
        String de la memòria de programa
        """
        self._s.dump_prog()

    def run(self):
        """
        Mètode principal.
        Fa iteracions infinites que:
        - Obté la instrucció del PC
        - Busca un Instrrunner que pugui execitar-la
        - Executa la instrucció
        Cal mirar les excepcions UnknownCodeError i BreakException
        """
        for i in self._s.progLL:
            a = self._rep.find(i)
            a.execute(i, self._s)

    def set_trace(self , t):
        """
        Quan s’invova amb t=True activa el mode trace de la memòria de dades. Si s’activa amb t=False es desactiva el mode.
        """
        if (t):
            self._s.data.trace_on()
        else:
            self._s.data.trace_off()

if __name__=='__main__':
    a = AvrMcu()
    a.set_trace(True)
    #a.set_prog([58369, 57361, 3073, 47107, 24367])
    a.set_prog([61199, 57361, 3089, 11313, 8192])
    a.run()
    a.dump_reg()
    #a.dump_dat()
    #a.dump_prog()
