
#[Q]: 5. Напишите функцию, которая принимает на вход массив строк, и возвращает такой же массив,
#но без тех строк, которых в исходном массиве было чётное количество.
#Оставшиеся в массиве элементы должны идти в том же порядке друг относительно друга, что и в первоначальном массиве.
#Решение должно быть оптимизировано по скорости работы.
#Писать можно на любом из популярных высокоуровневых языков программирования (выбранный язык нужно указать).

#[A]:
#удаление элементов с четным количеством повторов
def __del_even_counted_elem ( mas ) -> list [ str ]:

        d = {}

        for n in mas:                                                   #O(n)
                if n in d.keys():                                       #O(1)
                        d [ n ] = not d [ n ]                           #O(1)
                else:
                        d [ n ] = False                                 #O(1)

        oddelem = [ None ] * len ( mas )                                #O(n)

        for n in range ( len ( mas ) ):                                 #O(n)
                if not d [ mas [ n ] ]:                                 #O(1)
                        oddelem [ n ] = mas [ n ]                       #O(1)

        return [ elem for elem in oddelem if elem is not None ]         #O(n)


def __main():

        assert ( __del_even_counted_elem ( [] ) ) == []
        assert ( __del_even_counted_elem ( [ '1' ] ) ) == [ '1' ]
        assert ( __del_even_counted_elem ( [ '1', '2', '1' ] ) ) == [ '2' ]
        assert ( __del_even_counted_elem ( [ '1', '2', '1', '1', '1', '3', '3' ] ) ) == [ '2' ]
        assert ( __del_even_counted_elem ( [ '6', '6', '6', '0', '9' ] ) ) == [ '6', '6', '6', '0', '9' ]
        assert ( __del_even_counted_elem ( [ '6', '6', '7', '9', '0', '0', '0', '0' ] ) ) == [ '7', '9' ]
        print (  'All tests successfully passed!' )


if __name__ == '__main__':
        __main()


#[Q]: Оцените алгоритмическую сложность своей реализации.
#[A]: O(4n) => O(n)
