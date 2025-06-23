from models.produk_roti import ProdukRoti
from interfaces.produksi_interface import ProduksiInterface
from interfaces.pengembangan_interface import PengembanganInterface

class RotiManis(ProdukRoti, ProduksiInterface, PengembanganInterface):
    def produksi(self):
        return "Pengadonan -> Pengembangan -> Pemanggangan"

    def baking(self):
        return "Memanggang roti manis"

    def packaging(self):
        return "Mengepak roti manis"

    def labeling(self):
        return "Label roti manis"

    def fermentasi(self):
        return "Mengembangkan adonan roti manis"