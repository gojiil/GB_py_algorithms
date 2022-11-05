"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for i in range(len(nums)):
        new_arr.append(i) if nums[i] % 2 == 0 else next
    return new_arr


def func_3(nums):
    return[x for x in range(len(nums)) if nums[x] % 2 == 0]


if __name__ == '__main__':
    NUMS = [i for i in range(10000)]
    print(timeit.timeit(setup='from __main__ import func_1',
                        stmt='func_1(NUMS[:])',
                        globals=globals(),
                        number=10000))
    print(timeit.timeit(setup='from __main__ import func_2',
                        stmt='func_2(NUMS[:])',
                        globals=globals(),
                        number=10000))
    print(timeit.timeit(setup='from __main__ import func_3',
                        stmt='func_3(NUMS[:])',
                        globals=globals(),
                        number=10000))
    
