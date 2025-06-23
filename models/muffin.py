from models.produk_roti import ProdukRoti
from interfaces.produksi_interface import ProduksiInterface
from interfaces.pengembangan_interface import PengembanganInterface

class Muffin(ProdukRoti, ProduksiInterface, PengembanganInterface):
    def produksi(self):
        return "Pengadonan -> Pengembangan -> Pemanggangan"

    def baking(self):
        return "Memanggang muffin"

    def packaging(self):
        return "Mengepak muffin"

    def labeling(self):
        return "Label muffin"

    def fermentasi(self):
        return "Mengembangkan adonan muffin"