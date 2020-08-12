
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def draw(nestedGrid):
    for x in range(len(nestedGrid[0])):
        for y in range(len(nestedGrid)):
            print(nestedGrid[y][x], sep='', end='')
            # for x in range(len(nestedGrid[y])):
        print('', sep='', end='\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    draw(grid)
