from random import randint
# Patrons - 1-3 weight
# Food - 1-5 w
# Knife - 10-20 w
# Pistols - 20-30 w
# Rifle - 50-70 w
# Map - 1-2 w
# Phone - 7-10 w
# Tent - 40-60 w
inventory = {'Patrons': (1, 3), 'Food': (1, 5), 'Knife': (10, 20), 'Pistol': (20, 30), 'Rifle': (50, 70), 'Map': (1, 2), 'Phone': (7, 10), 'Tent': (40, 60)}
mainInventory = {}
secInv = ['Patrons', 'Food', 'Knife', 'Pistol', 'Rifle', 'Map', 'Phone', 'Tent']
for i in range(100):
    name = secInv[randint(0, 7)]
    weightCort = inventory.get(name)
    weight = randint(weightCort[0], weightCort[1])
    mainInventory[name] = weight
print(mainInventory)

def deleteItem(name):
    mainInventory.pop(name)

def newItem(name, weight):
    mainInventory[name] = weight







