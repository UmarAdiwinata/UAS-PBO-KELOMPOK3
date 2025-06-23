from models.produk_roti import ProdukRoti
from interfaces.produksi_interface import ProduksiInterface
from interfaces.pengembangan_interface import PengembanganInterface

class Croissant(ProdukRoti, ProduksiInterface, PengembanganInterface):
    def produksi(self):
        return "Pengadonan -> Pengembangan -> Pemanggangan"

    def baking(self):
        return "Memanggang croissant"

    def packaging(self):
        return "Mengepak croissant"

    def labeling(self):
        return "Label croissant"

    def fermentasi(self):
        return "Mengembangkan adonan croissant"