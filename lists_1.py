# 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом.

def filter_out_second_list_1(first: list, second: list) -> list:
    # Самое простое, но и низкоэффективное решение
    # Сложность порядка O(N*M), где N и M длины списков.
    return [x for x in first if x not in second]


def filter_out_second_list_2(first: list, second: list) -> list:
    # Чтобы ускорить алгоритм, нужно понимать, какого типа данные могут быть в списках
    # Например, если предположить, что элементы второго списка хешируемы,
    #   можно предложить решение со сложностью порядка O(M) + O(N) = O(max(N,M)),
    #   но на самом деле медленнее из-за возможных коллизий в хеш-таблице
    # Ну и расход памяти тут больше, O(M)
    second_set = set(second)
    return [x for x in first if x not in second_set]


for method in filter_out_second_list_1, filter_out_second_list_2:
    assert method([1, 2, 2, 2, 3], [2, 10, 15]) == [1, 3]
    assert method([1, 1, 1], []) == [1, 1, 1]
    assert method([1, 1, 1], [1, 2, 3, 1, 1]) == []
