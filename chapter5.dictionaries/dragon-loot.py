stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


def addToInventory(inventory, addedItems):
    for i in addedItems:
        print(i)
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory


def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number pf items: ' + str(total))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)