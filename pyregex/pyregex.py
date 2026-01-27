import pyregex.parser as parser
import pyregex.backtracking as backtracking


def regex_match(regex, string):
    tree = parser.parse(regex)
    return backtracking.regex_match_backtrack(tree, string)
