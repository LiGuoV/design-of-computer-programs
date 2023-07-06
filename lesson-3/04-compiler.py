def matchset(pattern,text):
    op,x,y = components(pattern)
    if 'lit' == op:
        return

# def lit(s):return ('lit',x)
def lit(s):
    return lambda text: set([text[len(s):]]) if text.startswith(s) else None
# elif 'seq' == op:
#     # 遍历 seq_1 余数(文本的其余部分,即t1) => 将y与余数匹配
#     return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
def seq(x,y):
    return lambda text: set().union(*map(y,x(text)))
# elif 'alt' == op:
#     # 并集
#     return matchset(x, text) | matchset(y, text)
def alt(x,y):
    return lambda text:x(text)|y(text)

