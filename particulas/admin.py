from .particula import Particula
import json

class Admin:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def mostar(self):
        for particula in self.__particulas:
            print(particula)
    
    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )
    
    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
    
    def __getitem__(self, key):
        return self.__particulas[key]

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=4)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                print(lista)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0