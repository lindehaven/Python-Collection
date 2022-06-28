'''Simple'''

def print_simple_table(n):
    '''Prints multiplication table to screen'''
    for c in range(1, 11):
        print(str(c*n).rjust(3), end='')
        if c < 10:
            print(end=',')

def main():
    '''Main application'''
    n = int(input("n? "))
    print_simple_table(n)

if __name__ == '__main__':
    main()
