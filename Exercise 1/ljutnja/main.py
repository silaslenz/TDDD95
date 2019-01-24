#  Author: Silas Lenz

def solve(M, N, children):
    missing = sum(children) - M
    anger = 0
    for child in range(len(children)):
        want = children[child]
        misses = min(want, round(missing/(N-child )))# Distribute the "bad luck" among all children equally
        missing-=misses
        anger += (misses*misses)
    return anger


if __name__ == '__main__':
    i = input()
    line = i.split()
    M = int(line[0])
    N = int(line[1])
    children = []
    for i in range(N):
        children.append(int(input()))

    # print(M, N, children)

    # print("Got:", M, "Need:", sum(children))
    children.sort()
    print(solve(M, N, children))