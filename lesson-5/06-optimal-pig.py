import random

other = {1: 0, 0: 1}
goal = 50


def hold(state):
    (p, me, you, pending) = state
    return (other[p], you, me + pending, 0)


def roll(state, d):
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me + 1, 0)  # pig out; other player's turn
    else:
        return (p, me, you, pending + d)  # accumulate die roll in pending


# 效用函数使用了获胜概率 赢1 输0
def Q_pig(state, action, Pwin):
    if action == 'hold':
        return 1 - Pwin(hold(state))
    if action == 'roll':
        return (1 - Pwin(roll(state, 1))
                + sum(Pwin(roll(state, d))
                      for d in (2, 3, 4, 5, 6))
                ) / 6
    raise ValueError


def actions(state):
    *_, pending = state
    return ['roll', 'hold'] if pending else ['roll']


def memo(f):
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(args)

    return _f


@memo
def Pwin(state):
    p, me, you, pending = state
    if me + pending >= goal:
        return 1
    if you + pending >= goal:
        return 0
    return max(Q_pig(state, action, Pwin)
               for action in actions(state))


# 新的效用函数 领先分数
@memo
def Q_win_diff(state):
    p, me, you, pending = state
    if me + pending >= goal or you >= goal:
        return (me + pending - you)
    return max(Q_pig(state, action, Q_win_diff)
               for action in actions(state))


def best_action(state, action, Q, U):
    # except utility
    def EU(action): return Q(state, action, U)

    return max(actions(state), key=EU)


# max_wins = lambda state: best_action(state, actions, Q_pig, Pwin)
max_wins = lambda state: best_action(state, actions, Q_pig, Q_win_diff)


# print(max_wins())
def hold_at(x):
    """Return a strategy that holds if and only if
    pending >= x or player reaches goal."""

    def strategy(state):
        # your code here
        _, me, you, pending = state
        return 'hold' if (me + pending >= goal) | (pending >= x) else 'roll'

    strategy.__name__ = 'hold_at(%d)' % x
    return strategy


possible_moves = ['roll', 'hold']


def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    # your code here
    return random.choice(possible_moves)


strategies = [clueless,
              hold_at(goal / 4),
              hold_at(1 + goal / 3),
              hold_at(goal / 2),
              hold_at(goal),
              max_wins
              ]


def test():
    assert (max_wins((1, 5, 34, 4))) == "roll"
    assert (max_wins((1, 18, 27, 8))) == "roll"
    assert (max_wins((0, 23, 8, 8))) == "roll"
    assert (max_wins((0, 31, 22, 9))) == "hold"
    assert (max_wins((1, 11, 13, 21))) == "roll"
    assert (max_wins((1, 33, 16, 6))) == "roll"
    assert (max_wins((1, 12, 17, 27))) == "roll"
    assert (max_wins((1, 9, 32, 5))) == "roll"
    assert (max_wins((0, 28, 27, 5))) == "roll"
    assert (max_wins((1, 7, 26, 34))) == "hold"
    assert (max_wins((1, 20, 29, 17))) == "roll"
    assert (max_wins((0, 34, 23, 7))) == "hold"
    assert (max_wins((0, 30, 23, 11))) == "hold"
    assert (max_wins((0, 22, 36, 6))) == "roll"
    assert (max_wins((0, 21, 38, 12))) == "roll"
    assert (max_wins((0, 1, 13, 21))) == "roll"
    assert (max_wins((0, 11, 25, 14))) == "roll"
    assert (max_wins((0, 22, 4, 7))) == "roll"
    assert (max_wins((1, 28, 3, 2))) == "roll"
    assert (max_wins((0, 11, 0, 24))) == "roll"
    return 'tests pass'


print(test())
