#Kevin Macario 17369
#David Valenzuela
#Carlos Chew

#PROYECTO LOGICA MATEMATICA
#MAQUINA DE TURING

import re


mt1 = '00010001010000101000110000100010000100010001100001001000001000100110000101000001010011000001000100000100010011000001010101011100010001001000101'


def is_valid_input(Tu):
    """
    params:
        - Tu: cadena e(T)e(z)
    returns: true if input is valid, false otherwise
    """
    regex = '^0001(?:(?:(?:0{1,5})1(?:0{1,3})1(?:0{1,5})1(?:0{1,3})1(?:0{0,3})1)1)+1(?:0{1,3}1)+$'
    match = re.search(regex, Tu)
    return match != None

def split_tape(Tu):
    """
    params:
        - Tu: cadena e(T)e(z)
    returns: tuple(tape1, tape2)
    """
    reT = '^0001(?:(?:(?:0{1,5})1(?:0{1,3})1(?:0{1,5})1(?:0{1,3})1(?:0{0,3})1)1)+'
    reZ = '1(?:0{1,3}1)+$'
    matchET = re.search(reT, Tu)
    matchEZ = re.search(reZ, Tu)
    return (matchET.group(0), '0'+matchEZ.group(0))

def readTxt(name):
    cadena = []
    with open (name, 'rt') as myfile:
        for myline in myfile:
            length = len(myline)
            myline1 = myline[:length -1]
            myline1.split("\n")
            cadena.append(myline1)
        return cadena

if __name__ == "__main__":
    if(is_valid_input(mt1)):
        tapes = split_tape(mt1)
        print(tapes)
