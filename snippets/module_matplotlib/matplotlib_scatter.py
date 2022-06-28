from matplotlib.pyplot import *    # importerar allt
x = ['A', 'B', 'C', 'D', 'E', 'F',
     'G', 'H', 'I', 'J', 'K', 'L'] # för kategoriaxel
y = [3, 5, 8, 5, 4, 2,
     2, 5, 7, 9, 8, 1]             # för kategorivärden
scatter(x, y, s=10)                # skapar punktdiagram
show()                             # visar punktdiagrammet
