import pickle

po = ['En picklad fil med olika datatyper.', {'pi': 3.14159}, {'heavens': 7}]
pickle.dump(po, open('pickled_file.p', 'wb'))
pi = pickle.load(open('pickled_file.p', 'rb'))
if pi == po:
    print(pi)
else:
    print('Fel vid läsning av picklad fil!')