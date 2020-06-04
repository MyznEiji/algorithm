import math


"""
Input
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


Prime number
[2,3,5,7,11,13,17,19]

Non prime number
[1,4,6,8,9,10,12,14,15,16,18,20]

"""



def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def is_prime_v2(num: int) -> bool:
    """
    36 = 1 * 36
    36 = 2 * 18
    36 = 3 * 12
    36 = 4 * 9
    36 = 6 * 6 = √n
    36 = 9 * 4
    36 = 12 * 3
    36 = 18 * 2
    36 = 36 * 1
    """

    if num <= 1:
        return False

    # for i in range(2, math.floor(math.sqrt(num) + 1)):
    #     if num % i == 0:
    #         return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


if __name__ == '__main__':
    import time
    import random

    numbers = [random.randint(0, 1000) for _ in range(100000)]

    start = time.time()
    for num in numbers:
        is_prime_v1(num)
    print('v1', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print('v2', time.time() - start)
