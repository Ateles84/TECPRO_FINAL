class BitVector(object):
    """docstring for BitVector."""

    def __init__(self, w = 0):
        """
        >>> int(Byte(7))
        7
        >>> int(Byte(0b1011))
        11
        >>> int(Word(403))
        403
        """
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
        """
        >>> print(Byte(10))
        0A
        >>> print(Word(10))
        000A
        >>> print(Byte(1))
        01
        >>> print(Byte(15))
        0F
        >>> print(Byte(-1))
        FF
        >>> print(Byte(403))
        93
        """
        return str(hex(self._w)).replace("x", "").upper()

    def __add__(self, o):
        """
        Operador de suma del bitVector amb o (+)

        >>> Byte(2)+Byte(12)
        0E
        >>> Byte(12)+2
        0E
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

        >>> Byte(12)-Byte(2)
        0A
        >>> Byte(12)-2
        0A
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

        >>> Byte(8)&Byte(8)
        08
        >>> Byte(7)&Byte(0b0010)
        02
        >>> Byte(0xff)&Byte(0b1011)
        0B
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

        >>> Byte(24)|Byte(8)
        18
        >>> Byte(7)|Byte(0b0010)
        07
        >>> Byte(3)|Byte(4)
        07
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

        >>> Byte(24)^Byte(8)
        10
        >>> Byte(0xff)^Byte(0b1011)
        F4
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

        >>> ~Byte(24)
        E7
        >>> ~Byte(0xf0)
        0F
        >>> print(~Byte(0b101010))
        D5
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
        """
        >>> Byte(1)<<4
        10
        >>> Byte(0xfe)<<3
        F0
        """
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
        """
        >>> Byte(0xff)>>4
        0F
        """
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
        """
        >>> Byte(2)[0]
        False
        >>> Byte(2)[1]
        True
        >>> Byte(10)[7]
        False
        """
        if (i > -1 and i < len(str(bin(self._w))[2:])):
            return bool(int(bin(self._w)[2:][i]))
        else:
            raise KeyError("i is out of bounds (getitem)")

    def __setitem__(self, i, v):
        """
        >>> a=Byte(2)
        >>> a[1]=0
        >>> print(a)
        00
        >>> b=Byte(4)
        >>> b[0]=1
        >>> print(b)
        05
        """
        if (i > -1 and i < len(str(bin(self._w))[2:])):
            lel = str(bin(self._w))[2:]
            lel2 = lel[0:i] + str(v) + lel[i+1:]
            self._w = int(lel2,2)
        else:
            raise KeyError("i is out of bounds (getitem)")

class Byte(BitVector):
    """docstring for Byte.

    """
    def __len__(self):
        """
        >>> print(len(Byte(4)))
        8
        """
        return 8

    def concat(self, b):
        """
        retorna el Word resultant de concatenar self amb el Byte b. self es MSB i b el LSB
        >>> b=Byte(255)
        >>> c=Byte(0)
        >>> d=b.concat(c)
        >>> print(d)
        F0
        """
        conA = bin(self)[2:]
        while len(conA) < 8:
            conA = "0" + conA

        conB = bin(b)[2:]
        while len(conB) < 8:
            conB = "0" + conB

        #print("A: " + conA + " | " + conB)

        return Word(int(conA + conB, 2))

class Word(BitVector):
    """docstring for Word."""

    def __len__(self):
        """
        >>> print(len(Word(24)))
        16
        """
        return 16

    def lsb(self):
        """
        >>> Word(255).lsb()
        FF
        >>> Word(65535).lsb()
        FF
        """
        return int(str(bin(self._w))[2:][0])

    def msb(self):
        """
        >>> Word(255).msb()
        00
        >>> Word(65535).msb()
        FF
        """
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
