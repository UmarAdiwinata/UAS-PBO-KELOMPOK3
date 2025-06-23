from models.roti_manis import RotiManis
from models.croissant import Croissant
from models.muffin import Muffin
from models.butter_cookies import ButterCookies
from services.kalkulator_profit import estimasi_profit
from utils.simulasi_produksi import simulasikan_produksi

produk_list = [
    RotiManis("Roti Coklat", "RM01", {"Tepung": "500g", "Coklat": "100g"}, 10000, 15000),
    Croissant("Croissant Keju", "CR02", {"Tepung": "600g", "Keju": "100g"}, 12000, 17000),
    Muffin("Muffin Pisang", "MF03", {"Tepung": "400g", "Pisang": "150g"}, 8000, 13000),
    ButterCookies("Butter Cookies", "BC04", {"Tepung": "300g", "Butter": "200g"}, 9000, 14000)
]

def tampilkan_menu():
    while True:
        print("\n=== HANARI BAKERY SYSTEM ===")
        print("1. Tampilkan semua produk")
        print("2. Estimasi profit")
        print("3. Simulasi proses produksi")
        print("4. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            for p in produk_list:
                print(f"{p.nama} (Kode: {p.kode}) - Harga: {p.harga_jual} - Biaya: {p.biaya_produksi}")

        elif pilih == "2":
            kode = input("Masukkan kode produk: ")
            jumlah = int(input("Masukkan jumlah pcs: "))
            produk = next((p for p in produk_list if p.kode == kode), None)
            if produk:
                print("Estimasi Profit:", estimasi_profit(produk, jumlah))
            else:
                print("Produk tidak ditemukan.")

        elif pilih == "3":
            kode = input("Masukkan kode produk: ")
            produk = next((p for p in produk_list if p.kode == kode), None)
            if produk:
                print(simulasikan_produksi(produk))
            else:
                print("Produk tidak ditemukan.")

        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid.")

tampilkan_menu()