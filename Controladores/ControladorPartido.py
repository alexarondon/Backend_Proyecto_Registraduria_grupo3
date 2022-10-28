from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self): #Constructor
        print("Creando ControladorPartido")
        self.repositorioPartido = RepositorioPartido()

    def index(self):  #Funcion listar
        return self.repositorioPartido.findAll()

    def create(self, infoPartido): #Funcion crear
        partido = Partido(infoPartido)
        return self.repositorioPartido.save(partido)

    def update(self, id, infoPartido):
        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)

    def show(self, id):
        partido = Partido(self.repositorioPartido.findById(id))
        return partido.__dict__