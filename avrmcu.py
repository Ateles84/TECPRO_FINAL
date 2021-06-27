"""
Mòdul AvrMcu

"""
from repertoir import Repertoir
from state import State

class AvrMcu(object):
    """
    Classe AvrMcu

    """
    def __init__(self):
        """
        Mètode constructor

        """
        self._s
        self._rep

        a = State()
        b = Repertoir(self._rep)

    def reset(self):
        """
        Fa un reset de l’estat deixant-lo de la mateixa forma que el mètode init .

        """

    def set_prog(self , p):
        """
        p és una llista d’enters que representen un programa en llenguatge màquina de l’AVR.
        El mètode instal·la el programa p en la memòria de programa del simulador a partir de l’adreça 0000
        
        """

    def dump_reg(self):
        """
        String dels registres

        """

    def dump_dat(self):
        """
        String de la memòria de dades

        """

    def dump_prog(self):
        """
        String de la memòria de programa

        """

    def run(self):
        """
        Mètode principal.
        Fa iteracions infinites que:
        - Obté la instrucció del PC
        - Busca un Instrrunner que pugui execitar-la
        - Executa la instrucció
        Cal mirar les excepcions UnknownCodeError i BreakException

        """

    def set_trace(self , t):
        """
        Quan s’invova amb t=True activa el mode trace de la memòria de dades. Si s’activa amb t=False es desactiva el mode.

        """
