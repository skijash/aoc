#!/usr/bin/env python3

import sys

# using a list of dicts because there are duplicate passwords in the input
passwords = []


def read_and_prepare(filename):
    global passwords
    with open(filename, 'r') as file:
        passwd_list = file.read().strip().split('\n')
        for p in passwd_list:
            rule, passwd = p.split(': ')
            range_, letter = rule.split(' ')
            range_ = [int(r) for r in range_.split('-')]
            passwords.append({
                'passwd': passwd,
                'range_': range_,
                'letter': letter
            })
    print('Total:', len(passwords))


def validate_1(passwd, letter, range_):
    # sorted() returns a list of characters in the string, sorted.
    p_list = sorted(passwd)
    count = p_list.count(letter)
    return range_[0] <= count <= range_[1]


def validate_2(passwd, letter, range_):
    return (passwd[range_[0]-1] == letter) ^ \
           (passwd[range_[1]-1] == letter)


def check_passwords():
    cnt_1 = 0
    cnt_2 = 0
    for passwd in passwords:
        if validate_1(**passwd):
            cnt_1 += 1
        if validate_2(**passwd):
            cnt_2 += 1

    print(f'Validate 1/2: {cnt_1} / {cnt_2}')


if __name__ == '__main__':
    try:
        read_and_prepare(sys.argv[1])
        check_passwords()

    except IndexError:
        print('Expecting an input filename as an argument.')
