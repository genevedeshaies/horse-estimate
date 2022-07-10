#Program to estimate your young horse's mature height

values = {"Current Height" : "", 
"Unit" : "",
"Current Age" : "",
}

def getValues():
    validHeight = False
    while not validHeight:
        height = input("What is your horse's current height at the withers? Please use cm, in or hh. ").split(sep=(" "))
        if len(height) == 1:
            try :
                float(height[0]),
            except:
                print("Please separate the measurement and the unit with a space.")
            else : 
                unit = input("Is this measurement in cm, in or hh? ")
                values["Unit"] = unit
                validHeight = True
                values["Current Height"] = height[0]
        else:
            values["Current Height"] = float(height[0])
            unit = height[1]
            values["Unit"] = unit
            validHeight = True
    validAge = False
    while not validAge:
        age = input("How old is your horse? Please enter age in months (mo). ")
        try:
            int(age)
        except:
            print("Please enter a valid number")
        else: 
            values["Current Age"] = int(age)
            validAge = True
    return values

print(f"Your horse's informations: {(getValues())}")

def predictHeight(height, unit, age):
    def convertUnit():
        if unit.lower() == "in":
            convertedHeight = height
        elif unit.lower() == "cm":
            convertedHeight = float(height) / 2.54
        elif unit.lower() == "hh":
            
            splitHeight = str(height).split(".")

            try:
                convertedHeight = (int(splitHeight[0])*4) + int(splitHeight[1])
            except:
                convertedHeight = height*4
        return convertedHeight

    def heightRange(lowFactor, highFactor, convertedHeight):
        lowHeight = int(((100*convertedHeight)/lowFactor))
        highHeight = int(((100*convertedHeight)/highFactor))
        return [lowHeight, highHeight]

    if age in range(1, 6):
        prediction ="Your foal is growing very fast, this calculator cannot evaluate its mature size at this age."
        if age in range (3, 6):
            print("At 3 months old, you can measure the length of its canon bone and multiply it by 4 to get an estimate.")
    elif age in range(6, 13):
        prediction = heightRange(75, 65, convertUnit())
    elif age in range(12, 19):
        prediction = heightRange(90, 75, convertUnit())
    elif age in range(18, 23):
        prediction = heightRange(90, 85, convertUnit())
    elif age in range(24, 31):
        prediction = heightRange(95, 90, convertUnit())
    elif age in range(30, 36):
        prediction = heightRange(97, 95, convertUnit())
    elif age in range (36, 61):
        prediction = [(int(convertUnit()+1)), (int(convertUnit()+2))]
    elif age > 60:
        prediction = "Your horse has probably finished growing by now."
    
    return prediction

def convertBack(lowHeight, highHeight):
            hhLow = f"{(lowHeight // 4)}.{(lowHeight % 4)}hh"
            hhMax = f"{(highHeight // 4)}.{(highHeight % 4)}hh"
            return f"Your horse should be about {hhLow} to {hhMax}."

prediction = predictHeight(values["Current Height"], values["Unit"], values["Current Age"])

try:
    print(convertBack(prediction[0], prediction[1]))
except:
    print(prediction)      


# print(predictHeight(values["Current Height"], values["Unit"], values["Current Age"]))
