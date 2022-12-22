#teste

class Teste:
    def __init__(self, teste):
        self.teste = teste
    
    def i(self):
        return self.teste

instance = Teste('teste')
print(instance.i())
