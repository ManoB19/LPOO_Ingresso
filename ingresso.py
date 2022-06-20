class Ingresso:
    def __init__(self, valor):
        self.valor = valor
        
    def getValor(self):
        return self.valor
    
    def setValor(self, custo):
        self.custo = custo

class IngressoVip(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor,)
        self.adicional = adicional
     
    def getAdicional(self):
        return self.adicional + self.valor
    
    
    def setAdicional(self, vip1):
        self.adicional = vip1