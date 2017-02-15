from random import *

def makeArray(x, y, mines):
    array = []
    allmines = []
    minecount = 1
    count = 0
    for n in range(x):
        plot = []
        for j in range(y):
            plot.append(n)
            plot.append(j)
            array.append(plot)
            plot = []
    while count < mines:
        mine = []
        mine.append(randint(0, x))
        mine.append(randint(0, y))
        if mine not in allmines:
            allmines.append(mine)
            minecount += 1
            count += 1

    print(makePTUI(x, y, array, allmines))

def makePTUI(x, y, array, mines):
    ptui = ""
    j = 0
    while j < y:
        n = 0
        while n < x:
            ptui += "□ "
            n += 1
        ptui += "\n\n"
        j += 1

    return ptui

def main():
    while True:
        x = int(input("Enter x value (10-25) : "))
        y = int(input("Enter y value(10-25) : "))
        mines = int(input("Enter mines: "))
        if mines <= (x*y):
            print()
            makeArray(x, y, mines)
        else:
            print("Too many mines")
            break

main()

