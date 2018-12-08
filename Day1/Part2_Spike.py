def main(inputValues):
    intialFrequency = 0
    calculatedFrequencies = []
    calculatedFrequencies.append(intialFrequency)

    inputFrequenciesChanges = inputValues

    do_calc(inputFrequenciesChanges, intialFrequency, calculatedFrequencies)



def do_calc(frequencyChanges, currentFrequency, calculatedFrequencies):
    iFoundTheSecondFrequency = False

    for frequency in frequencyChanges:
        currentFrequency += frequency
        if currentFrequency in calculatedFrequencies:
            iFoundTheSecondFrequency = True
            print("Found second frequency: ", currentFrequency)
            break
        else:
            calculatedFrequencies.append(currentFrequency)                
    
    if iFoundTheSecondFrequency == False:
        do_calc(frequencyChanges, currentFrequency, calculatedFrequencies)
    else:
        return


inputData1 = [+1, -2, +3, +1] #Answer 2
main(inputData1) 

inputData2 = [+1, -1] #Answer 0
main(inputData2) 

inputData3 = [+3, +3, +4, -2, -4] #Answer 10
main(inputData3) 

inputData4 = [-6, +3, +8, +5, -6] #Answer 5
main(inputData4) 

inputData5 = [+7, +7, -2, -7, -4] #Answer 14
main(inputData5) 