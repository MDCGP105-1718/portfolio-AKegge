semi_annual_raise = 0.07
annual_return_rate = 0.04
portion_deposit = 0.25
total_cost = 1000000
deposit = total_cost * portion_deposit
leeway = 100
annual_salary = 0
while annual_salary == 0:
    print ("Please enter your annual salery: ") #request user input
    Input = input() #input annual_salary
    try:
        annual_salary = float(Input) #check that the input is a number
    except:
        print ("Please enter the cost as a number.") #if the input isn't a number then give the user a polite error message
max_saving_rate = 10000
min_saving_rate = 0
optimal_saving_rate_achieved = False
steps = 0

saving_rate = int((max_saving_rate + min_saving_rate)/2)

while optimal_saving_rate_achieved == False:
    steps+=1
    current_savings = 0
    saving_rate = int((max_saving_rate + min_saving_rate)/2)
    months = 0
    monthly_salary = annual_salary / 12
    while current_savings < deposit:
        months+=1
        current_savings += current_savings * annual_return_rate / 12
        if(months % 6 == 0):
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
        current_savings += monthly_salary * (saving_rate / 1000)
        if months >= 36:
            break
    if (current_savings + leeway >= deposit and current_savings <= deposit + leeway) or (min_saving_rate == max_saving_rate):
        optimal_saving_rate_achieved = True
        print ("Best savings rate: " + str(saving_rate/1000))
        print ("Steps in bisection search: " + str(steps))
        break
    elif current_savings > deposit+leeway:
        max_saving_rate = int(saving_rate)
    elif current_savings + leeway < deposit and saving_rate < 10000:
        min_saving_rate = int(saving_rate)
    else:
        print ("It is not possible to pay the down payment in three years")
        break
