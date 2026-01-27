def parse(string):
    pass

# a|b, ab|cd
def parse_alternation(string, index):
    index, left = parse_concatenation(string, index)
    assert string[index] == "|", "There is a problem"
    index, right = parse_concatenation(string, index + 1)
    return index, ("alternation", left, right)

# abc...  (complete)
def parse_concatenation(string, index):
    left = None
    while index < len(string):
        if string[index] == "|":
            break
        right = string[index]
        index += 1
        if left is None:
            left = right
        else:
            left = ("concatenation", left, right)
    return index, left

print(parse_alternation("ab|cd",0))