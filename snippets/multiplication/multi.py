'''Multi'''

MAX_ROWS = 5
MIN_VALUE = 1
MAX_VALUE = 99

def convert_string_to_int(int_string):
    '''Converts string to integer'''
    i = -1
    try:
        i = int(int_string)
    except ValueError:
        i = -1
    return i

def get_value(out_string, min_value, max_value):
    '''Gets value in range from keyboard'''
    i = convert_string_to_int(input(out_string))
    while i < min_value or i > max_value:
        print("Ange värde %d-%d." % (min_value, max_value))
        i = convert_string_to_int(input(out_string))
    return i

def print_multi_table(m, n):
    '''Prints multiplication table to screen'''
    for r in range(m, n+1):
        for c in range(1, 11):
            print(str(r*c).rjust(3), end='')
            if c < 10:
                print(end=',')
        print()

def main():
    '''Main application'''
    m = get_value("m? ", MIN_VALUE, MAX_VALUE)
    n = get_value("n? ", m, MAX_VALUE)
    if (n - m) >= MAX_ROWS:
        n = m + MAX_ROWS - 1
    print_multi_table(m, n)

if __name__ == '__main__':
    main()
