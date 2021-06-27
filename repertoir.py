"""
Mòdul Repertoir

"""

from instruction import InstRunner

class Repertoir(object):
    """
    Classe Repertoir

    """
    def __init__(self , li):
        """
        Mètode constructor

        """
        self._li = li

    def find(self , instr):
        """
        instr és un Word que denota una instrucció. El mètode retorna un objecte InstRunner capaç d’executar la instrucció instr. En cas que no existeixi cap InstRunner capaç d’executar la instrucció, aixeca l’excepció UnknownCodeError.
        """
