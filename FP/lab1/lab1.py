# 08.10.2024
# a. a. Zerlege eine gegebene natürliche Zahl in ihren Primfaktoren.
# b. Bei einem gegebenen Zahlenvektor finde die längste aufeinanderfolgende Teilfolge wobei aufeinanderfolgenden Elemente dieselben Ziffern enthalten.
def ub_a():
    n = int(input("Geben Sie eine naturliche Zahl ein:"))
    d = 2
    while n > 1:
        if n % d == 0:
            p = 0
            while n % d == 0:
                p += 1
                n //= d
            print(d)
        d += 1
        if n > 1 and d * d > n:
            print(n)
            break


# ub_a()


def cifre(cif):
    return set(str(abs(cif)))


def ub_b():
    v = [
        12,
        21,
        21,
        12,
        33,
        45,
        54,
        45,
        54,
        45,
        54,
        45,
        66,
        89,
        98,
        89,
        89,
        89,
        89,
        89,
        89,
        89,
    ]
    nv = []
    lm = 1
    lc = 1
    start = 0
    temp_start = 0

    for i in range(1, len(v)):
        cif_ant = cifre(v[i - 1])
        cif_c = cifre(v[i])
        if cif_c == cif_ant:
            lc += 1
        else:
            if lc >= lm:
                lm = lc
                start = temp_start
            lc = 1
            temp_start = i
    if lc >= lm:
        lm = lc
        start = temp_start
    for i in range(start, start + lm):
        nv.append(v[i])
    print(nv)
    return lm


print(ub_b())
