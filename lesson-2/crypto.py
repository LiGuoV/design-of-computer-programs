import itertools
import re


def solve(formula):
    for f in fill_in(formula):
        if valid(f):
            return f

def compile_formula(formula,verbose=False):
    """
    ODD+ODD==EVEN
    """
    # ODEVN
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))

    # 排除0前导 找出字母
    first_letters = set(re.findall(r'\b([A-Z])[A-Z]+',formula))

    # [O,D,E,V,N]
    params = ', '.join(letters)
    # ['', 'ODD', '+', 'ODD', '==', 'EVEN', '']
    tokens = map(compile_word,re.split(r'([A-Z]+)',formula))
    # (O*100+D*10+D*1)+(O*100+D*10+D*1)==(E*1000+V*100+E*10+N*1)

    # if E !=0 and O != 0:
    test = ' and '.join(f'{x}!=0' for x in first_letters)
    print(first_letters,test)
    body = ''.join(tokens)
    f = f'lambda {params}:{test} and {body}'
    if verbose:print(f)
    return eval(f),letters

def faster_solve(formula):
    f,letters = compile_formula(formula)
    for digits in itertools.permutations([0,1,2,3,4,5,6,7,8,9], r=len(letters)):
        try:
            if f(*digits) is True:
                print(digits)
                table = str.maketrans(letters, ''.join(map(str,digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass

def fill_in(formula):
    # letters = ''.join([c for c in set(f) if c.isalpha()])
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    # 'ABC'
    for digits in itertools.permutations('1234567890', r=len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError as e:
        print(e)
        return False

def compile_word(word):
    # YOU => '(100*Y+10*O+1*U)'
    if word.isupper():
        terms = [f'{char}*{10**i}' for i,char in enumerate(reversed(word))]
        return '('+ '+'.join(reversed(terms)) + ')'
    return word

# solve('ODD+ODD==EVEN')
result = faster_solve('ODD+ODD==EVEN')
print(result)


# def foo():
#     foo.a = 'a'
# foo()
# print(foo.a)
