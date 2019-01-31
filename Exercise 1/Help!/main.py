#  Author: Silas Lenz
import re

pattern_reg = re.compile("^<.*>$")


# print(pattern_reg.match("<a>"))

def replace_stuff(words, replacements):
    output = []
    for word in words:
        if word in replacements:
            output.append(replacements[word])
        else:
            output.append(word)
    return output


def match(line1, line2):
    again = True
    output1 = []
    output2 = []
    replacements1 = {}
    replacements2 = {}
    words1 = line1.split(" ")
    words2 = line2.split(" ")
    last_templates_left = -1
    while again:
        templates_left = 0
        if output1:
            words1 = output1
            words2 = output2
        again = False
        if (len(words1) != len(words2)):
            return "-", "-"
        for word1, word2 in zip(words1, words2):
            if pattern_reg.match(word1) and pattern_reg.match(word2):
                again = True
                templates_left += 1
            elif pattern_reg.match(word1):
                replacements1[word1] = word2
                templates_left += 1
            elif pattern_reg.match(word2):
                replacements2[word2] = word1
                templates_left += 1
            else:
                pass
        # print("replacement dicts",replacements1,replacements2)
        output1 = replace_stuff(words1, replacements1)
        output2 = replace_stuff(words2, replacements2)
        if last_templates_left == templates_left:
            # print(words1[0])
            for word in words1:
                if pattern_reg.match(word):
                    replacements1[word] = "bla"
                    break
            else:
                for word in words2:
                    if pattern_reg.match(word):
                        replacements2[word] = "bla"

            again = True
        last_templates_left = templates_left

    return output1, output2


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        line1 = input()
        line2 = input()
        replacements1 = {}
        replacements2 = {}
        out1, out2 = match(line1, line2)
        # print(out1,out2)
        if (out1 == out2):
            print(" ".join(out1))
        else:
            print("-")
