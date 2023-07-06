million = 1000000


def Q(state, action, U):
    if action == 'hold':
        return U(state + million)
    if action == 'gamble':
        return U(state + 3 * million) * .5 + U(state) * .5


def actions(state): return ['hold', 'gamble']


def identity(x): return x


U = identity

def best_action(state, action,Q,U):
    # except utility
    def EU(action):return Q(state,action,U)
    return max(actions(state),key=EU)

print(best_action(million,actions,Q,U))


import math

print(best_action(100,actions,Q,math.log))
print(best_action(million*10,actions,Q,math.log))

U = math.log10
# what is c such that: Q(c,'gamble',U)==Q(c,'hold',U)
## c = [ ] million

print(Q(million,'gamble',U),Q(million,'hold',U))


# def c_generator():
#     start = 1
#     def fn(increase=True):
#         yield 1
#         while True:
#             yield start * 2
#     return fn
#
# for c in c_generator():
#     action = best_action(c,actions,Q,U)
#     print()