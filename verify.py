#Kevin Macario 17369
#David Valenzuela 171001
#Carlos Chew 17507

#PROYECTO LOGICA MATEMATICA
#MAQUINA DE TURING

import re


mt1 = '00010001010000101000110000100010000100010001100001001000001000100110000101000001010011000001000100000100010011000001010101011100010001001000101'

class sigma(object):

    def __init__():
        """
        """

def is_valid_input(Tu):
    """
    params:
        - Tu: cadena e(T)e(z)
    returns: true if input is valid, false otherwise
    """
    regex = '^(?:0+)1(?:(?:(?:0+)1(?:0+)1(?:0+)1(?:0+)1(?:0+)1)1)+1(?:0+1)+$'
    match = re.search(regex, Tu)
    return match != None

#Step 1
def split_tape(Tu):
    """
    params:
        - Tu: cadena e(T)e(z)
    returns: tuple(tape1, tape2)
    """
    reT = '^(?:0+)1(?:(?:(?:0+)1(?:0+)1(?:0+)1(?:0+)1(?:0+)1)1)+'
    reZ = '1(?:0+1)+$'
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

def get_entries(tape2):
    """
    params:
        -tape2: Tape No 2 with entry string
        -returns: List with the inputs
    """
    regex = '(?:^01)(.*)(?:1)'
    match = re.search(regex, tape2)
    return match.group(0).split('1')

def print_tapes(t1, t2, t3):
    print('tape 1:\n', t1)
    print('tape 2:\n', t2)
    print('tape 3:\n', t3)

def print_line():
    print('-'*50)
    

if __name__ == "__main__":
    #step 1
    if(is_valid_input(mt1)):
        print('Step 1:')
        tape1 = mt1
        tape2 = 'UqU'
        tape3 = 'UqU'
        print_tapes(tape1, tape2, tape3)
        print_line()
        #Step 2
        print('Step 2:')
        tapes = split_tape(mt1)
        tape1, tape2 = split_tape(mt1)
        print_tapes(tape1, tape2, tape3)

