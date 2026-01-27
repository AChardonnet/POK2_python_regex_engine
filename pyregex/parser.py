REGEX_MAX_REPEAT = 424242424242


def parse(string):
    index, tree = parse_alternation(string, 0)
    assert index == len(string), "parsing stopped early"
    return tree


# a|b, ab|cd
def parse_alternation(string, index):
    index, left = parse_concatenation(string, index)
    while index < len(string):
        if string[index] == ")":
            break
        assert string[index] == "|", "There is a problem"
        index, right = parse_concatenation(string, index + 1)
        left = ("alternation", left, right)
    return index, left


# abc...  (complete)
def parse_concatenation(string, index):
    left = None
    while index < len(string):
        if string[index] in "|)":
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
    assert character not in "|)"
    if character == "(":
        index, node = parse_alternation(string, index)
        if index < len(string) and string[index] == ")":
            index += 1
        else:
            raise Exception("missing )")
    elif character in "*+{":
        raise Exception("first charcter cannot be a repeat")
    else:
        node = character
    index, node = parse_repeat(string, index, node)
    return index, node


def parse_repeat(string, index, node):
    if index == len(string) or string[index] not in "*+{":
        return index, node

    character = string[index]
    index += 1
    if character == "*":
        rmin = 0
        rmax = float("inf")
    elif character == "+":
        rmin = 1
        rmax = float("inf")
    else:
        index, rmin = parse_int(string, index)
        if rmin is None:
            raise Exception("expected int")
        if index < len(string) and string[index] == ",":
            index, rmax = parse_int(string, index + 1)
            if rmax is None:
                rmax = float("inf")
        if index < len(string) and string[index] == "}":
            index += 1
        else:
            raise Exception("expected }")

    assert rmin < rmax, "min repeat should be lesser than max repeat"
    assert rmin < REGEX_MAX_REPEAT

    node = ("repeat", node, rmin, rmax)
    return index, node


def parse_int(string, index):
    start = index
    while index < len(string) and string[index].isdigit():
        index += 1
    if start != index:
        toReturn = int(string[start:index])
    else:
        toReturn = None
    return index, toReturn
