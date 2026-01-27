REGEX_MAX_REPEAT = 424242424242


def regex_match_backtrack(node, text):
    for index in match_backtrack_alternation(node, text, 0):
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
    elif node[0] == "alternation":
        yield from match_backtrack_alternation(node[1], text, index)
        yield from match_backtrack_alternation(node[2], text, index)
    elif node[0] == "repeat":
        yield from match_backtrack_repeat(node, text, index)


def match_backtrack_concatenation(node, text, index):
    met = set()
    for index1 in match_backtrack_alternation(node[1], text, index):
        if index1 in met:
            continue
        met.add(index1)
        yield from match_backtrack_alternation(node[2], text, index1)


def match_backtrack_repeat(node, text, index):
    _, node, rmin, rmax = node
    rmax = min(rmax, REGEX_MAX_REPEAT)
    output = []
    if rmin == 0:
        output.append(index)
    start = {index}
    for i in range(1, rmax + 1):
        found = set()
        for index1 in start:
            for index2 in match_backtrack_alternation(node, text, index1):
                found.add(index2)
                if i >= rmin:
                    output.append(index2)
        if not found:
            break
        start = found
    yield from reversed(output)
