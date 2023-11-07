#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    return input()


def test_input(string):
    try:
        if int(string):
            return True
    except ValueError:
        return False


def str_to_int(number):
    return int(number)


def print_int(number):
    print(number)


if __name__ == '__main__':
    result1 = get_input()
    if test_input(result1):
        result2 = str_to_int(result1)
        print_int(result2)
    else:
        print('Введенное значение не является числом.')
