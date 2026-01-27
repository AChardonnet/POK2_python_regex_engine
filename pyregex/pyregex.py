def parse(string):
    pass

# a|b, ab|cd
def parse_alternation(string, index):
    index, left = parse_concatenation(string, index)
    while index < len(string):
        assert string[index] == "|", "There is a problem"
        index, right = parse_concatenation(string, index + 1)
        left = ("alternation", left, right)
    return index, left

# abc...  (complete)
def parse_concatenation(string, index):
    left = None
    while index < len(string):
        if string[index] == "|":
            break
        index, right = parse_character(string, index)
        if left is None:
            left = right
        else:
            left = ("concatenation", left, right)
    return index, left


def parse_character(string, index):
    character = string[index]
    index += 1
    return index, character