'''Strobogrammatiska tal.

Ett exempel på en vanlig funktion som skriver ut strobogrammatiska tal.
Ett strobogrammatiskt tal är ett tal som ser likadant ut om man tittar på
det som vanligt eller upp och ner.
'''

def strobogrammatic(length):
    '''Vanlig funktion som beräknar strobogrammatiska tal.
    
    Funktionen arbetar sig från kanterna av talet (siffran längst till
    vänstra respektive siffran längst till höger) mot mitten till dess
    den utforskat alla tillåtna kombinationer.

    Argument:
        length    Antalet sökta siffror i det strobogrammatiska talet.

    Returnerar:
        En tom lista om length är 0 (noll).
        En lista med talen 0, 1 och 8 om length är 1.
        En lista med strobogrammatiska tal om length är större än 1.
    '''
    if length < 1:
        # Tom lista om strobogrammatiskt tal med för få antal siffror.
        return []

    elif length == 1:
        # Talen som kan finnas i mitten av ett strobogrammatiskt tal med udda
        # antal siffor.
        return [0, 1, 8]

    else:
        # Ta fram en lista med flersiffriga strobogrammatiska tal.
        result = []
        nbr = 10 ** (length-1)
        while nbr < 10 ** length:
            nbr_str = str(nbr)
            nbr_len = len(nbr_str)
            nbr_mid = nbr_len // 2
            is_strobogrammatic = True
            for i in range(nbr_mid):
                is_strobogrammatic = is_strobogrammatic and \
                       (nbr_str[i] == '1' and nbr_str[-i - 1] == '1' or \
                        nbr_str[i] == '8' and nbr_str[-i - 1] == '8' or \
                        nbr_str[i] == '6' and nbr_str[-i - 1] == '9' or \
                        nbr_str[i] == '9' and nbr_str[-i - 1] == '6')
                if not is_strobogrammatic:
                    break

            if is_strobogrammatic:
                if nbr_len % 2 == 0:
                    # Ett jämnt antal siffror i det strobogrammatiska talet så det
                    # finns ingen mittensiffra.
                    result.append(nbr)
                else:
                    # Ta fram den siffra som kan finnas i mitten av det
                    # strobogrammatiska talet.
                    if nbr_str[nbr_mid] == '0' or \
                       nbr_str[nbr_mid] == '1' or \
                       nbr_str[nbr_mid] == '8' :
                        result.append(nbr)

            if 1 < nbr < 6:
                nbr = 6
            elif nbr == 6:
                nbr = 8
            else:
                nbr += 1

        return result

def print_strobogrammatic_nbrs(length):
    '''Skriver ut strobogrammatiska tal i nummerordning.

    Argument:
        length    Antalet sökta siffror i det strobogrammatiska talet.
    '''
    if length > 5:
        print('Beräknar, var vänlig vänta...', flush=True)
    strobogrammatic_list = strobogrammatic(length)
    strobogrammatic_list.sort()
    for strobogrammatic_nbr in strobogrammatic_list:
        print(strobogrammatic_nbr)

if __name__ == '__main__':
    print_strobogrammatic_nbrs(int(input('Hur många siffror i talet? ')))
