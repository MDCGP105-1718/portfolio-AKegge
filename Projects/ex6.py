name = ""
age = 0
height = 0 #inches
weight = 0 #pounds
Eye_colour = ""
Hair_colour = ""
while name == "":
    print ("Please enter your name (then press enter): ")
    Input = input()
    if Input != "":
        name = Input
while age == 0:
    print ("Please enter your age:")
    Input = input()
    try:
        age = int(Input)
    except:
        print ("Please enter your age as a whole number")
if age <5 or age>150:
    print ("Really? Well if you say so...")
while height == 0:
    print ("Please enter your height in inches: ")
    Input = input()
    try:
        height = int(Input)
    except:
        print ("Please enter your height as a whole number of inches")
if height<30 or height>100:
    print ("Really? Well if you say so...")
while weight == 0:
    print ("Please enter your weight in pounds: ")
    Input = input()
    try:
        weight - int(Input)
    except:
        print ("Please enter your weight as a whole number of pounds")
if weight<50 or weight>500:
    print ("Really? Well if you say so...")
while Eye_colour == "":
    print ("Please enter your eye colour (then press enter): ")
    Input = input()
    if Input != "":
        Eye_colour = Input
while Hair_colour == "":
    print ("Please enter your hair colour (then press enter): ")
    Input = input()
    if Input != "":
        Hair_colour = Input
