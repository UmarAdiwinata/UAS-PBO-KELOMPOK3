from abc import ABC, abstractmethod

class ProdukRoti(ABC):
    def __init__(self, nama, kode, bahan_baku, biaya_produksi, harga_jual):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual

    def hitung_profit(self, jumlah):
        return (self.harga_jual - self.biaya_produksi) * jumlah

    @abstractmethod
    def produksi(self): pass