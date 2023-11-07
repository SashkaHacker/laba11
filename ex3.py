#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiplication():
    number = int(input())
    result = 1
    while number != 0:
        result *= number
        number = int(input())
    return result


if __name__ == '__main__':
    print(multiplication())
