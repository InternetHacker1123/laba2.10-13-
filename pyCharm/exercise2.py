#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def harmonic_sr(*args):
    if args:
        number_of_arguments = len(args)
        count = 0
        for i in args:
            count += 1/i
        result = number_of_arguments/count 
        return result

    else:
        return None


if __name__ == "__main__":
    arguments = list(map(int, input("Введите аргументы: ").split()))
    result = harmonic_sr(*arguments)
    print(f"Среднее гармоническое равно: {result}")