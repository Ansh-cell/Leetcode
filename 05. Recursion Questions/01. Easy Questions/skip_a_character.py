a: str = "baccarat"


def skip_char(string: str, index: int, answer=""):
    if index == len(string):
        return ""
    else:
        if string[index] != "a":
            answer += string[index]
            return answer + skip_char(string, index + 1)
        else:
            return answer + skip_char(string, index + 1)


print(skip_char(a, 0))
