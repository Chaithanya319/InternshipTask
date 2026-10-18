# Problem 19: Company Logo
# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

if __name__ == '__main__':
    s = input().strip()

    frequency = Counter(s)

    for char, count in sorted(
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    )[:3]:
        print(char, count)
