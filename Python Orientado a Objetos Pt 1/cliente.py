class Cliente:
    
    def __init__(self,nome):
        self._nome = nome
        
    @property
    
    def nome(self):
        print("chamando @property name()")
        return self._nome.title()
    
    @nome.setter
    def nome(self, nome):
        print("chamando @property setter name()")
        self.__nome = nome
    