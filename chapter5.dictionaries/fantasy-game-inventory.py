stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}


def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number pf items: ' + str(total))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    displayInventory(stuff)
