
import pprint

class TreeStore:
    
    def __init__ ( self, items ):
        
        self.__items = { item [ 'id' ]: item for item in items }
    
    
    def getAll ( self ):
        
        return list ( self.__items. values () )
        
    
    def getItem ( self, item_id, default=None ):
        
        return self.__items.get ( item_id, default )
        
    
    def getChildren ( self, item_id ):
        
        return [ self.getItem ( item ) for item in self.__items if self.getItem ( item ) [ 'parent' ] == item_id ]
        
        
    def getAllParents ( self, item_id ):
        
        parent_id = self.getItem ( item_id, {} ).get ( 'parent' )
        
        if parent_id in [ 'root', None ]:
            result = []
        else:
            result = [ self.getItem ( parent_id ) ] + self.getAllParents ( parent_id )
        
        return result


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


#MAIN
def __main ():
    
    ts = TreeStore ( items )
    
    pprint.pprint ( ts.getAll () )
    
    assert ts.getItem ( 6 ) == {"id": 6, "parent": 2, "type": "test"}
    
    assert ts.getChildren ( 4 ) == [ {"id": 7, "parent": 4, "type": None},
                                     {"id": 8, "parent": 4, "type": None} ]
                                     
    assert ts.getAllParents ( 8 ) == [ {"id": 4, "parent": 2, "type": "test"},
                                       {"id": 2, "parent": 1, "type": "test"},
                                       {"id": 1, "parent": "root"} ]
    

if __name__ == '__main__':
    __main ()
