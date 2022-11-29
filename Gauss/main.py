
#MAIN

#search for a missing element in an array
def __find_missing ( mas: list ) -> int:

        length = len ( mas ) + 1                        #length of the original array with all elements         #O(1)
        total_sum = ( length + 1 ) * ( length / 2 )     #Gauss formula: sum of numbers from 1 to N              #O(1)

        return int ( total_sum - sum ( mas ) )          #this difference will be equal to the lost number       #O(n)


def __main():

        assert __find_missing ( [ 1, 3 ] ) == 2
        assert __find_missing ( [ 1, 2, 4, 5 ] ) == 3
        assert __find_missing ( [ 1, 2, 3 ] ) == 4
        assert __find_missing ( [ 2, 3, 4, 5 ] ) == 1


if __name__ == '__main__':
        __main()
