"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

"""
Самая быстрая реализация - строчный переворот. 
Происходит это потому что нет необходимости производить вычисления.
Ускорить третью функцию можно избавившись от лишних присваиваний, 
сразу возвращая результат.
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return str(enter_num)[::-1]


if __name__ == '__main__':
    print(revers(123456789))
    print(timeit(stmt='revers(123456789)',
                 globals=globals(),
                 number=10000))
    print(revers_2(123456789))
    print(timeit(stmt='revers_2(123456789)',
                 globals=globals(),
                 number=10000))
    print(revers_3(123456789))
    print(timeit(stmt='revers_3(123456789)',
                 globals=globals(),
                 number=10000))
    print(revers_4(123456789))
    print(timeit(stmt='revers_4(123456789)',
                 globals=globals(),
                 number=10000))

