import matplotlib.pyplot as plt

def initiate():
    '''Initiate the values for lists x and y for x and y axis'''
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [0,3,4,2,5,1,2,2,4,3]
    return x, y

def process(x,y):
    '''Process the lists x and y for x and y axis'''
    for i in range(len(y)-1):
        if y[i] > y[i+1]:
            y[i], y[i+1] = y[i+1], y[i]
    return x, y

plt.ion()
x, y = initiate()
for iteration in range(len(y)):
    plt.clf()
    plt.plot(x, y)
    plt.pause(0.5)
    x, y = process(x, y)

input('Press the ENTER key to exit: ')
plt.close()
