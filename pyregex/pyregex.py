def parse(string):
    pass

def parse_alternation(string, index):
    assert string[index] == "|"
    return ("alternation", string[index-1], string[index+1])