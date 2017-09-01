# -*- coding:utf-8 -*-

"解析装饰器的原理，本质上是闭包的应用"

__author__ = '建磊'

def decorator(func):

    def wrapper(*args,**kw):
        print('这里扩展func函数的功能')
        return func(*args,**kw)

    return wrapper

def demo1(tmp):
    print(tmp)

def demo2(tmp):
    print(tmp)

demo1 = decorator(demo1)

demo2 = decorator(demo2)

if __name__ == '__main__':
    demo1('我是demo1')
    demo2('我是demo2')
