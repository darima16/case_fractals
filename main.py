"""Case-study#1 Fractals
Developers:
Rashidova A. (60%), Zhambaeva D. (55%), Ganbat S. (57%)
"""

from turtle import *
from rulocal import FRACTALS, SIZE, N


def kocha(n, size):
    """ Kocha curve """
    if n == 0:
        forward(size)
    else:
        kocha(n - 1, size / 3)
        left(60)
        kocha(n - 1, size / 3)
        right(120)
        kocha(n - 1, size / 3)
        left(60)
        kocha(n - 1, size / 3)


def snowflake_kocha(n, size):
    """ Kocha snowflake """
    kocha(n - 1, size)
    right(120)
    kocha(n - 1, size)
    right(120)
    kocha(n - 1, size)


def levi(n, size):
    """ Levi curve """
    if n == 0:
        forward(size)
    else:
        left(45)
        levi(n - 1, size)
        right(90)
        levi(n - 1, size)
        left(45)


def mink(n, size):
    """ Minkovski curve """
    if n == 0:
        forward(size)
    else:
        mink(n - 1, size / 3)
        left(90)
        mink(n - 1, size / 3)
        right(90)
        mink(n - 1, size / 3)
        right(90)
        mink(n - 1, size / 3)
        mink(n - 1, size / 3)
        left(90)
        mink(n - 1, size / 3)
        left(90)
        mink(n - 1, size / 3)
        right(90)
        mink(n - 1, size / 3)


def ice_1(n, size):
    """ Ice fractal #1 """
    if n == 0:
        forward(size)
    else:
        ice_1(n - 1, size / 2)
        left(90)
        ice_1(n - 1, size / 4)
        right(180)
        ice_1(n - 1, size / 4)
        left(90)
        ice_1(n - 1, size / 2)


def ice_2(n, size):
    """ Ice fractal #2 """
    if n == 0:
        forward(size)
    else:
        ice_2(n - 1, size / 2)
        left(120)
        ice_2(n - 1, size / 4)
        left(180)
        ice_2(n - 1, size / 4)
        left(120)
        ice_2(n - 1, size / 4)
        left(180)
        ice_2(n - 1, size / 4)
        left(120)
        ice_2(n - 1, size / 2)


def tree(n, size):
    """ Binary tree """
    if n == 0:
        return
    else:
        forward(size)
        right(30)
        tree(n - 1, size / 2)
        left(60)
        tree(n - 1, size / 2)
        right(30)
        backward(size)


def square(n, size):
    """ Square """
    if n == 0:
        return
    pendown()
    for _ in range(4):
        forward(size)
        right(90)
    penup()
    right(10)
    forward(0.1 * size)
    return square(n - 1, 0.9 * size)


def dragon(n, size, k):
    """ Dragon fractal """
    if n == 0:
        forward(size)
    else:
        if k == 1:
            left(45)
        else:
            right(45)
        dragon(n - 1, size / 2 ** 0.5, 1)
        if k == 1:
            right(90)
        else:
            left(90)
        dragon(n - 1, size / 2 ** 0.5, -1)
        if k == 1:
            left(45)
        else:
            right(45)


def main():
    """ Main function """
    f = int(input(FRACTALS))
    size = int(input(SIZE))
    n = int(input(N))
    up()
    goto(-200, 0)
    down()
    speed(0)
    if f == 1:
        kocha(n, size)
    elif f == 2:
        snowflake_kocha(n, size)
    elif f == 3:
        ice_1(n, size)
    elif f == 4:
        ice_2(n, size)
    elif f == 5:
        for i in range(1, 7):
            ice_1(n, size)
            right(180)
            ice_1(n, size)
            left(120)
    elif f == 6:
        for i in range(1, 7):
            ice_2(n, size)
            right(180)
            ice_2(n, size)
            left(120)
    elif f == 7:
        mink(n, size)
    elif f == 8:
        levi(n, size)
    elif f == 9:
        left(90)
        tree(n, size)
    elif f == 10:
        square(n, size)
    elif f == 11:
        dragon(n, size, 1)
    mainloop()


if __name__ == '__main__':
    main()
