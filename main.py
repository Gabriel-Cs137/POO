class veiculo:
    def __init__(self,marca,modelo,cor,ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def acelerar(self):

        print(f'A moto {self.modelo} de cor {self.cor} acelerou a {self.ano}km por hora')


class  moto(veiculo):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)
        self.guidao = True

class  carro(veiculo):
    def __init__(self, marca, modelo, cor, ano,porta):
        super().__init__(marca, modelo, cor, ano)
        self.portas = porta
 
fusca = carro('WolksWagen','Fusca','Azul',1945,2)
cb300 = moto('Honda','CB 300','Vermelha',2016)
 
cb300.acelerar()

fusca.acelerar()