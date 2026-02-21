#LET'S START DEFINING THE FORMULAS TO CALCULATE THE BMI BOTH IN THE INTERNATIONAL SYSTEM AND THE IMPERIAL SYSTEM
def bmiInt(weight, height):
    return (weight / (height / 100)**2)

def bmiEng(weight, heightFoot, heightInch):
    height_total = (heightFoot * 12 + heightInch)
    return (weight / (height_total**2)) * 703

#NOW, LET'S USE A BUCLE WHILE TO GIVE THE OPTION TO CALCULATE THE BMI WITH THE INTERNATIONAL SYSTEM OR THE IMPERIAL SYSTEM
def BucleBMICalculator():
    while True:
        try:
            measure = int(input('Enter "1" and press the key "ENTER" if you want to calculate your BMI use the International System of Units\nEnter "2" and press the key "ENTER" if you want to calculate your BMI using the Imperial System: '))
            if measure == 1:
                try:
                    weight = float(input('Enter your weight in kilos:'))
                    height = float(input('Enter your height in centimetres:'))
                    return measure, weight, height, None, None #<-- THIS WAY, WE CAN USE THE DATA ON THESE VALUES OUTSIDE THE WHILE BUCLE
                except ValueError:
                    print('Please, enter a valid number.')

            elif measure == 2:
                try:
                    weight = float(input('Please, enter your weight in POUNDS:'))
                    heightFoot = float(input('Please, first enter your height in FEET and press "ENTER":'))
                    heightInch = float(input('Please, now enter your height in INCHES and press "ENTER":'))
                    return measure, weight, None, heightFoot, heightInch
                except ValueError:
                    print('Please, enter a valid number.')
                
            else:
               print('Please, enter only "1" or "2", and then press "ENTER"')
        except ValueError:
                print('Please, enter only "1" or "2", and then press "ENTER"')

def Calculate_BMI(): #CREATING A FUNCTION TO USE THE DATE REGISTERED IN THE PREVIOUS BUCLE, AS WELL AS USING THOSE DATA
    measure, weight, height, heightFoot, heightInch = BucleBMICalculator() #<-- DECLARING THIS, IT LET US USE THE DATA OBTAINED INSIDE THE PREVIOUS BUCLE

#NOW LET'S USE AN 'IF' CONDITION TO PRINT THE RESULT DEPENDING IF WE USED THE INTERNATIONAL OR THE IMPERIAL SYSTEM
    if measure == 1:
        result = bmiInt(weight, height)
        print('Your BMI is:', (result))
    if measure == 2:
        result = bmiEng(weight, heightFoot, heightInch)
        print('Your BMI is:', (result))

#AND HERE WE PRINT THE MEANING OF THE SCORE
    if result < 18.5:
        print('Your BMI is Underweight')
    elif result < 24.9:
        print('Your BMI is Normal')
    elif result < 29.9:
        print('Your BMI is Overweight')
    else:
        print('Your BMI is Obese')

#NOW, LET'S CREATE ANOTHER ONE BUCLE TO LET THE USER USING AGAIN THIS PROGRAM WITHOUT LOADING AGAIN THE PROGRAM
def Lastbucle():
    print('Would you like to calculate another BMI?')
    while True:
        Another_calc = str(input('Press "y" and ""ENTER"" to calculate another BMI\nPress "n" and "ENTER" to exit the program.')).lower()
    
        if Another_calc == "y":
            print('Let´s calculate another BMI!')
            Calculate_BMI() #<-- WITH THIS, WE CALL AGAIN THE PREVIOUS BUCLE TO CALCULATE THE BMI
        elif Another_calc == "n":
            print('Thanks for using my program.')
            break
        else: #IN CASE THE USE PRESS A DIFFERENT KEY THAN 'y' OR 'n', THIS BUCLE STARTS AGAIN.
            print('Please, enter "y" to make another BMI calculation, or "n" to exit the program.')

Calculate_BMI() #<-- THIS LET'S THE PROGRAM TO START AND TO CALL THE BUCLE THAT ASKS FOR THE BMI DATA AND USE THOSE DATA TO CALCULATE THE BMI
Lastbucle() #<-- THIS CALLS A BUCLE TO ASK IF THE USER WANTS TO CALCULATE ANOTHER BMI OR FINISH THE PROGRAM
