#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def geometric_sr(*args):
    if args:
        number_of_arguments = len(args)
        count = 1
        for i in args:
            count *= i

        result = math.pow(count, 1 / number_of_arguments)
        return result

    else:
        return None


if __name__ == "__main__":
    arguments = list(map(int, input("Введите аргументы: ").split()))
    result = geometric_sr(*arguments)
    print(f"Среднее геометрическое равно: "
          f"{result}")