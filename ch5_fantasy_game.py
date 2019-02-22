inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

def displayInventory(inventory):
    total_items = 0
    text = 'Inventory:\n'
    if any(inventory) == False:
        print("There's nothing in the inventory!")
    else:
        for k, v in inventory.items():
            text += str(v) + ' ' + str(k) + "\n"
            total_items += v
        print(text + 'Total number of items: ' + str(total_items))


displayInventory(inventory)