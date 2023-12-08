# [A] Write a function that returns the Nth number in the following sequence:
# 8, 15, 22, 29, 36, …
# For example:
# ● num_in_seq(1) = 8
# ● num_in_seq(2) = 15
# ● num_in_seq(3) = 22
# ● num_in_seq(4) = 29
# ● num_in_seq(5) = 36
# ● num_in_seq(10) = 71

def num_in_sequence(num):
    if num == 0:
        return 1
    return num_in_sequence(num - 1) + 7


if __name__ == '__main__':
    print(num_in_sequence(1))
    print(num_in_sequence(2))
    print(num_in_sequence(3))
    print(num_in_sequence(4))
    print(num_in_sequence(5))
    print(num_in_sequence(10))
