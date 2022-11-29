
#MAIN

#Extract unique dataset names from collections list
def __extract_names ( collections_list: list [ str ] ) -> list:

        unique_names = set()

        #[O(1) for tuple.add] + [O(len(string) + len(delimiter)) = O(n)] + [O(1) for [0]] + [O(n) for cycle 'for'] = O(n^2)
        [ unique_names.add ( item.split ( '@' ) [ 0 ] ) for item in collections_list ]

        return list ( unique_names )            #O(n)


def __main() -> None:

        #Colletions have format 'dataset_name@dataset_id'
        collections_list = []
        if collections_list: assert __extract_names ( collections_list ) == []
        collections_list = [ 'ab@45' ]
        if collections_list: assert __extract_names ( collections_list ) == [ 'ab' ]
        collections_list = [ 'a._b@06', 'b_c@0' ]
        if collections_list: assert __extract_names ( collections_list ) == list ( set ( [ 'a._b', 'b_c' ]) )
        collections_list = [ 'p.@9', '.kl@2', '_b@04', 'al@0', '_b@04' ]
        if collections_list: assert __extract_names ( collections_list ) == list ( set ( [ 'p.', '_b', '.kl', 'al' ] ) )


if __name__ == '__main__':
        __main()


#Complexity Analysis
#Time Complexity: O(n^2)
#Space Complexity: O(1)
