# 2. Дан массив целых чисел. Нужно удалить из него нули.
# Можно использовать только О(1) дополнительной памяти.

def remove_zeroes(input_list: list) -> list:
    i = len(input_list) - 1
    while i >= 0:
        if input_list[i] == 0:
            del input_list[i]

        i -= 1

    return input_list


assert remove_zeroes([1]) == [1]
assert remove_zeroes([]) == []
assert remove_zeroes([0, 0, 0, 0]) == []
assert remove_zeroes([0, 0, 1, 0, 2]) == [1, 2]
assert remove_zeroes([0, 1, 0]) == [1]
assert remove_zeroes([1, 1, 2, 0, 0]) == [1, 1, 2]
