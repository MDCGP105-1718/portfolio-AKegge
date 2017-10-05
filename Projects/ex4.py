my_name = 'Aaron Kegge'
my_age = 19
my_height = 70 #inches
my_weight = 135 #pounds
my_eyes = 'Grey-Green'
my_hair = 'Brown'
is_heavy = my_weight > 3000
my_height_cm = my_height * 2.54 #convert my_height from inches to centimetres
my_height_m = my_height_cm / 100 #convert my_height to meters
my_weight_kg = round (my_weight / 2.2, 2) #convers my_weight from pounds to kilograms
my_height_ft = int(my_height / 12) #convert my_height to feet
my_height_in = my_height % 12 #and inches

print(f"Let's talk about {my_name}.")
print(f"He is {my_height_m} metres tall ({my_height_cm} centimetres), or {my_height_ft} feet and {my_height_in} inches tall ({my_height} inches total).")
print(f"He weighs {my_weight_kg} kilograms, or {my_weight} pounds.")
print(f"It is {is_heavy} that he is overweight.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")

total = my_age + my_height + my_weight
print (f"If I add {my_age}, {my_height} and {my_weight} I get {total}")
