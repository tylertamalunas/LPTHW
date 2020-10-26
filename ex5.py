name = 'Tyler Tamalunas'
age = 28
height = 72 # inches
weight = 215 # pounds
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

weight_kilograms = weight / 2.2 #kilograms
weight_kilograms = round(weight_kilograms)
cent_height = 2.54 * height #centimeters
print(f"My weight in kilograms is {weight_kilograms} kg.")
print(f"My height in centimeters is {cent_height} cm.")