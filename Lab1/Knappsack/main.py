#  Author: Silas Lenz
import sys
from collections import namedtuple

Item = namedtuple("Item","index weight value")

#


def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for _ in
             range(len(items) + 1)]  # Column, number of items, row, weight of items

    for tablerow in range(1,len(items)+1):
        # print(tablerow)
        item = items[tablerow-1]
        for weight in range(1,limit+1):
            if item.weight > weight:
                table[tablerow][weight] = table[tablerow-1][weight]
            else:
                table[tablerow][weight] = max(table[tablerow -1][weight], table[tablerow-1][weight-item.weight]+item.value)
    print(table)

    #
    #
    # for j in range(1, len(items) + 1):
    #     item, wt, val = items[j - 1]
    #     for w in range(1, limit + 1):
    #         if wt > w:
    #             table[j][w] = table[j - 1][w]
    #         else:
    #             table[j][w] = max(table[j - 1][w],
    #                               table[j - 1][w - wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            item, wt, val = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result


if __name__ == '__main__':
    # i = input()
    for line in sys.stdin:
        items = []

        line = line.split()
        C = int(float(line[0]))
        n = int(line[1])
        # print("capacity:", C)
        for i in range(n):
            line = input().split()
            value = int(line[0])
            weight = int(line[1])
            items.append(Item(str(i), weight, value))
        # print(items)
        result = knapsack01_dp(items, C)
        print(len(result))
        for item in result:
            print(item[0], end=" ")
        print()
