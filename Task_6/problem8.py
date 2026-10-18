# Problem 8: Tuples
# HackerRank: https://www.hackerrank.com/challenges/python-tuples/problem

def legacy_tuple_hash(values):
    x = 0x345678
    mult = 1000003
    mask = (1 << 64) - 1

    for i, value in enumerate(values):
        remaining = len(values) - i - 1

        if value < 0:
            value = -((-value) % 2305843009213693951)
        else:
            value %= 2305843009213693951

        if value == -1:
            value = -2

        x = ((x ^ value) * mult) & mask
        mult += 82520 + remaining + remaining

    x = (x + 97531) & mask

    if x >= (1 << 63):
        x -= (1 << 64)

    if x == -1:
        x = -2

    return x


if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))

    print(legacy_tuple_hash(integer_list))
