#  Author: Silas Lenz

#  Author: Silas Lenz
import random

ops = ["=","?"]

N = 1000000
print(N)
for i in range(N):
    print(random.choice(ops),end=" ")
    print(random.choice(range(0, 1000)), end=" ")
    print(random.choice(range(0, 1000)))
