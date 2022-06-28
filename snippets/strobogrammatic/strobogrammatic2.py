'''Strobogrammatiska tal.

Ett exempel på en rekursiv funktion som skriver ut strobogrammatiska tal.
Ett strobogrammatiskt tal är ett tal som ser likadant ut om man tittar på
det som vanligt eller upp och ner.
'''

def strobogrammatic(current, length):
    '''Rekursiv funktion som beräknar strobogrammatiska tal.

    Funktionen arbetar sig rekursivt från kanterna av talet (siffran längst
    till vänstra respektive siffran längst till höger) mot mitten till dess
    den utforskat alla tillåtna kombinationer.

    Argument:
        current   Nuvarande antal siffror i talet.
        length    Antalet sökta siffror i det strobogrammatiska talet.

    Returnerar:
        En tom lista om current är 0 (noll).
        En lista med talen 0, 1 och 8 om current är 1.
        En lista med strobogrammatiska tal om current är större än 1.
    '''
    if current == 0:
        # Tom lista om strobogrammatiskt tal med jämnt antal siffror. Detta
        # avslutar ett rekursivt anrop till denna funktion.
        return ['']

    elif current == 1:
        # Talen som kan finnas i mitten av ett strobogrammatiskt tal med udda
        # antal siffor. Detta avslutar ett rekursivt anrop till denna funktion.
        return ['0', '1', '8']

    else:
        # Ta fram de tal som kan finnas i mitten av det strobogrammatiska talet.
        # Anropet är rekursivt vilket betyder att denna funktion anropar sig
        # själv till dess den funnit mitten av det strobogrammatiska talet.
        middle_number_list = strobogrammatic(current - 2, length)
        result = []
        for middle_number in middle_number_list:
            if current != length:
                # Detta villkor finns för att det strobogrammatiska talet inte
                # får börja med en onödig nolla, t ex 0110 eller 06890.
                # Det strobogrammatiska talet får dock vara en enda nolla.
                result.append('0' + middle_number + '0')
            result.append('8' + middle_number + '8')
            result.append('1' + middle_number + '1')
            result.append('9' + middle_number + '6')
            result.append('6' + middle_number + '9')
        return result

def print_strobogrammatic_numbers(length):
    '''Skriver ut strobogrammatiska tal i nummerordning.

    Argument:
        length    Antalet sökta siffror i det strobogrammatiska talet.
    '''
    strobogrammatic_list = strobogrammatic(length, length)
    strobogrammatic_list.sort()
    for strobogrammatic_number in strobogrammatic_list:
        print(strobogrammatic_number)

if __name__ == '__main__':
    print_strobogrammatic_numbers(int(input('Hur många siffror i talet? ')))
