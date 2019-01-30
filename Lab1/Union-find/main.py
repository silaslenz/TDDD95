#  Author: Silas Lenz

sets = {}


def merge(a, b):
    # in_a = sets[a]
    if not a in sets:
        sets[a] = {a}
    if not b in sets:
        sets[b] = {b}
    sets[a] = sets[a].union({b})
    sets[b] = sets[b].union({a})

    # a_location = -1
    # b_location = -1
    # for i in range(sets):
    #     set = sets[i]
    #     if a in set:
    #         # print("daskjdlk")
    #         a_location = i
    #     if b in set:
    #         b_location = i
    # # print("loaction", a_location, b_location)
    # sets[min(a_location,b_location)] = sets[a_location].union(sets[b_location])
    # # print(sets[a_location].union(sets[b_location]))
    # sets[max(a,b)] = min(a,b)
    # del sets[b_location]

def dfs(graph, start,b):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if b == vertex:
                return True
            stack.extend(graph[vertex] - visited)
            print(stack)
    return False

def is_in_same(a, b):
    if (a == b):
        print("yes")
        return True
    if not a in sets:
        print("no")
        return False


    if dfs(sets,a,b):
        print("yes")
        return True
    print("no")
    return False


if __name__ == '__main__':
    i = input()
    line = i.split()
    N = int(line[0])
    Q = int(line[1])
    sets = {}
    for i in range(Q):
        line = input().split()
        op = line[0]
        a = int(line[1])
        b = int(line[2])
        # print(line)
        print(sets)

        if (op == "="):
            merge(a, b)
            # print(sets)
        else:
            is_in_same(a, b)
        # print(sets)

