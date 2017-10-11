Input = ""
annual_salary = 0
while annual_salary == 0:
    print ("Please enter your annual salery: ") #request user input
    Input = input() #input annual_salary
    try:
        annual_salary = float(Input) #check that the input is a number
    except:
        print ("Please enter the cost as a number.") #if the input isn't a number then give the user a polite error message
monthly_salary = annual_salary/12

portion_saved = 0.00
while portion_saved == 0: #input portion of salery to save
    print ("Please enter the portion of your salery to save as a decimal (ie: 0.1 for 10%): ") #request user input
    Input = input()
    try:
        portion_saved = float(Input) #check that input is a number, if it isn't then the input request message will repeat
    except:
        print("")
#no error message as the inout message should be clear enough

total_cost = 0.00
while total_cost == 0:
    print ("Please enter the total cost of your dream home: ") #request user input
    Input = input() #input total_cost
    try:
        total_cost = float(Input) #check that the input is a number
    except:
        print ("Please enter the cost as a number.") #if the input isn't a number then give the user a polite error message

portion_deposit = 0.20
current_savings = 0.00
annual_return = 0.04
r = annual_return #"Task 3: 4. Assume that you invest wisely, with an annual return of r"
months = 0
total_deposit = total_cost * portion_deposit

while current_savings < total_deposit: #every month:
    months += 1 #a month passes
    current_savings += current_savings * r / 12 #monthly return on investments
    current_savings += monthly_salary * portion_saved #savings from salary

print ("Number of months: " + str(months)) #output how many months passed
