def like(numbers: str, a_set: str, b_set: str):
    likes = 0
    numbers, a_set, b_set = numbers.split(' '), a_set.split(' '), b_set.split(' ')
    for i in numbers:
        if i in a_set and i not in b_set:
            likes += 1
        elif i in b_set and i not in a_set:
            likes -= 1
    return likes

numbers = '3 2 10 7 5 5 2 1 2'
a = '2 3 7'
b = '5 10 7'
print(like(numbers, a, b))

numbers = '1 4 10 20 1 11 12'
a = '1 4 1 12'
b = '1 12 10 20'
print(like(numbers, a, b))


def fine_print(n: int):
    for i in range(n):
        print('%-10d %-10o %-10x %-10s' % (i,i,i,bin(i)))

fine_print(20)