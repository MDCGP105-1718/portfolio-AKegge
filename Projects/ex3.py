cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = 0                                     #assuming for now that there will be no cars not drinen
cars_driven = cars                                      #assuming for now that all cars will be drinen
drivers_not_in_cars = drivers                           #assuming for now that all drivers will be in cars
if cars > drivers:                                      #if there are more cars than drivers
    cars_not_driven = cars - drivers                    #the number of cars not driven will be equal to the number of cars - the number of drivers
    drivers_not_in_cars = 0                             #there will be no drivers who arn't in cars
    cars_driven = drivers                               #and the number of cars drinen will be equal to the number of drivers
else:                                                   #but if there are less cars than drivers
    cars_not_driven = 0                                 #there will be no cars not driven
    drivers_not_in_cars = dirvers - cars                #the number of drivers not in cars will be equal to the number of drivers - the number of cars
    cars_driven = cars                                  #and the number of cars driven will be equal to the number of cars

carpool_capacity = cars_driven * space_in_a_car         #the number of people who can be transported is equal to the number of cars being driven multiplied by the space in each car
average_passengers_per_car = passengers/cars_driven     #the average number of people in each car will be the number of passengers divided by the number of cars driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
