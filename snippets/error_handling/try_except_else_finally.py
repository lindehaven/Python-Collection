class MinusError(Exception):
    pass

try:
    a = 0
    b = input('Ange ett positivt heltal: ')
    c = int(b)
    if c < 0:
        raise MinusError
    elif c == 0:
        raise ZeroDivisionError

except MinusError:
    a = 'Negativt tal!'
except ZeroDivisionError:
    a = 'Division med noll!'
except ValueError:
    a = 'Inte ett heltal!'
except:
    a = 'Oväntat fel!'

else:
    a = 1/c

finally:
    print('a = 1 /', b, '=', a)
