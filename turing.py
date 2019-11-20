#Kevin Macario 17369
#David Valenzuela 171001
#Carlos Chew 17507

#PROYECTO LOGICA MATEMATICA
#MAQUINA DE TURING

import re

file_list= ['MT1.txt', 'MT2.txt', 'MT3.txt', 'MT4.txt']
f = ''

def pprint(*args):
    string = '\n'.join(args)
    print(string)
    f.write('\n'+string)

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

def get_initial_state(tape1):
    match = re.search('^0+', tape1)
    return re.sub('^(0+)(?:1)', '', tape1), match.group(0)

def get_transitions(tape1):
    regex = '(0+)1(0+)1(0+)1(0+)1(0+)1'
    match = re.findall(regex, tape1)
    return match

def find_transition_fun(transitions, current_state, entry):
    for fun in transitions:
        if fun[0] == current_state and fun[1] == entry:
            return fun
    else:
        return None

def print_tapes(t1, t2, t3):
    pprint('Cinta 1:', t1)
    pprint('Cinta 2:', t2)
    pprint('Cinta 3:', t3)

def print_line():
    print('-'*50)

def entries_to_tape(entries, thead):
    str = ''
    for i in range(0, len(entries)):
        if i == thead:
            str += 'q'
        str += entries[i] + '1'
    return str

if __name__ == "__main__":
    #step 1
    for file in file_list:
        f = open(f'{file[:3]}-out.txt', 'a')
        mt1 = readTxt(file)[-1]
        if(is_valid_input(mt1)):
            pprint('Paso 1:')
            tape1 = mt1
            tape2 = 'UqU'
            tape3 = 'UqU'
            print_tapes(tape1, tape2, tape3)
            print_line()
            #Step 2
            pprint('Paso 2:')
            tapes = split_tape(mt1)
            tape1, tape2 = split_tape(mt1)
            print_tapes(tape1, tape2, tape3)
            print_line()
            #Step 3
            pprint('Paso 3:')
            tape1, tape3 = get_initial_state(tape1)
            print_tapes(tape1, tape2, tape3)
            #step 4 - n
            step = 4
            transitions = get_transitions(tape1)
            entries = get_entries(tape2)
            t2Head = 0
            print_line()
            while True:
                pprint(f'Paso {step}:')
                pprint(f'Busca la transicion con estados {tape3} y letra {entries[t2Head]} en la cinta 1')
                print_tapes(tape1, entries_to_tape(entries, t2Head), tape3)
                fun = find_transition_fun(transitions, tape3, entries[t2Head])
                if not fun:
                    pprint('Halt now')
                    break
                _, _, q, b, d = fun
                tape3 = q
                entries[t2Head] = b
                t2Head = t2Head + 1 if d == '000' else t2Head - 1 if d == '00' else t2Head
                print_tapes(tape1, entries_to_tape(entries, t2Head), tape3)
                print_line()
                if(q == '0' or q == '00'):
                    tape1 = '1'.join(entries)
                    tape2 = '1'.join(entries)
                    break
                else:
                    step += 1
                if step > 100:
                    break;
            print_tapes(tape1, tape2, tape3)
            f.close()

