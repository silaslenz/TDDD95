#  Author: Silas Lenz


if __name__ == '__main__':
    N = int(input())
    for testcase in range(N):
        M = int(input())
        jumps = [int(jump) for jump in input().split()]

        alternatives = [[None] * 501]
        alternatives[0][0] = {"visited": "", "highest": 0}

        for jump in jumps:
            step = [None] * 501
            for i, alternative in enumerate(alternatives[-1]):
                if alternative:
                    # print(i, jump)
                    if (i + jump <= 500):
                        # print(alternative)
                        # print(alternative["highest"])
                        highest = max(i + jump, alternative["highest"])
                        action_list = alternative["visited"] + "U"
                        if step[i + jump]:
                            if step[i + jump]["highest"] > highest:
                                step[i + jump] = {"visited": action_list, "highest": highest}
                        else:
                            step[i + jump] = {"visited":action_list,"highest":highest}
                    if (i - jump >= 0):
                        highest = max(i - jump, alternative["highest"])
                        action_list = alternative["visited"] + "D"
                        if step[i - jump]:
                            if step[i - jump]["highest"] > highest:
                                step[i - jump] = {"visited": action_list, "highest": highest}
                        else:
                            step[i - jump] = {"visited": action_list, "highest": highest}
            # print(step)
            alternatives.append(step)
        if alternatives[-1][0]:
            print(alternatives[-1][0]["visited"])
        else:
            print("IMPOSSIBLE")
