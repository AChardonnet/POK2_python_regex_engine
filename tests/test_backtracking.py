import pyregex.backtracking as backtracking


def test_backtracking_None():
    assert backtracking.regex_match_backtrack(None, "azerty") == False


def test_backtracking_single_char():
    assert backtracking.regex_match_backtrack("a", "a") == True
    assert backtracking.regex_match_backtrack("a", "b") == False
