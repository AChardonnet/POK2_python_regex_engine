import pyregex

def test_alternation_parsing():
    assert pyregex.parse_alternation("a|b", 1) == ("alternation", "a", "b")
    assert pyregex.parse_alternation("b|a", 1) == ("alternation", "b", "a")
    assertionErrorRaised = False
    try:
        pyregex.parse_alternation("a|b",0) 
    except AssertionError:
        assertionErrorRaised = True
    assert assertionErrorRaised, "Should raise AssertionError"

def test_concatenation_parsing():
    assert pyregex.parse_concatenation("ab", 0) == ("concatenation", "a", "b")
    assert pyregex.parse_concatenation("ba", 0) == ("concatenation", "b", "a")