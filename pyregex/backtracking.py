def regex_match_backtrack(node, text):
    for index in match_backtrack_alternation(node, text, 0):
        print(index)
        if index == len(text):
            return True
    return False


def match_backtrack_alternation(node, text, index):
    if node is None:
        yield index
    elif isinstance(node, str):
        assert len(node) == 1, "expected a single character"
        if index < len(text) and text[index] == node:
            yield 1 + index
    elif node[0] == "concatenation":
        yield from match_backtrack_concatenation(node, text, index)


def match_backtrack_concatenation(node, text, index):
    met = set()
    for index1 in match_backtrack_alternation(node[1], text, index):
        if index1 in met:
            continue
        met.add(index1)
        yield from match_backtrack_alternation(node[2], text, index1)


print(regex_match_backtrack(("concatenation", "a", "b"), "ab"))
