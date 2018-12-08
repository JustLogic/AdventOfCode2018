#Example Input

#frequencies = [+1, -2, +3, +1]
#frequencies = [+1, +1, +1]
#frequencies = [+1, +1, -2]
frequencies = [-1, -2, -3]


def do_calc():
    finalFrequency = 0
    for frequency in frequencies:
         finalFrequency += frequency
    print(finalFrequency)
    return

do_calc()      