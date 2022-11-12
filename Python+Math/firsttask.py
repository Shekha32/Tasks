
# 1. Дана функция (статический метод) на языке Java:

# static int myfunc(int[] a) {

#         int x = 0;

#         for (int i = 0; i < a.length; i++) {
#                 for (int j = i; j < a.length; j++) {
#                         if (a[j] != a[i]) {
#                                 if (j - i > x) {
#                                         x = j - i;
#                                 }
#                                 i = j - 1;
#                                 break;
#                         }
#                 }
#         }
#         return x;
# }

#[Q]: Что делает эта функция?
#[A]: Возвращает наибольшую длину непрерывной последовательности одинаковых элементов в заданном массиве.

#[Q]: Какая у неё алгоритмическая сложность (в среднем)?
#[A]: O(n * (n * (n+1))/2n) => O(n^2)

#[Q]: Есть ли в этой функции логические дефекты? Если да, то какие?
#[A]: Да.
#     1) Если массив состоит из одного элемента, то функция вернет 0 вместо 1;
#     2) Если массив состоит из всех одинаковых элементов, то функция вернет 0 вместо длины массива;
#     3) Если максимальная непрерывная последовательность одинаковых элементов находится в конце массива, функция возвращает некорректный ответ.

#[Q]: Можно ли как-то улучшить данный код? Если да, напишите улучшенный вариант.

#[A]:
#поиск наибольшей длины непрерывной последовательности одинаковых элементов в заданном массиве
def __max_len_same_elem ( mas ) -> int:

        max = 0
        count = 1
        length = len ( mas )                            #O(1)

        if length == 0:                                 #O(1)
                count = 0

        else:
                previous = mas [ 0 ]                    #O(1)

                for n in range ( 1, length ):           #O(n-1)

                        if mas [ n ] == previous:       #O(1)
                                count += 1
                        else:
                                if count > max:         #O(1)
                                        max = count

                                count = 1
                                previous = mas [ n ]    #O(1)

        return max if max > count else count            #O(1)        the only exit from the function


def __main():

        assert ( __max_len_same_elem ( [] ) ) == 0
        assert ( __max_len_same_elem ( [ 1 ] ) ) == 1
        assert ( __max_len_same_elem ( [ 1, 2, 3 ] ) ) == 1
        assert ( __max_len_same_elem ( [ 1, 2, 1, 1, 1, 3, 3] ) ) == 3
        assert ( __max_len_same_elem ( [ 6, 6, 6, 0, 9 ] ) ) == 3
        assert ( __max_len_same_elem ( [ 6, 7, 6, 0, 0, 0, 0 ] ) ) == 4
        print (  'All tests successfully passed!' )


if __name__ == '__main__':
        __main()


#[Q]: Какая алгоритмическая сложность у вашего варианта?
#[A]: O(n)
