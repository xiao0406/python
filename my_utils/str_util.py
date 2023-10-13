

def str_reverse(s):
    '''
    函数:str_reverse(s)，接受传入字符串，将字符串反转返回
    :param s:
    :return:
    '''
    return s[::-1]

def substr(s, x, y):
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("abcd"))

