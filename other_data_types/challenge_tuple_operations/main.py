# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

banana_index = shelf.index("bananas")
print("First banana index:", banana_index)

if(apple_count < 5):
    print("Apples need to be restocked.")

else:
    print("Apples are sufficiently stocked.")

grape_count = shelf.count("grapes")
print(grape_count)
if(grape_count == 1):
    print("Grapes need to be restocked.")

else: 
    print("Grapes are sufficiently stocked.")

orange_count = shelf.count("oranges")
print(orange_count)
if(orange_count >=1):
    print("Oranges are at index:", orange_count)

else:
    print("Oranges are out of stock.")

if("oranges" in shelf):
    print("Oranges are at index:", orange_count)

else:
    print("Oranges are out of stock.")