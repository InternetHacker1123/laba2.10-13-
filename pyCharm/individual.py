#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geometric_sr(*args):
    if args:
        cnt = 0
        result = 0
        for i in args:
            if i < 0:
                cnt += 1
                continue
            if cnt == 1:
                result += i
                continue
            if cnt == 2:
                break
        return result
    else:
        return None


if __name__ == "__main__":
    arguments = list(map(int, input("Введите аргументы: ").split()))
    result = geometric_sr(*arguments)
    print(f"Результат: {result}")