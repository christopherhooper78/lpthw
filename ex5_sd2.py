my_name = 'Zen A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

my_height_metric = round(my_height * 2.54)
my_weight_metric = round(my_weight * 0.453592)

print(f"{my_name}'s metric height is {my_height_metric} cms.")
print(f"{my_name}'s metric weight is {my_weight_metric} kgs.")
