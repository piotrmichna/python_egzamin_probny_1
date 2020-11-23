from random import randint


def roll(n, d, ad):
    dice_type = [2, 4, 6, 8, 10, 12, 100]
    if not d in dice_type:
        raise ValueError('No such dice!')

    result = ad
    for n in range(0, n):
        result += randint(1, d)

    return result


print(roll(2, 7, 20))
print(roll(3, 6, -3))
