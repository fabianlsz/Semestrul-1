def count_char(word):
    count = {}
    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count


# print(count_char("school"))


def anag(word1, word2):
    count1 = count_char(word1)
    count2 = count_char(word2)

    for key in count1:
        if count1[key] != count2[key]:
            return False
        return True


def add_tags(tag, word):
    # return "<{}> {} </{}>".format(tag, word, tag)
    return f"<{tag}> {word} </{tag}>"


# print(add_tags("i", "Python"))


def fact(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


# print(fact(3))


def is_pali(word):
    for i in range(len(word)):
        if word[i] != word[len(word) - i - 1]:
            return False
        return True


# print(is_pali("rentner"))


def str_find(cuv1, cuv2):
    len_cuv1 = len(cuv1)
    len_cuv2 = len(cuv2)
    if len_cuv2 > len_cuv1:
        return -1
    for i in range(len_cuv1 - len_cuv2 + 1):
        found = True

        for j in range(len_cuv2):
            if cuv1[i + j] != cuv2[j]:
                found = False
                break
        if found:
            return i
    return -1


print(str_find("testing", "ing"))
print(str_find("abcdefg", "hij"))
