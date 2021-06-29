"""
Mòdul Instruction

"""
from state import State
from bitvector import Word
from bitvector import Byte
import sys

class InstRunner(object):
    """
    Classe InstRunner

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "algo"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        if (True):
            return True

        else:
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """

        return "kekw"

class Add(InstRunner):
    """
    Classe Add

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "ADD"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "000011"):
            return True
        else:
            print("Returning: " + toCheck[:6])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """

        instr = int(instr,16)
        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]
                Ld = toCheck[6] + toCheck[12:16]

                valorRd = int(state.data.__getitem__(int(Rd,2)),16)
                valorLd = int(state.data.__getitem__(int(Ld,2)),16)

                resultat = Byte(valorRd) + Byte(valorLd)

                if (int(resultat) == 0): # comprovar resultat != 0
                    state.flags += 2
                elif (state.flags == 2 or state.flags == 3 or state.flags == 6 or state.flags == 7):
                    state.flags -= 2

                if (int(resultat) > 255): # comprovar carry
                    state.flags += 4
                    resultat -= 255
                elif (int(state.flags)  > 3):
                    state.flags -= 4

                if (int(resultat) > 128):#Comprovar negatiu
                    state.flags += 1
                elif (int(state.flags) % 2 != 0):
                    state.flags -= 1

                state.data.__setitem__(int(Rd,2), resultat)

        else:
            print("ERROR: WRONG OP_CODE FOR ADD")

        state.pc += 1

class Adc(InstRunner):
    """
    Classe Adc

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "ADC " + "R" + str(hex("registe on es guarda")) + " R" + str(hex("registe amb el qual es fa la suma"))

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "000111"):
            return True
        else:
            print("Returning: " + toCheck[:6])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]
                Ld = toCheck[6] + toCheck[12:16]

                valorRd = int(state.data.__getitem__(int(Rd,2)))
                valorLd = int(state.data.__getitem__(int(Ld,2)))

                carry = 0
                if (int(state.flags) > 3):
                    carry = 1
                    state.flags = Byte(int(state.flags) - 4)

                resultat = int(Byte(valorRd) + Byte(valorLd)) + carry
                if (resultat > 255):
                    resultat = resultat - 255
                    state.flags = Byte(int(state.flags) + 4)

                state.data.__setitem__(int(Rd,2), Byte(valorRd) + Byte(valorLd))

        else:
            print("ERROR: WRONG OP_CODE FOR ADC")
        state.pc += 1

class Sub(InstRunner):
    """
    Classe Sub

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "SUB"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "000110"):
            return True
        else:
            print("Returning: " + toCheck[:6])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]
                Ld = toCheck[6] + toCheck[12:16]

                valorRd = int(state.data.__getitem__(int(Rd,2)))
                valorLd = int(state.data.__getitem__(int(Ld,2)))

                resultat =  Byte(valorRd) - Byte(valorLd)

                if (int(resultat) == 0): # comprovar resultat != 0
                    state.flags += 2
                elif (state.flags == 2 or state.flags == 3 or state.flags == 6 or state.flags == 7):
                    state.flags -= 2

                if (int(resultat) > 255): # comprovar carry
                    state.flags += 4
                    resultat -= 255
                elif (int(state.flags)  > 3):
                    state.flags -= 4

                if (int(resultat) > 128):#Comprovar negatiu
                    state.flags += 1
                elif (int(state.flags) % 2 != 0):
                    state.flags -= 1

                state.data.__setitem__(int(Rd,2), resultat)



        else:
            print("ERROR: WRONG OP_CODE FOR SUB")

        state.pc += 1

class Subi(InstRunner):
    """
    Classe Subi

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "SUBI"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:4] == "0101"):
            return True
        else:
            print("Returning: " + toCheck[:4])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[8:12]
                Ld = toCheck[4:8] + toCheck[12:16]

                valorRd = int(state.data.__getitem__(int(Rd,2)))
                valorLd = int(Ld,2)
                print("toCheck: " + toCheck + " | valorRd: " + str(valorRd) + " | valorLd: " + str(Ld))

                resultat =  Byte(valorRd) - Byte(valorLd)

                if (int(resultat) == 0): # comprovar resultat != 0
                    state.flags += 2
                elif (state.flags == 2 or state.flags == 3 or state.flags == 6 or state.flags == 7):
                    state.flags -= 2

                if (int(resultat) > 128): # comprovar carry - Set if the absolute value of K is larger than the absolute value of Rd; cleared otherwise.
                    if (int(resultat) - 128 < valorLd):
                        state.flags += 4
                elif (int(state.flags)  > 3):
                    state.flags -= 4

                if (int(resultat) > 128):#Comprovar negatiu
                    state.flags += 1
                elif (int(state.flags) % 2 != 0):
                    state.flags -= 1

                state.data.__setitem__(int(Rd,2), resultat)

        else:
            print("ERROR: WRONG OP_CODE FOR SUBI")

        state.pc += 1

class And(InstRunner):
    """
    Classe And

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "AND"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "001000"):
            return True
        else:
            print("Returning: " + toCheck[:6])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]
                Ld = toCheck[6] + toCheck[12:16]

                valorRd = int(state.data.__getitem__(int(Rd,2)))
                valorLd = int(state.data.__getitem__(int(Ld,2)))

                resultat = Byte(valorRd) & Byte(valorLd)

                if (int(resultat) == 0): # comprovar resultat != 0
                    state.flags += 2
                elif (state.flags == 2 or state.flags == 3 or state.flags == 6 or state.flags == 7):
                    state.flags -= 2

                if (int(resultat) > 128):#Comprovar negatiu
                    state.flags += 1
                elif (int(state.flags) % 2 != 0):
                    state.flags -= 1

                state.data.__setitem__(int(Rd,2), resultat)

        else:
            print("ERROR: WRONG OP_CODE FOR AND")

        state.pc += 1

class Or(InstRunner):
    """
    Classe Or

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "OR"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "001010"):
            return True
        else:
            print("Returning: " + toCheck[:4])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]
                Ld = toCheck[6] + toCheck[12:16]

                valorRd = int(state.data.__getitem__(int(Rd,2)))
                valorLd = int(state.data.__getitem__(int(Ld,2)))

                resultat = Byte(valorRd) | Byte(valorLd)

                if (int(resultat) == 0): # comprovar resultat != 0
                    state.flags += 2
                elif (state.flags == 2 or state.flags == 3 or state.flags == 6 or state.flags == 7):
                    state.flags -= 2

                if (int(resultat) > 128):#Comprovar negatiu
                    state.flags += 1
                elif (int(state.flags) % 2 != 0):
                    state.flags -= 1

                state.data.__setitem__(int(Rd,2), resultat)

        else:
            print("ERROR: WRONG OP_CODE FOR OR")

        state.pc += 1

class Eor(InstRunner):
    """
    Classe Eor

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "EOR"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "001001"):
            return True
        else:
            print("Returning: " + toCheck[:6])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]
                Ld = toCheck[6] + toCheck[12:16]

                valorRd = int(state.data.__getitem__(int(Rd,2)))
                valorLd = int(state.data.__getitem__(int(Ld,2)))

                resultat = Byte(valorRd) ^ Byte(valorLd)

                if (int(resultat) == 0): # comprovar resultat != 0
                    state.flags += 2
                elif (state.flags == 2 or state.flags == 3 or state.flags == 6 or state.flags == 7):
                    state.flags -= 2

                if (int(resultat) > 128):#Comprovar negatiu
                    state.flags += 1
                elif (int(state.flags) % 2 != 0):
                    state.flags -= 1

                state.data.__setitem__(int(Rd,2), resultat)

        else:
            print("ERROR: WRONG OP_CODE FOR EOR")

        state.pc += 1

class Lsr(InstRunner):
    """
    Classe Lsr

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "LSR"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:7] == "1001010"):
            return True
        else:
            print("Returning: " + toCheck[:7])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]

                valorRd = int(state.data.__getitem__(int(Rd,2)))

                resultat = Byte(valorRd) >> 1

                if (str(bin(valorRd))[-1] == "1"):
                    state.flags += 4
                elif (state.flags > 3):
                    state.flags -= 4

                if (state.flags == 2 or state.flags == 3 or state.flags == 6 or state.flags == 7):
                    state.flags -= 2

                state.data.__setitem__(int(Rd,2), resultat)

        else:
            print("ERROR: WRONG OP_CODE FOR LSR")

        state.pc += 1

class Mov(InstRunner):
    """
    Classe Mov

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "MOV"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "001011"):
            return True
        else:
            print("Returning: " + toCheck[:6])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]
                Ld = toCheck[6] + toCheck[12:16]

                valorRd = int(state.data.__getitem__(int(Rd,2)))
                valorLd = int(state.data.__getitem__(int(Ld,2)))


                state.data.__setitem__(int(Rd,2), Byte(valorLd))

        else:
            print("ERROR: WRONG OP_CODE FOR MOV")

        state.pc += 1

class Ldi(InstRunner):
    """
    Classe Ldi

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "LDI"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:4] == "1110"):
            return True
        else:
            print("Returning: " + toCheck[:4])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = ""
                if (len(str(bin(instr))[2:]) <= 15):
                    aux = (str(bin(instr))[2:])
                    for i in range(16-len((str(bin(instr))[2:]))):
                        aux = "0" + aux
                    toCheck = aux
                else:
                    toCheck = str(bin(instr))[2:]

                Rd = toCheck[8:12]
                Ld = toCheck[4:8] + toCheck[12:16]

                valorLd = int(Ld,2)

                state.data.__setitem__(int(Rd,2), Byte(valorLd))

        else:
            print("ERROR: WRONG OP_CODE FOR LDI")
        state.pc += 1

class Sts(InstRunner):
    """
    Classe Sts

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "STS"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:7] == "1001001"):
            return True
        else:
            print("Returning: " + toCheck[:7])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]
                Ld = toCheck[16:32]

                valorRd = int(state.data.__getitem__(int(Rd,2)))

                state.data.__setitem__(int(Ld,2), Byte(valorRd))

                state.pc += 2

        else:
            print("ERROR: WRONG OP_CODE FOR STS")
            state.pc += 1

class Lds(InstRunner):
    """
    Classe Lds

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "LDS"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "001010"):
            return True
        else:
            print("Returning: " + toCheck[:4])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = str(bin(instr))[2:]

                Rd = toCheck[7:12]
                K = toCheck[16:32]

                valorK = int(state.data.__getitem__(int(K,2)))

                state.data.__setitem__(int(Rd,2), Byte(valorK))

                state.pc += 2

        else:
            print("ERROR: WRONG OP_CODE FOR STS")
            state.pc += 1

class Rjmp(InstRunner):
    """
    Classe Rjmp
    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "RJMP"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:4] == "1100"):
            return True
        else:
            print("Returning: " + toCheck[:4])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = str(bin(instr))[2:]

                value = int(toCheck[4:16],2)

                state.pc += value + 1

        else:
            print("ERROR: WRONG OP_CODE FOR RJMP")

class Brbs(InstRunner):
    """
    Classe Brbs

    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "BRBS"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "111100"):
            return True
        else:
            print("Returning: " + toCheck[:6])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = str(bin(instr))[2:]

                value = int(toCheck[7:13],2)
                sreg = int(toCheck[13:16],2)

                yey = False

                if (sreg == 0): #Estem mirant el carry
                    if (state.flags > 3):
                        yey = True
                elif (sreg == 1): #Estem mirant el Zero
                    if (int(state.flags) > 1 and int(state.flags) != 5):
                        yey = True
                elif (sreg == 2): #Estem mirant el negatiu
                    if (state.flags % 2 != 0):
                        yey = True

                if (yey):
                    state.pc += value + 1
                else:
                    state.pc += 1

        else:
            print("ERROR: WRONG OP_CODE FOR BRBS")

class Brbc(InstRunner):
    """
    Classe Brbc
    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "BRBC"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = ""
        if (len(str(bin(instr))[2:]) <= 15):
            aux = (str(bin(instr))[2:])
            for i in range(16-len((str(bin(instr))[2:]))):
                aux = "0" + aux
            toCheck = aux
        else:
            toCheck = str(bin(instr))[2:]

        if (toCheck[:6] == "111101"):
            return True
        else:
            print("Returning: " + toCheck[:6])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
                toCheck = str(bin(instr))[2:]

                value = int(toCheck[7:13],2)
                sreg = int(toCheck[13:16],2)

                yey = False

                if (sreg == 0): #Estem mirant el carry
                    if (state.flags < 3):
                        yey = True
                elif (sreg == 1): #Estem mirant el Zero
                    if (int(state.flags) != 2 and int(state.flags) != 3 and int(state.flags) != 6 and int(state.flags) != 7):
                        yey = True
                elif (sreg == 2): #Estem mirant el negatiu
                    if (state.flags % 2 == 0):
                        yey = True

                if (yey):
                    state.pc += value + 1
                else:
                    state.pc += 1
        else:
            print("ERROR: WRONG OP_CODE FOR BRBC")

class Nop(InstRunner):
    """
    Classe Nop
    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "NOP"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        if (int(instr) == 0):
            return True
        else:
            print("Returning: " + bin(instr))
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
            state.pc += 1
        else:
            print("ERROR: WRONG OP_CODE FOR NOP")

class Break(InstRunner): # BREAK: 38296
    """
    Classe Break
    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "IN"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        if (int(instr) == 38296):
            return True
        else:
            print("Returning: " + toCheck[:5])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
            sys.exit()

        else:
            print("ERROR: WRONG OP_CODE FOR BREAK")

class In(InstRunner): #aquesta es diferent
    """
    Classe In
    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "IN"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = str(bin(instr))[2:]

        if (toCheck[:5] == "10110"):
            return True
        else:
            print("Returning: " + toCheck[:5])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
            lel = input("IN (dec): ")

            Rd = str(bin(instr))[2:][6:11]

            print("Tot: " + bin(instr) + "\nTret: " + Rd)

            state.data.__setitem__(int(Rd,2), Byte(int(lel)))

        else:
            print("ERROR: WRONG OP_CODE FOR IN")

        state.pc += 1

class Out(InstRunner): #aquesta es diferent
    """
    Classe Out
    """
    def __repr__(self):
        """
        retorna una cadena que representa la instrucció
        """
        return "OUT"

    def match(self , instr):
        """
        instr és un Word i denota una instrucció. Retorna True si aquesta instància pot
        executar la instrucció instr.
        """
        toCheck = str(bin(instr))[2:]

        if (toCheck[:5] == "10111"):
            return True
        else:
            print("Returning: " + toCheck[:5])
            return False

    def execute(self , instr , state):
        """
        instr és un Word que denota una instrucció. state és una instància de la classe State. El mètode executa la instrucció i, com a resultat, modifica l’estat del microcontrolador al qual accedeix a través del paràmetre corresponent. Per poder executar la instrucció l’ha de descodificar, obtenir els operands (fetch), calcular el resultat, modificar convenientment el registre d’estat i emmagatzemar el resultat.
        """
        if not type(instr) == int:
            instr = int(instr,16)

        if (self.match(instr)):
            Rr = bin(instr)[2:][6:11]

            A = bin(instr)[2:][5:7] + bin(instr)[2:][11:16]

            Aux = ""
            if (int(A,2) == 0):
                Aux = int(state.data.__getitem__(int(Rr,2)), 16)
            elif (int(A,2) == 1):
                Aux = state.data.__getitem__(int(Rr,2))[2:].upper()
            else:
                Aux = state.data.__getitem__(int(Rr,2))[2:].encode()
                Aux = Aux.decode()
            print(Aux)

        else:
            print("ERROR: WRONG OP_CODE FOR OUT")

        state.pc += 1

if __name__=='__main__':
    print("prova ADD 2 registers")
    s=State()
    s.prog[0] = 0b0000110011010010
    #print(s.prog[0])
    s.data[0b01101] = 5
    s.data[0b00010] = 5
    a=Add()
    print(a.match(s.prog[0]))
    a.execute(s.prog[0],s)
    print(s.pc)
    print("Registre R13",s.data[13])
    print("Registre R2",s.data[2])
    s.data.trace_on()
    a.execute(s.prog[0],s)
    s.data.trace_off()
    print(s.pc)
    #s.dump_reg()


#Result
# prova ADD 2 registers
# True
# 0001
# registre R1 0A
# registre R2 05
# Read 0x05 from 0x02
# Read 0x0A from 0x01
# Write 0x0F to 0x01
# 0002
