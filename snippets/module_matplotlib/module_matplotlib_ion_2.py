from matplotlib import pyplot as plt
 
plt.ion()
fig = plt.figure()
axis = fig.add_subplot(111)
 
for i in range(300):
    axis.plot(i,i,'o')
    plt.draw()
    if i > 5:
        plt.pause(0.01)   
input('Press the ENTER key to exit: ')
plt.close()
