spam = ['apples', 'bananas', 'tofu', 'cats']


def convertToString(list):
    string = ''
    for i in range(len(list)):
        if i == 0:
            string = list[i]
        elif i < (len(list) - 1):
            string += ', ' + list[i]
        else:
            string += ', and ' + list[i]
    return string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(convertToString(spam))
