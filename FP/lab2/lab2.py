# 1
def duplicate(numere):
    """Programul elimina duplicatele din lista

    Parameters
    ----------
    numere : list
        Lista cu numere cu n aparitii

    Returns
    -------
    list
        Lista cu numere cu o aparitie
    """
    return list(set(numere))


# numere1 = [21, 21, 21, 15, 15, 15, 29,29,29,31,31,10,10]
# print(duplicate(numere1))


# 2
def count_simetrice(numere2):
    """Returneaza numarul de perechi simetrice

    Parameters
    ----------
    list : numere2
        Lista cu numere

    Returns
    -------
    cnt
        Numarul de perechi

    """
    cnt = 0
    accesat = set()
    for num in numere2:
        zeci = num // 10
        unitati = num % 10
        invers = unitati * 10 + zeci
        if invers in accesat:
            cnt += 1
        accesat.add(num)
    return cnt


# numere2 = [12, 18, 81, 90, 21, 37, 73]
# print(count_simetrice(numere2))

# 3 in doua variante // 1 cu sortare scrisa de mana // 2 cu functia numere.sort(reverse = True)
"""def concatenation(numere):
    def compare(num1, num2):
        v1 = str(num1) + str(num2)
        v2 = str(num2) + str(num1)
        return v1 > v2

    n = len(numere)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not compare(numere[j], numere[j + 1]):
                numere[j], numere[j + 1] = numere[j + 1], numere[j]
    rezultat = ""
    for num in numere:
        rezultat += str(num)
    return rezultat"""


def concatenation2(numere):
    """Programul returneaza cel mai mare numar concatenat din lista

    Parameters
    ----------
    numere : List
        Lista cu numere neordonate

    Returns
    -------
    rezultat
        Cel mai mare numar rezultat din ordonarea crescatoare si concatenarea numerelor din lista
    """
    rezultat = ""
    numere.sort(reverse=True)
    for num in numere:
        rezultat += str(num)
    return rezultat


# numere3 = [11, 22, 15, 21, 98, 16]
# print(concatenation2(numere3))


# 4
def cryptography(numere):
    """ "Cripteaza" lista utilizand adunarea cu primul numar din lista

    Parameters
    ----------
    numere : list
        Lista cu numere

    Returns
    -------
    List
        Lista cu numerele criptate, primul ramanand la fel
    """
    n = numere[0]
    for i in range(1, len(numere)):
        numere[i] += n
    return numere


# numere4 = [15, 29, 19, 20, 23, 10, -12, -15]
# print(cryptography(numere4))


# 5 varianta 1 varianta proasta, v2 cea buna
'''def filter(numere):
    """Cauta numerele din lista cu proprietatea x = y * 2

    Parameters
    ----------
    numere : List
        Lista cu numere

    Returns
    -------
    List
        Lista cu perechi de numere ce respecta conditia
    """
    rezultat = []
    for x in numere:
        for y in numere:
            if x == y * 2:
                rezultat.append((x, y))
    return rezultat
'''


def filter2(numere, conditie):
    """Returneaza lista cu numerele care indeplinesc conditia specificata

    Parameters
    ----------
    numere : List
        Lista cu numerele de verificat
    conditie : string
        Conditia sub forma de expresie de tipul 'x == y * 2'

    Returns
    -------
    List
        Lista cu numerele care indeplinesc conditia
    """
    rezultat = []

    for i in numere:
        pc = i // 10  # prima cifra din numarul curent
        uc = i % 10  # ultima cifra din numarul curent
        cond = conditie.replace("x", str(pc)).replace("y", str(uc))
        if "==" in cond:
            stanga, dreapta = cond.split("==")
            if expresie(stanga.strip()) == expresie(dreapta.strip()):
                rezultat.append(i)
    return rezultat


def expresie(semn):
    """Evalueaza expresia matematica cu operatori simpli +, -, // si *

    Parameters
    ----------
    semn : string
        Expresia matematica in format string

    Returns
    -------
    int
        Rezultatul evaluarii expresiei
    """
    if "*" in semn:
        stanga, dreapta = semn.split("*")
        return int(stanga.strip()) * int(dreapta.strip())
    elif "+" in semn:
        stanga, dreapta = semn.split("+")
        return int(stanga.strip()) + int(dreapta.strip())
    elif "-" in semn:
        stanga, dreapta = semn.split("-")
        return int(stanga.strip()) - int(dreapta.strip())
    elif "//" in semn:
        stanga, dreapta = semn.split("//")
        return int(stanga.strip()) // int(dreapta.strip())
    else:
        return int(semn.strip())


# 6
def domino(numere):
    """Returneaza cea mai lunga secventa de numere cu proprietatea ca ultima cifra a numarului curent este egala cu prima cifra a succesorului sau din lista

    Parameters
    ----------
    numere : List
        Lista cu numere

    Returns
    -------
    list
        Lista cu cea mai lunga secventa care respecta proprietatea
    """
    secv_curenta = []
    lmax = []
    secv_curenta.append(numere[0])

    for i in range(1, len(numere)):
        ant = numere[i - 1]
        curent = numere[i]
        antUC = ant % 10  # ultima cifra a numarului anterior
        curPC = curent // 10  # prima cifra a numarului curent

        if antUC == curPC:
            secv_curenta.append(curent)
        else:
            if len(secv_curenta) > len(lmax):
                lmax = list(secv_curenta)
            secv_curenta.clear()
            secv_curenta.append(curent)
    if len(secv_curenta) > len(lmax):
        lmax = list(secv_curenta)

    return lmax


# numere6 = [12, 25, 58, 87, 77, 72, 20, 12, 29, 95, 56, 64, 47, 72, 29, 90]
# print(domino(numere6))


# 7


def cmmdc(a, b):
    """Returneaza cel mai mare divizor comun al lui a si b

    Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    int
        CMMDC al lui a si b
    """
    while b:
        r = a % b
        a = b
        b = r
    return a


def cmmmc(a, b):
    """Returneaza cel mai mic multiplu comun dintre a si b utilizand CMMDC

    Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    int
       CMMMC al lui a si b
    """
    cmmdc1 = cmmdc(a, b)
    cmmmc1 = abs(a * b) // cmmdc1
    return cmmmc1


def index(ind_from, ind_to, lista):
    """Returneaza cel mai mic multiplu comun dintr-un interval de numere

    Parameters
    ----------
    ind_from : int
        Index-ul primului element de la care porneste calcularea CMMMC
    ind_to : int
        Index-ul ultimului element la care se opreste calcularea CMMMC
    lista : list
        Lista care contine numerele

    Returns
    -------
    int
        Returneaza rezultatul calculului
    """
    result = lista[ind_from]
    for i in range(ind_from + 1, ind_to + 1):
        result = cmmmc(result, lista[i])
    return result


def main():

    # 1
    print(
        "Lista de numere dupa eliminarea duplicatelor este: ",
        duplicate([21, 21, 21, 15, 15, 15, 29, 29, 29, 31, 31, 10, 10]),
    )

    # 2
    print(
        "Perechile de numere simetrice de tip (xy) si (yx) sunt: ",
        count_simetrice([12, 18, 81, 90, 21, 37, 73]),
    )

    # 3
    print(
        "Cel mai mare numar in urma sortarii si concatenarii numerelor este: ",
        concatenation2([11, 22, 15, 21, 98, 16]),
    )

    # 4
    # rez = cryptography([15, 29, 19, 20, 23, 10, -12, -15])
    print("Numerele dupa criptare:", cryptography([15, 29, 19, 20, 23, 10, -12, -15]))

    # 5
    # rez = filter2([[21, 42, 44, 86, 65, 86, 96, 63, 84]])
    numere1203 = [20, 42, 44, 86, 65, 86, 96, 63, 84, 21, 31]
    conditie = "x + 1 = y + 3"
    conditie = conditie.replace("=", "==")
    rez = filter2(numere1203, conditie)
    print(f"Perechi {conditie}: ", rez)

    # 6
    rez = domino([12, 25, 58, 87, 77, 72, 20, 12, 29, 95, 56, 64, 47, 72, 29, 90])
    print("Domino: ", rez)

    # 7
    eroare = "Numarul introdus depaseste lungimea listei!"
    lista = [3, 6, 9, 2, 1, 18, 36, 12, 24, 20, 26, 10, 14]
    index_from = int(input("x: "))
    index_to = int(input("y: "))
    if (
        index_from < 0
        or index_from >= len(lista)
        or index_to < 0
        or index_to >= len(lista)
        or index_from > index_to
    ):
        print(eroare)
        exit
    else:
        print(
            f"CMMMC al numerelor din intervalul {index_from}, {index_to} este: ",
            index(index_from, index_to, lista),
        )


if __name__ == "__main__":
    main()
