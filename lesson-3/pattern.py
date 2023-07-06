"""
特殊字符
*
    a* 空字符串 和0次多次前面的字符
?
    a? 一个任意字符
.
    [独立使用] 不是2个字符序列 不匹配空串
^
    ^a 限制在开头
$
    a$ 尾
不属于上面特殊字符的都与本身完全匹配 ab 匹配 ab
'' 空串匹配空串

"""
# search 任何位置进行测试
def search(pattern:str,text):
    # 简化为: 与其他模式匹配
    if pattern.startswith('^'):
        return match(pattern[1:],text)
    else:
        # [search] 'a'  => [match] '.*a'
        return match(f'.*{pattern}',text)
    #     return match(pattern[1:],text)
    # return match('.*'+pattern,text)

def match(pattern:str,text):
    # 1 匹配特殊字符情况
    # @2 剩下普通字符 是否匹配 其余部分
    if pattern == '':
        return True
    if pattern == '$':
        return (text == '')
    # a* a?
    if len(pattern) > 1 and pattern[1] in '*?':
        p,op,rest_p = pattern[0],pattern[1],pattern[2:]
        if op == '*':
            # 将p匹配任意次数,然后根据文本匹配模式
            return match_star(p,rest_p,text)
        if op == '?':
            # 匹配P,然后?后面部分匹配剩余文本
            if match1(p,text) and match(rest_p,text[1:]):
                return True
            else:
                # 匹配?后面部分匹配剩余文本
                return match(rest_p,text)
    # @2
    return (match1(pattern[0],text) and
            match(pattern[1:],text[1:]))

def match1(p,text):
    if not text:return False
    return p=='.' or p == text[0]

def match_star(p,pattern,text):
    # 将p匹配任意次数,
    # 0次
    # 多次
    # 然后根据文本匹配模式
    return (match(pattern,text) or
            (match1(p,text) and
             match_star(p,pattern,text[1:])))

def test():
    assert search('baa*!','Sheep said baaaa!')
    # assert search('baa*!','Sheep said baaaa humbug') == False
    # assert match('baa*!','Sheep said baaaa!') == False
    # assert match('baa*!','baaaa! said the sheep!')
    # assert search('def','abcdefg')
    # assert search('def$','abcdef')
    # assert search('def$','abcdefg') == False
    # assert search('^start','not the start') == False
    # assert match('start','not the start') == False
    # assert match('a*b*c','just anything')
    # assert match('x?','text')
    # assert match('text?','text')
    # assert match('text?','tex')
    print('test pass')


test()