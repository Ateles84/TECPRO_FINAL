class BitVector(object):
    """docstring for BitVector."""

    def __init__(self, w = 0):
        if (w > 255 and type(self) == Byte):
            aux = bin(w)[2:]
            while len(aux) < 16:
                aux = "0" + aux
            self._w = int(aux[8:16],2)

        else:
            self._w = w

    def __int__(self):
        return self._w

    def __index__(self):
        return self._w

    def __repr__(self):
        return str(hex(self._w)).replace("x", "").upper()

    def __add__(self, o):
        """
        Operador de suma del bitVector amb o (+)
        """
        operandA = 0
        operandB = 0

        if (len(str(bin(self._w))[2:]) == 8):
            aux = str(bin(self._w))[2:]
            print(aux)
            if (aux[0] == '1'):
                aux = aux[1:]
                aux2 = ""
                for i in aux:
                    if (i == "1"):
                        aux2 += "0"
                    else:
                        aux2 += "1"

                operandA = (int(aux2,2) + 1) * -1
        else:
            operandA = self._w

        if (len(str(bin(o))[2:]) == 8):
            aux = str(bin(o))[2:]
            if (aux[0] == '1'):
                aux = aux[1:]
                aux2 = ""
                for i in aux:
                    if (i == "1"):
                        aux2 += "0"
                    else:
                        aux2 += "1"
                    operandB = (int(aux2,2) + 1) * -1
        else:
            operandB = int(o)

        resultat = operandA + operandB
        if (resultat < 0):
            if (type(self) == Byte):
                return Byte(128 + (128 - resultat * -1))
            elif(type(self) == Word):
                return Word(128 + (128 - resultat * -1))
            else:
                return BitVector(128 + (128 - resultat * -1))

        else:
            if (type(self) == Byte):
                return Byte(resultat)
            elif(type(self) == Word):
                return Word(resultat)
            else:
                return BitVector(resultat)

    def __sub__(self, o):
        """
        Operador de suma del bitVector amb o (-)
        """
        operandA = 0
        operandB = 0

        if (len(str(bin(self._w))[2:]) == 8):
            aux = str(bin(self._w))[2:]
            print(aux)
            if (aux[0] == '1'):
                aux = aux[1:]
                aux2 = ""
                for i in aux:
                    if (i == "1"):
                        aux2 += "0"
                    else:
                        aux2 += "1"

                operandA = (int(aux2,2) + 1) * -1
        else:
            operandA = self._w

        if (len(str(bin(o))[2:]) == 8):
            aux = str(bin(o))[2:]
            if (aux[0] == '1'):
                aux = aux[1:]
                aux2 = ""
                for i in aux:
                    if (i == "1"):
                        aux2 += "0"
                    else:
                        aux2 += "1"
                    operandB = (int(aux2,2) + 1) * -1
        else:
            operandB = int(o)

        resultat = operandA - operandB
        if (resultat < 0):
             if (type(self) == Byte):
                 return Byte(128 + (128 - resultat * -1))
             elif(type(self) == Word):
                 return Word(128 + (128 - resultat * -1))
             else:
                 return BitVector(128 + (128 - resultat * -1))
        else:
            if (type(self) == Byte):
                return Byte(resultat)
            elif(type(self) == Word):
                return Word(resultat)
            else:
                return BitVector(resultat)

    def __and__(self, o):
        """
        Operador and del bitVector amb o (&)
        """
        if (type(self) == Byte):
            return Byte(int(self._w) & int(o))
        elif(type(self) == Word):
            return Word(int(self._w) & int(o))
        else:
            return BitVector(int(self._w) & int(o))

    def __or__(self, o):
        """
        Operador or del bitVector amb o (|)
        """
        if (type(self) == Byte):
            return Byte(int(self._w) | int(o))
        elif(type(self) == Word):
            return Word(int(self._w) | int(o))
        else:
            return BitVector(int(self._w) | int(o))

    def __xor__(self, o):
        """
        Operador xor del bitVector amb o (^)
        """
        if (type(self) == Byte):
            return Byte(int(self._w) ^ int(o))
        elif(type(self) == Word):
            return Word(int(self._w) ^ int(o))
        else:
            return BitVector(int(self._w) ^ int(o))

    def __invert__(self):
        """
        Operador not del bitVector (~)
        """
        selfVec = str(bin(self._w))[2:]
        #print("---" + selfVec)
        resultVec = ""

        for i in reversed(range(len(selfVec))):

            if (int(selfVec[i]) == 1):
                resultVec += "0"
            else:
                resultVec += "1"
            #

        if (type(self) == Byte):
            return Byte(int(resultVec[::-1], 2))
        elif(type(self) == Word):
            return Word(int(resultVec[::-1], 2))
        else:
            return BitVector(int(resultVec[::-1], 2))

    def __lshift__(self, i = 1):
        if (i < len(str(bin(self._w))[2:])):
            if (type(self) == Byte):
                return Byte(int(self._w) << i)
            elif(type(self) == Word):
                return Word(int(self._w) << i)
            else:
                return BitVector(int(self._w) << i)
        else:
            raise IndexError("i is out of bounds (lshift)")

    def __rshift__(self, i = 1):
        if (i < len(str(bin(self._w))[2:])):
            if (type(self) == Byte):
                return Byte(int(self._w) >> i)
            elif(type(self) == Word):
                return Word(int(self._w) >> i)
            else:
                return BitVector(int(self._w) >> i)
        else:
            raise IndexError("i is out of bounds (lshift)")

    def __getitem__(self, i):
        if (i > -1 and i < len(str(bin(self._w))[2:])):
            return bool(int(str(bin(self._w))[2:][i]))
        else:
            raise KeyError("i is out of bounds (getitem)")

    def __setitem__(self, i, v):
        if (i > -1 and i < len(str(bin(self._w))[2:])):
            lel = str(bin(self._w))[2:]
            lel2 = lel[0:i] + str(v) + lel[i+1:]
            self._w = int(lel2,2)
        else:
            raise KeyError("i is out of bounds (getitem)")

class Byte(BitVector):
    """docstring for Byte."""
    def __len__(self):
        return 8

    def concat(self, b):
        conA = bin(self)[2:]
        while len(conA) < 8:
            conA = "0" + conA

        conB = bin(b)[2:]
        while len(conB) < 8:
            conB = "0" + conB

        print("A: " + conA + " | " + conB)

        return Word(int(conA + conB, 2))

class Word(BitVector):
    """docstring for Word."""

    def __len__(self):
        return 16

    def lsb(self):
        return int(str(bin(self._w))[2:][0])

    def msb(self):
        if (len(str(bin(self._w))[2:]) < 15):
            return 0
        else:
            return int(str(bin(self._w))[2:][0])


if __name__ == "__main__":
    lel = Byte(42)
    lel2 = Byte(95)
    print(bin(lel) + "\n" + bin(lel2))

    #lel2 = (lel << 2)
    #print(int(lel2))
    #print(type(lel2))
