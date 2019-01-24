#  Author: Silas Lenz

number = int(input())

negative = 0
numbers = input().split()
for i in numbers:
    if int(i) < 0:
        negative += 1
print(negative)
