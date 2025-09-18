items= ["milk", "bread", "eggs"]
def add_item ():
    items.append("icecream")
    return items
print(add_item())
def remove_item ():
    items.pop()
    return items
print(remove_item())
item = lambda x : print("items:",x)
for x in items:
      item(x)
def sum_characters(items, index=0):
    if index == len(items):
        return 0
    return len(items[index]) + sum_characters(items, index + 1)
print(sum_characters(items))
        



     