def parse(string):
    pass

# a|b
def parse_alternation(string, index):
    assert string[index] == "|"
    return ("alternation", string[index-1], string[index+1])

# ab
def parse_concatenation(string, index):
    return ("concatenation", string[index], string[index+1])