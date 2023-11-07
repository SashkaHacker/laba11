#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test(number):
    if number >= 0:
        return positive()
    return negative()


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


if __name__ == "__main__":
    test(float(int(input())))
