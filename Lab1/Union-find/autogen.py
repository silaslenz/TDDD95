#  Author: Silas Lenz
import random

ops = ["=","?"]

N = 1000000
print("1000000 1000000")
for i in range(N):
    print(random.choice(ops),end=" ")
    print(random.choice(range(0, 1000000)), end=" ")
    print(random.choice(range(0, 1000000)))