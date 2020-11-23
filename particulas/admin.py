from .particula import Particula
import json

class Admin:
    def __init__(self):
        self.__particulas = []
        self.__grafo = dict()

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def mostar(self):
        for particula in self.__particulas:
            print(particula)
    
    def __str__(self):
        return "".join (
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
    
    def ordenar(self, by, reversal:bool=False):
        self.__particulas.sort(key=by, reverse=reversal)
    
    def grafo(self):
        self.__grafo.clear()
        for particula in self.__particulas:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            
            if origen in self.__grafo:
                self.__grafo[origen].append((particula.destino_x, particula.destino_y, particula.distancia))
            else:
                self.__grafo[origen] = [(particula.destino_x, particula.destino_y, particula.distancia)]
            if destino in self.__grafo:
                self.__grafo[destino].append((particula.origen_x, particula.origen_y, particula.distancia))
            else:
                self.__grafo[destino] = [(particula.origen_x, particula.origen_y, particula.distancia)]

        return self.__grafo

        