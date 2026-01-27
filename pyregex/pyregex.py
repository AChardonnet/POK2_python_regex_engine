def parse(string):
    pass

# a|b
def parse_alternation(string, index):
    assert string[index] == "|"
    return index, ("alternation", string[index-1], string[index+1])

# ab
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

print(parse_concatenation("abcd",0))