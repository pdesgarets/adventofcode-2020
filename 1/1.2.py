import os

with open(os.getcwd() + '/input.txt') as f:
    lines = f.read().split('\n')
    found = {}
    for line in lines:
        current = int(line)
        for a in found.keys():
            if found[a].get(2020-current-a, False) is True:
                print(current)
                print(a)
                print(2020-a-current)
                print(current*a*(2020-a-current))
                exit()
            found[a][current] = True
        if found.get(current, False) is False:
            found[current] = {}
