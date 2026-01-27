def regex_match_backtrack(tree, text):
    for index in match_backtrack(tree, text, 0):
        if index == len(text):
            return True
    return False


def match_backtrack(tree, text, index):
    if tree is None:
        yield index
    elif isinstance(tree, str):
        assert len(tree) == 1, "Invalid Tree"
        if index < len(text) and text[index] == tree:
            yield index + 1


print(regex_match_backtrack("a", "a"))
