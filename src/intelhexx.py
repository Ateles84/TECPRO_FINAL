from intelhex import IntelHex16bit

if __name__ == "__main__":
    a = IntelHex16bit()
    a.fromfile("exemple1.hex", format="hex")
    b = a.todict()
    print(b)
