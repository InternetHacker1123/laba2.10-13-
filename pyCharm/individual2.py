#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(*args):
    if args:
        return args
    else:
        return None


if __name__ == "__main__":
    arguments = list(map(str, input("Введите дела: ").split()))
    result = func(*arguments)
    for i, item in enumerate(result):
        print(f"Дело {i}: {item}")    