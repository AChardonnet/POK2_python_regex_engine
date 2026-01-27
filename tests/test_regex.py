import pyregex

def test_alternation_parsing():
    assert pyregex.parse_alternation("a|b", 0) == (3, ("alternation", "a", "b"))
    assert pyregex.parse_alternation("b|a", 0) == (3, ("alternation", "b", "a"))

def test_alternation_long_parsing():
    assert pyregex.parse_alternation("ab|cd", 0) == (5, ("alternation", ("concatenation", "a", "b"), ("concatenation", "c", "d")))

def test_alternation_multiple_parsing():
    assert pyregex.parse_alternation("a|b|c", 0) == (5, ("alternation", ("alternation", "a", "b"), "c"))

def test_concatenation_parsing():
    assert pyregex.parse_concatenation("ab", 0) == (2, ("concatenation", "a", "b"))
    assert pyregex.parse_concatenation("ba", 0) == (2, ("concatenation", "b", "a"))
    assert pyregex.parse_concatenation("|", 0) == (0, None)
    assert pyregex.parse_concatenation("a", 0) == (1, "a")

def test_concatenation_long_parsing():
    assert pyregex.parse_concatenation("abc", 0) == (3, ("concatenation", ("concatenation", "a", "b"), "c"))
    assert pyregex.parse_concatenation("abcd", 0) == (4, ('concatenation', ('concatenation', ('concatenation', 'a', 'b'), 'c'), 'd'))

def test_character_parsing():
    assert pyregex.parse_character("a", 0) == (1, "a")
    assert pyregex.parse_character("ab", 0) == (1, "a")

    assertionErrorRaised = False
    try: 
        pyregex.parse_character("|", 0)
    except AssertionError:
        assertionErrorRaised = True
    assert assertionErrorRaised, "Should raise an assertion error"

    assertionErrorRaised = False
    try: 
        pyregex.parse_character(")", 0)
    except AssertionError:
        assertionErrorRaised = True
    assert assertionErrorRaised, "Should raise an assertion error"

def test_alternation_parenthesis_parsing():
    print(pyregex.parse_alternation("ab(cd|ef)", 0))
    assert pyregex.parse_alternation("ab(cd|ef)", 0) == (9, ('concatenation', ('concatenation', 'a', 'b'), ('alternation', ('concatenation', 'c', 'd'), ('concatenation', 'e', 'f'))))

def test_repeat_parsing():
    assert pyregex.parse_alternation("a*", 0) == (2, ("repeat", "a", 0, float("inf")))
    assert pyregex.parse_alternation("a+", 0) == (2, ("repeat", "a", 1, float("inf")))
    assert pyregex.parse_alternation("a{4,42}", 0) == (7, ("repeat", "a", 4, 42))

def test_parsing():
    assert pyregex.parse("") is None
    assert pyregex.parse("a") == "a"
    assert pyregex.parse("ab") == ("concatenation", "a", "b")
    assert pyregex.parse("a|b") == ("alternation", "a", "b")
    assert pyregex.parse("a+") == ("repeat", "a", 1, float("inf"))
    assert pyregex.parse("a{2,42}") == ("repeat", "a", 2, 42)
    assert pyregex.parse("a|bc") == ("alternation", "a", ("concatenation", "b", "c"))
