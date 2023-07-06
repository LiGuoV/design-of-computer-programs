import itertools
from typing import Iterable


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    if text == '': return 0, 0
    text = text.lower()

    def length(x): a, b = x;return b - a

    # 以一个位置为中心的最大字符串
    candidate = [
        all_subpalidrome(text, start, end)
        for start in range(len(text))
        for end in (start, start + 1)]
    return max(candidate, key=length)


def all_subpalidrome(text, start, end):
    print(start,end,'=====')
    while (start > 0
           and end < len(text)
           # and is_palindrome(text[start:end])):
           and text[start-1] == text[end]):
        start -= 1;end += 1
    return start, end

# def is_palindrome(text):
#     return text == text[::-1]


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    # assert L('racecar') == L('Racecar') == L('RacecarX') == (0, 7)
    # assert L('Race carr') == (7, 9)
    # assert L('') == (0, 0)
    # assert L('something rac e car going') == (8, 21)
    # assert L('xxxxx') == (0, 5)
    # assert L('Mad am I ma dam.') == (0, 15)
    # return 'tests pass'


print(test())
