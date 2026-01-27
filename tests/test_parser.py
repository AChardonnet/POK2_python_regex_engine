import pyregex.parser as parser

def test_alternation_parsing():
    assert parser.parse_alternation("a|b", 0) == (3, ("alternation", "a", "b"))
    assert parser.parse_alternation("b|a", 0) == (3, ("alternation", "b", "a"))

def test_alternation_long_parsing():
    assert parser.parse_alternation("ab|cd", 0) == (5, ("alternation", ("concatenation", "a", "b"), ("concatenation", "c", "d")))

def test_alternation_multiple_parsing():
    assert parser.parse_alternation("a|b|c", 0) == (5, ("alternation", ("alternation", "a", "b"), "c"))

def test_concatenation_parsing():
    assert parser.parse_concatenation("ab", 0) == (2, ("concatenation", "a", "b"))
    assert parser.parse_concatenation("ba", 0) == (2, ("concatenation", "b", "a"))
    assert parser.parse_concatenation("|", 0) == (0, None)
    assert parser.parse_concatenation("a", 0) == (1, "a")

def test_concatenation_long_parsing():
    assert parser.parse_concatenation("abc", 0) == (3, ("concatenation", ("concatenation", "a", "b"), "c"))
    assert parser.parse_concatenation("abcd", 0) == (4, ('concatenation', ('concatenation', ('concatenation', 'a', 'b'), 'c'), 'd'))

def test_character_parsing():
    assert parser.parse_character("a", 0) == (1, "a")
    assert parser.parse_character("ab", 0) == (1, "a")

    assertionErrorRaised = False
    try: 
        parser.parse_character("|", 0)
    except AssertionError:
        assertionErrorRaised = True
    assert assertionErrorRaised, "Should raise an assertion error"

    assertionErrorRaised = False
    try: 
        parser.parse_character(")", 0)
    except AssertionError:
        assertionErrorRaised = True
    assert assertionErrorRaised, "Should raise an assertion error"

def test_alternation_parenthesis_parsing():
    print(parser.parse_alternation("ab(cd|ef)", 0))
    assert parser.parse_alternation("ab(cd|ef)", 0) == (9, ('concatenation', ('concatenation', 'a', 'b'), ('alternation', ('concatenation', 'c', 'd'), ('concatenation', 'e', 'f'))))

def test_repeat_parsing():
    assert parser.parse_alternation("a*", 0) == (2, ("repeat", "a", 0, float("inf")))
    assert parser.parse_alternation("a+", 0) == (2, ("repeat", "a", 1, float("inf")))
    assert parser.parse_alternation("a{4,42}", 0) == (7, ("repeat", "a", 4, 42))

def test_parsing():
    assert parser.parse("") is None
    assert parser.parse("a") == "a"
    assert parser.parse("ab") == ("concatenation", "a", "b")
    assert parser.parse("a|b") == ("alternation", "a", "b")
    assert parser.parse("a+") == ("repeat", "a", 1, float("inf"))
    assert parser.parse("a{2,42}") == ("repeat", "a", 2, 42)
    assert parser.parse("a|bc") == ("alternation", "a", ("concatenation", "b", "c"))
