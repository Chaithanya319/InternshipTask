# Problem 18: Set Mutations
# HackerRank: https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == '__main__':
    n = int(input())
    set_a = set(map(int, input().split()))

    number_of_operations = int(input())

    for _ in range(number_of_operations):
        operation, _ = input().split()
        other_set = set(map(int, input().split()))

        if operation == 'intersection_update':
            set_a.intersection_update(other_set)
        elif operation == 'update':
            set_a.update(other_set)
        elif operation == 'symmetric_difference_update':
            set_a.symmetric_difference_update(other_set)
        elif operation == 'difference_update':
            set_a.difference_update(other_set)

    print(sum(set_a))
