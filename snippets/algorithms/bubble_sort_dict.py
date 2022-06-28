'''Bubble Sort Dictionary'''

def bubble_sort_dict(d, s=1):
    '''
    Performs bubble sort of a dictionary

    d : dictionary
        the dictionary to sort
    s : int
        how to sort; 0 for key, 1 for value
    '''
    t = list(d.items()) # Use temporary list t for the sorting
    for i in range(len(t)-1, 0, -1):
        for j in range(i):
            if t[j][s] > t[j+1][s]: # Sort for the key
                t[j], t[j+1] = t[j+1], t[j]
    # Could use 'return {k:v for k, v in t}' instead of the below.
    r = {}
    for k, v in t: # Build a sorted dictionary from list t
        r[k] = v
    return r

def main():
    '''Main function'''
    d = {'Spider':8, 'Fish':0, 'Human':2, 'Insect':6, 'Tripod':3}
    print('Osorterade lexikonet:', d)
    print('Sorterade lexikonet :', bubble_sort_dict(d))

if __name__ == '__main__':
    main()
