from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self, infoCandidato):
        candidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(candidato)
    def update(self, id, infoCandidato): #update de varios campos
        candidato = Candidato(self.repositorioCandidato.findById(id))
        candidato.cedula = infoCandidato['cedula']
        candidato.numero_resolucion = infoCandidato['numero_resolucion']
        candidato.nombre = infoCandidato['nombre']
        candidato.apellido = infoCandidato['apellido']
        return self.repositorioCandidato.save(candidato)
    def delete(self, id):
        return self.repositorioCandidato.delete(id)
    def show(self, id):
        candidato = Candidato(self.repositorioCandidato.findById(id))
        return candidato.__dict__
    def setPartido(self, id_candidato, id_partido):
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        partido = Partido(self.repositorioPartido.findById(id_partido))
        candidato.partido = partido
        return self.repositorioCandidato.save(candidato)