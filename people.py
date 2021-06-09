class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta
        