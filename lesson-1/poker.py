# hand_card 手牌5张
# rank 大小
# suit 花色 Clubs, Spades, Hearts Diamonds
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands.
#
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function
#                  returns their corresponding ranks as a
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks
#                  in a hand (where the order goes from
#                  highest to lowest rank).
import random


def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return allmax(hands, key=hand_rank2)


def deal(numhands, n=5, deck=[r + s for r in '23456789TJQKA' for s in 'CSHD']):
    deck = random.sample(deck, len(deck))
    return [[deck.pop() for _ in range(n)] for _ in range(numhands)]


def allmax(iterable, key):
    result, max_val = [], None
    key = key or (lambda x: x)
    for x in iterable:
        x_val = key(x)
        if not result and x_val > max_val:
            print(x_val, max_val)
            result, max_val = [x], x_val
        elif x_val == max_val:
            result.append(x)
    return result


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    if k4 := kind(4, ranks):
        return (7, k4, kind(1, ranks))
    if (k3 := kind(3, ranks)) and (k2 := kind(2, ranks)):
        return (6, k3, k2)
    if flush(hand):
        return (5, ranks)
    if straight(ranks):
        return (4, max(ranks))
    if k3 := kind(3, ranks):
        return (3, k3, ranks)
    if tp := two_pair(ranks):
        return (2, tp, ranks)
    if k2 := kind(2, ranks):
        return (1, k2, ranks)
    return (0, ranks)

def hand_rank2(hand):
    # ranks = ('--23456789TJQKA'.index(r) for r, _ in hand)
    # ranks = sorted(ranks, reverse=True)
    groups = group(['--23456789TJQKA'.index(r) for r, _ in hand])
    # (3个,A),(2个，J）
    counts,ranks = zip(*groups)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]

    def get_lev(counts):
        match counts:
            case (5,):
                return  9
            case _ if straight(ranks) and flush(hand):
                return 8
            case (4,1):
                return 7
            case (3,2):
                return 6
            case _ if flush(hand):
                return 5
            case _ if straight(ranks):
                return 4
            case (3,1,1):
                return 3
            case (2,2,1):
                return 2
            case (2,1,1,1):
                return 1
            case _:
                return 0
    return get_lev(counts),ranks

def group(items:list):
    groups =  [(items.count(x),x) for x in set(items)]
    return sorted(groups,reverse=True)

def card_ranks(hand):
    ranks = ('--23456789TJQKA'.index(r) for r, _ in hand)
    ranks = sorted(ranks, reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def straight(ranks):
    # 顺子
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5


def flush(hand):
    # 同花
    return len(set([s for _, s in hand])) == 1


def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and pair != low_pair:
        return (pair, low_pair)


def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()  # Two pairs

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 7, 6, 4]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(tpranks) == (9, 5)
    # assert poker([sf, fk, fh]) == sf
    # assert poker([fk, fh]) == fk
    # assert poker([fh, fh]) == fh
    # assert poker([sf]) == sf
    # assert poker([sf, *99 * [fk]]) == sf
    # assert hand_rank2(sf) == (8, 10)
    # assert hand_rank2(fk) == (7, 9, 7)
    # assert hand_rank2(fh) == (6, 10, 7)
    return 'tests pass'


print(test())
# print(deal(10,5))