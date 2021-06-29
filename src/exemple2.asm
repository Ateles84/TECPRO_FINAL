EOR R0, R0
LAB1:
LDI R17, 65             ; la base del codi ASCII
ADD R17, R0
OUT 3, R17              ; escrivim caracter
SUBI R16, -1             ; iteracio
LDI R17, 26
SUB R17, R0
BRBC 1, LAB1
BREAK
