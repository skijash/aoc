#!/usr/bin/env python3

import sys
import math


RESULT = 2020
numbers = None
numbers_in_reverse = None


def read_and_prepare(filename):
    """Reads the file input and splits it into two lists of ints.
    One is sorted ascending, other in reverse.
    """
    global numbers, numbers_in_reverse
    with open(filename, 'r') as file:
        input_content = file.read().strip().split('\n')
        numbers = sorted(
            [int(line) for line in input_content])
        numbers_in_reverse = sorted(numbers, reverse=True)


def sum_correct(numbers):
    num_sum = sum(numbers)
    if num_sum == RESULT:
        return True
    elif num_sum > RESULT:
        return False
    else:
        return None


def find_reverse(num_1):
    """
    Since this is iterating in reverse, while the sum is larger,
    we're continuing.
    The first time we hit a sum smaller than the result, we can return (None).
    If the result is found, we return the addend.
    """
    for num_2 in numbers_in_reverse:
        status = sum_correct((num_1, num_2))
        if status:
            return num_2
        elif status is False:
            continue

    return False if status is False else None


def find_2():
    for num_1 in numbers:
        num_2 = find_reverse(num_1)
        if num_2:
            return [num_1, num_2]


def find_3():
    for num_1 in numbers:
        for num_2 in numbers[numbers.index(num_1)+1:]:
            num_3 = find_reverse(num_1 + num_2)
            if num_3:
                return [num_1, num_2, num_3]
            elif num_3 is False:
                # the sum is larger than RESULT, iterating num_2 towards
                # larger numbers won't help, we can:
                break


if __name__ == '__main__':
    try:
        read_and_prepare(sys.argv[1])

        result_num = find_2()
        product = math.prod(result_num)
        print(f'Numbers: {result_num}\nProduct: {product}')

        result_num = find_3()
        product = math.prod(result_num)
        print(f'Numbers: {result_num}\nProduct: {product}')

    except IndexError:
        print('Expecting an input filename as an argument.')
