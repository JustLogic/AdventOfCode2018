import os

#Get File Path
script_dir = os.path.dirname(__file__)
rel_path = "Day1_Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def is_int(value):
  try:
    int(value)
    return True
  except:
    print(value)
    return False

def main():
    intialFrequency = 0
    calculatedFrequencies = []
    calculatedFrequencies.append(intialFrequency)

    with open(abs_file_path) as f:  
      inputData = f.readlines()
    
    inputData = [x.strip() for x in inputData] 
    inputFrequenciesChanges = inputData

    do_calc(inputFrequenciesChanges, intialFrequency, calculatedFrequencies)



def do_calc(frequencyChanges, currentFrequency, calculatedFrequencies):
    iFoundTheSecondFrequency = False

    for frequency in frequencyChanges:
      if is_int(frequency):
        currentFrequency += int(frequency)
        if currentFrequency in calculatedFrequencies:
            iFoundTheSecondFrequency = True
            print("Found second frequency: ", currentFrequency)
            break
        else:
            calculatedFrequencies.append(currentFrequency)                
    
    if iFoundTheSecondFrequency == False:
        print("checking list again")
        print("Current Frequency: ", currentFrequency)
        print("Num items in CalculatedFrequencies: ", len(calculatedFrequencies))
        do_calc(frequencyChanges, currentFrequency, calculatedFrequencies)
    else:
        return

main()