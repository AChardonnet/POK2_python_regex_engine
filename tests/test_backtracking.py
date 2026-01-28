import pyregex.backtracking as backtracking


def test_backtracking_None():
    assert backtracking.regex_match_backtrack(None, "azerty") == False


def test_backtracking_single_char():
    assert backtracking.regex_match_backtrack("a", "a") == True
    assert backtracking.regex_match_backtrack("a", "aa") == False
    assert backtracking.regex_match_backtrack("a", "b") == False


def test_backtracking_concatenation():
    assert backtracking.regex_match_backtrack(("concatenation", "a", "b"), "ab") == True
    assert backtracking.regex_match_backtrack(("concatenation", "a", "b"), "a") == False
    assert (
        backtracking.regex_match_backtrack(("concatenation", "a", "b"), "ba") == False
    )
    assert (
        backtracking.regex_match_backtrack(("concatenation", "a", "b"), "aab") == False
    )


def test_backtracking_alternation():
    assert backtracking.regex_match_backtrack(("alternation", "a", "b"), "a") == True
    assert backtracking.regex_match_backtrack(("alternation", "a", "b"), "b") == True
    assert backtracking.regex_match_backtrack(("alternation", "a", "b"), "ab") == False
    assert backtracking.regex_match_backtrack(("alternation", "a", "b"), "ba") == False


def test_backtracking_alternation_concatenation():
    # (a | b)c
    node = ("concatenation", ("alternation", "a", "b"), "c")
    assert backtracking.regex_match_backtrack(node, "ac") == True
    assert backtracking.regex_match_backtrack(node, "bc") == True
    assert backtracking.regex_match_backtrack(node, "ab") == False
    # (ab | ac)
    node = ("alternation", ("concatenation", "a", "b"), ("concatenation", "a", "c"))
    assert backtracking.regex_match_backtrack(node, "ab") == True
    assert backtracking.regex_match_backtrack(node, "ac") == True
    assert backtracking.regex_match_backtrack(node, "ba") == False
    assert backtracking.regex_match_backtrack(node, "abc") == False


def test_backtracking_repeat():
    # a*
    node = ("repeat", "a", 0, float("inf"))
    assert backtracking.regex_match_backtrack(node, "") == True
    assert backtracking.regex_match_backtrack(node, "a") == True
    assert backtracking.regex_match_backtrack(node, 42 * "a") == True
    # a+
    node = ("repeat", "a", 1, float("inf"))
    assert backtracking.regex_match_backtrack(node, "") == False
    assert backtracking.regex_match_backtrack(node, "a") == True
    assert backtracking.regex_match_backtrack(node, 42 * "a") == True
    # a{4,42}
    node = ("repeat", "a", 4, 42)
    assert backtracking.regex_match_backtrack(node, "") == False
    assert backtracking.regex_match_backtrack(node, "a") == False
    assert backtracking.regex_match_backtrack(node, 42 * "a") == True
