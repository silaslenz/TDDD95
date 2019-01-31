#  Author: Silas Lenz
from collections import defaultdict

sets = []

def root(a):
    if sets[a] != a:
        sets[a] = root(sets[a])
    return sets[a]

def merge(a, b):
    # in_a = sets[a]
    if a==b:
        return
    root_of_a = root(a)
    root_of_b = root(b)
    if (root_of_a == root_of_b):
        return
    if (root_of_a<root_of_b):
        sets[root_of_a] = root_of_b
    else:
        sets[root_of_b] = root_of_a


def is_in_same(a, b):
    return root(a)==root(b)


if __name__ == '__main__':
    i = input()
    line = i.split()
    N = int(line[0])
    Q = int(line[1])
    sets = [x for x in range(N)]
    for i in range(Q):
        line = input().split()
        op = line[0]
        a = int(line[1])
        b = int(line[2])
        # print(line)
        # print(sets)

        if (op == "="):
            merge(a, b)
            # print(sets)
        else:
            if is_in_same(a, b):
                print("yes")
            else:
                print("no")
        # print(sets)

