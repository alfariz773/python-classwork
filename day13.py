  
item = input("Enter the name of the new item: ")

with open("items.txt", "a") as f:   
    f.write(item + "\n")

print("\nCurrent List of Items:")
with open("items.txt", "r") as f:
    print(f.read())
