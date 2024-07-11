from sequencia import Sequencia

class OrganismoFasta:
    def __init__(self, id, nome, sequencia):
        self.id = id
        self.nome = nome
        self.sequencia = Sequencia(sequencia)

    def mostrar_atributos(self):
            print(f"ID: {self.id}, Nome: {self.nome}, Sequencia: {self.sequencia}")

