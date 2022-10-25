# input: list of games and min-leaf size -> nested dict

# Method:
#     Iterate through each game for a depth of 1,
#     count up all first moves in a dictionary,
#     if all leaves below min_leaf_size -> done.
#     else add another filtration
#  def generate_opening_book(games, min_leaf_size=100) -> book

# easy: fixed depth opening book
from collections import defaultdict
from itertools import islice, zip_longest, groupby
from functools import reduce
import operator

def n_nested_ddict(depth=3):
    return defaultdict(lambda: n_nested_ddict(depth-1) if depth > 1 else 0)

def get_from_dict(d, mapList):
    return reduce(operator.getitem, mapList, d)

def increment_in_dict(d, mapList):
    get_from_dict(d, mapList[:-1])[mapList[-1]] += 1

def sum_leaves(d):
    if isinstance(d, int):
        return d
    return sum([v if isinstance(v, int) else sum_leaves(v) for v in d.values()])

def generate_fixed_depth_opening_book(games, depth=3):
    book = n_nested_ddict(depth=depth)
    for game in games:
        moves = list(islice(game.mainline_moves(), depth))
        if len(moves) == depth:
            increment_in_dict(book, moves)
    return book

def generate_rankings(d):
    kvs = [(k, sum_leaves(v)) for k, v in d.items()]
    return sorted(kvs, key=lambda x: x[1], reverse=True)
    # for other moves, defer to eval func
    
def _generate_variable_depth_opening_book(games, min_leaf_size):
    d = {}
    games = sorted(filter(lambda g: len(g), games), key=lambda g: str(g[0]))
    for k, grp in groupby(games, key=lambda g: g[0]):
        game_moves = list(grp)
        if len(game_moves) > min_leaf_size:
            d[k] = _generate_variable_depth_opening_book([g[1:] for g in game_moves], min_leaf_size)
        else:
            d[k] = len(game_moves)
    return d

def generate_variable_depth_opening_book(games, min_leaf_size=10):
    game_moves = list(map(lambda g: list(g.mainline_moves()), games))
    return _generate_variable_depth_opening_book(game_moves, min_leaf_size)