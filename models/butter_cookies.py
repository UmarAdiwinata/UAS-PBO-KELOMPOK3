from models.produk_roti import ProdukRoti
from interfaces.produksi_interface import ProduksiInterface

class ButterCookies(ProdukRoti, ProduksiInterface):
    def produksi(self):
        return "Pengadonan -> Pemanggangan -> Topping"

    def baking(self):
        return "Memanggang butter cookies"

    def packaging(self):
        return "Mengepak butter cookies"

    def labeling(self):
        return "Label butter cookies"