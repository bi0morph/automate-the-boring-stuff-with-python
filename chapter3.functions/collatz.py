# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def collatz(number):
    result = number // 2
    if number % 2 == 1:
        result = 3 * number + 1
    print(result)
    return result


def main():
    print('Enter number:')
    try:
        number = int(input())
    except ValueError:
        print('You should enter a number')
    while number != 1:
        number = collatz(number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
