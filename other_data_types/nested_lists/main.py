# Creating an inventory
vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove(vegetables[2])
print(vegetables)
if("carrots" not in vegetables):
    vegetables.append("carrots")
print(vegetables)
vegetables.append("cucumbers")
print(vegetables)
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)
if("carrots" in vegetables):
    print("Carrots are already in the list")
if("cucumbers" in vegetables):
    print("Cucumbers are already in the list")