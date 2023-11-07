#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import pi


def cylinder(radius, height):
    command = input('Напишите, что хотите получить: "Площадь боковой'
                    'поверхности" или "Полная площадь": ')
    match command:
        case "Площадь боковой поверхности":
            return 2 * pi * radius * height
        case "Полная площадь":
            return 2 * circle(radius) + 2 * pi * radius * height


def circle(radius):
    return pi * radius ** 2


if __name__ == "__main__":
    cylinder(float(input("Введите радиус:")), float(input("Введите высоту:")))
    