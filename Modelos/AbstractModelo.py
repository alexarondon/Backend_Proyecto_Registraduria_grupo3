from abc import ABCMeta

class AbstractModelo(metaclass=ABCMeta):
    def __init__(self, data): #Constructor
        for llave, valor in data.items():
            setattr(self, llave, valor)