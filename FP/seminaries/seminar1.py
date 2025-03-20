"""probleme laborator1"""


def problema1():
    numbers = []
    n = 100
    i = 2
    while i < n:
        isprim = True
        for d in range(2, i // 2):
            if i % 2 == 0:
                isprim = False
                break
        if isprim:
            numbers.append(i)
        i += 1
    for number in numbers:
        print(numbers)
    max = 0
    for i in range(len(numbers)):
        l = [i]
        n = 1
        for j in range(i + 1, len(numbers)):
            if numbers[i] <= numbers[j]:
                l.append(j)
        if n > max:
            max = n
            lm = l[:]
    print(lm)


# /seminar
def problema5():
    s = "abcdeac"
    ns = ""
    for c in s:
        # found = False
        # for x in ns:
        #     if c == x:
        #         found = True
        if c not in ns:
            ns += c
    print(ns)


problema5()
