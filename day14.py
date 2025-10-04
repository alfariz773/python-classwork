import random
import math


names = {name.strip() for name in input("Enter guest names (comma-separated): ").split(",")}
unique_names = list(names)

selected = random.choice(unique_names)

print("The reversed name is:", selected[::-1])

total = len(unique_names)
print("The total number of unique guests is:", total)

# Rounded square root
print("The rounded square root is:", round(math.sqrt(total)))


   
    
