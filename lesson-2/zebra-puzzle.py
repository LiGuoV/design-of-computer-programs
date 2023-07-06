'''
Zebra Puzzle
斑马拼图
1 有五栋房子。
1 There are five houses.

2 英国人住在红房子里。
2 The Englishman lives in the red house.

3 西班牙人拥有这只狗。
3 The Spaniard owns the dog.

4 咖啡在温室里喝。
4 Coffee is drunk in the green house.

5 乌克兰人喝茶。
5 The Ukrainian drinks tea.

6 绿色房子紧邻象牙色房子的右侧。
6 The green house is immediately to the right of the ivory house.

7 老金吸烟者拥有蜗牛。
7 The Old Gold smoker owns snails.

8 库尔在黄色房子里熏。
8 Kools are smoked in the yellow house.

9 中屋喝牛奶。
9 Milk is drunk in the middle house.

10 挪威人住在第一所房子里。
10 The Norwegian lives in the first house.

11 抽切斯特菲尔德烟的人住在养狐狸的人旁边的房子里。
11 The man who smokes Chesterfields lives in the house next to the man with the fox.

12 养马的房子旁边的一间房子里正在抽烟。
12 Kools are smoked in a house next to the house where the horse is kept.

13 好彩吸烟者喝橙汁。
13 The Lucky Strike smoker drinks orange juice.

14 日本人对议会抽烟。
14 The Japanese smokes Parliaments.

15 挪威人住在蓝房子旁边。
15 The Norwegian lives next to the blue house.

谁喝水？ 斑马的主人是谁？
Who drinks water? Who owns the zebra?

每栋房子都漆成不同的颜色，里面的居民来自不同的国籍，拥有不同的宠物，喝不同的饮料，抽不同品牌的美国香烟。
Each house is painted a different color, and their inhabitants are of different nationalities, own different pets, drink different beverages and smoke different brands of American cigarettes.
'''

import itertools


# nationalities = ['Englishman','Spaniard','Ukrainian','Norwegian','Japanese',]

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1 - h2 == 1


def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1 - h2) == 1


counts = 0


def zebra_puzzle():
    # houses = [1, 2, 3, 4, 5]
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]

    # orderings = itertools.permutations(houses)
    orderings = list(itertools.permutations(houses))



    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in c(orderings)
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in c(orderings)
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )


import time


def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    time.time()
    t0 = time.clock()
    result = fn(*args)
    t1 = time.time()
    return t1 - t0, result


def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))


def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    # Your code here.

    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])

    return min(times), average(times), max(times)

def c(iterable):
    c.starts +=1
    for x in iterable:
        c.items +=1
        yield x
c.starts = 0
c.items = 0

def instrument_fn(fn,*args):
    c.starts,c.items = 0,0
    result = fn(*args)
    print(f'{fn.__name__} got {result} with {c.starts:0=8,} iters orver {c.items:,} items.')

print(zebra_puzzle())
print(counts)
instrument_fn(zebra_puzzle)

def ints(start,end=None):
    while end is None or start <= end :
        yield start
        start +=1

def all_ints():
    yield 0
    for n in ints(1):
        yield n
        yield -n
a = all_ints()
next(a)
next(a)
next(a)
next(a)
