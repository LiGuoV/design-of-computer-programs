[视频列表](https://www.youtube.com/watch?v=49qSOQpFExQ&list=PLAwxTw4SYaPnJVtPvZZ5zXj_wRBjH0FxX)
[扑克手牌规则](https://en.wikipedia.org/wiki/List_of_poker_hands)

| 迭代器例子                                    | 结果                                              |
|------------------------------------------|-------------------------------------------------|
| product('ABCD', repeat=2)                | AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD |
| product('ABCD', 'xy')                    | Ax Ay Bx By Cx Cy Dx Dy                         |
| product(range(2), repeat=3)              | 000 001 010 011 100 101 110 111                 |
| permutations('ABCD', 2)                  | AB AC AD BA BC BD CA CB CD DA DB DC             |
| combinations('ABCD', 2)                  | AB AC AD BC BD CD                               |
| combinations_with_replacement('ABCD', 2) | AA AB AC AD BB BC BD CC CD DD                   |
```python
itertools.permutations([1, 2, 3, 4, 5], 2) =>
  (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 1), (2, 3), (2, 4), (2, 5),
  (3, 1), (3, 2), (3, 4), (3, 5),
  (4, 1), (4, 2), (4, 3), (4, 5),
  (5, 1), (5, 2), (5, 3), (5, 4)
  
itertools.combinations([1, 2, 3, 4, 5], 2) =>
  (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 3), (2, 4), (2, 5),
  (3, 4), (3, 5),
  (4, 5)
  
itertools.combinations_with_replacement([1, 2, 3, 4, 5], 2) =>
  (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 2), (2, 3), (2, 4), (2, 5),
  (3, 3), (3, 4), (3, 5),
  (4, 4), (4, 5),
  (5, 5)


```
[排列](https://zh.wikipedia.org/zh-hans/%E6%8E%92%E5%88%97)  
[组合](https://zh.wikipedia.org/wiki/%E7%B5%84%E5%90%88)  
[标准库](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.combinations)  
[函数式编程指引](https://docs.python.org/zh-cn/3/howto/functional.html)  
列表推导 _list comprehension_  
```python
    [rank 
    for rank,suit in card if rank in 'JQK 
    for ... if ...
    for ... if ...]
```
生成器表达式 _generator experssion_
> 与列表区别: 用"( )"包裹 & 延迟计算

正则也叫 _pattern_

```python
import re

s = "ba! baaa!"
re.findall(r'baa*!',s)
> ['ba!', 'baaa!']
```

| special | e.g. | match      |
|---------|------|------------|
| *       | a*   | '',a,aa,aa |
| ?       | a?   | '',a,      |
| .       | .    | 非空字符       |
| ^       | ^a   | a1 ab ac   |
| $       | a$   | ba         |
|         |      |            |
