"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

my_array = [1, 3, 1, 3, 4, 5, 1]


def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):
    i = max(set(array), key=array.count)
    return f'Чаще всего встречается число {i}, '\
           f'оно появилось в массиве {array.count(i)} раз(а)'


if __name__ == '__main__':
    print(func_1(my_array))
    print(timeit(stmt='func_1(my_array)',
                 globals=globals(),
                 number=10000))
    print(func_2(my_array))
    print(timeit(stmt='func_2(my_array)',
                 globals=globals(),
                 number=10000))
    print(func_3(my_array))
    print(timeit(stmt='func_3(my_array)',
                 globals=globals(),
                 number=10000))
