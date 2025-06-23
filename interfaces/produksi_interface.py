from abc import ABC, abstractmethod

class ProduksiInterface(ABC):
    @abstractmethod
    def baking(self): pass

    @abstractmethod
    def packaging(self): pass

    @abstractmethod
    def labeling(self): pass