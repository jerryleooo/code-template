# -*- coding: utf-8 -*-

def fib(n):
    a, b, i = 1, 1, 2
    while i < n:
        a, b, i = a + b, a, i + 1
    return a

print fib(10)