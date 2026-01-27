def parse(string):
    pass

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
        if index < len(string) and string[index] ==")":
            index += 1
        else:
            raise Exception("missing )")
    elif character in "*":
        raise Exception("first charcter cannot be a repeat")
    else:
        node = character
    index, node = parse_repeat(string, index, node)
    return index, node

def parse_repeat(string, index, node):
    if index == len(string) or string[index] not in "*":
        return index, node
    
    character = string[index]
    index += 1
    if character == "*":
        rmin = 0
        rmax = float("inf")
    
    node = ("repeat", node, rmin, rmax)
    return index, node

print(parse_alternation("a*", 0))