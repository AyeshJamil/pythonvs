# Swapping two variables using Typecasting
# initialize two variables
y = 4
z = 8.5

# Print before Swapping
print("Before Swapping:")
print(f"y = {y}, z = {z}")

# Swap variables using type casting 
y = str(y) # convert to string 
z = str(z) # convert to string

y, z = float(z), int(y) 

# Print after swapping
print(f"After swapping:")
print(f"y = {y}, z = {z}")