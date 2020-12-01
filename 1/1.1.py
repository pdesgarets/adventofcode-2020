import os

with open(os.getcwd() + '/input.txt') as f:
    lines = f.read().split('\n')
    found = {}
    for line in lines:
        number = int(line)
        if found.get(number, False) is True:
            print(number)
            print(2020-number)
            print(number * (2020 - number))
            exit(0)
        found[2020-number] = True
