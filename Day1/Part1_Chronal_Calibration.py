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

def do_frequency_calibration():
    finalFrequency = 0

    with open(abs_file_path) as fp:  
        for cnt, frequency in enumerate(fp):
            if is_int(frequency):
                finalFrequency += int(frequency)
    
    print(finalFrequency)
    return

do_frequency_calibration()