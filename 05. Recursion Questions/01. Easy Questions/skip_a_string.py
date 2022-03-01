x = "aapplehhh"


def skip_char(string: str, index: int, answer=""):
    if index == len(string):
        return ""
    else:
        if string[index:].startswith("apple"):
            return answer + skip_char(string, index + 5)
        else:
            answer += string[index]
            return answer + skip_char(string, index + 1)


print(skip_char(x, 0, ""))