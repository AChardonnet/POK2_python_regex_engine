import pyregex.backtracking as backtracking


def test_backtracking_None():
    assert backtracking.regex_match_backtrack(None, "azerty") == False


def test_backtracking_single_char():
    assert backtracking.regex_match_backtrack("a", "a") == True
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
