def hotel_cost(nights):
    return (nights * 70)
def plane_ticket_cost(city, flightClass):
    if(city=="New York"):
        return (2000 * flightClass)
    if(city=="Auckland"):
        return (790 * flightClass)
    if(city=="Venice"):
        return (154 * flightClass)
    if(city=="Glasgow"):
        return (65 * flightClass)
def rental_car_cost(days):
    cost = days * 30
    if(days > 7):
        cost -= 50
    elif(days > 3):
        cost -= 30
    return (cost)
def total_cost(city, flightClass, days):
    cost = hotel_cost(days - 1)
    cost += plane_ticket_cost(city, flightClass)
    cost += rental_car_cost(days)
    return (cost)

city = input("Please enter your destination: ")
days = int(input("Please enter how many days you will be staying there: "))
flightClass = int(input("Press 1 for economy class, 2 for premium economy, 3 for business class or 4 for first class: "))
if(flightClass == 2):
    flightClass = 1.3
if(flightClass == 3):
    flightClass = 1.6
if(flightClass == 4):
    flightClass = 1.9
totalCost = total_cost(city, flightClass, days)
print(f"Your trip will cost £{totalCost}.")
