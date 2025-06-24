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

def tambah_produk():
    print("\n== Tambah Produk Baru ==")
    print("1. Roti Manis")
    print("2. Croissant")
    print("3. Muffin")
    print("4. Butter Cookies")
    jenis = input("Pilih jenis produk: ")

    nama = input("Nama produk: ")
    kode = input("Kode produk: ")
    bahan_input = input("Bahan baku (format: Tepung:500g,Gula:100g): ")
    bahan_baku = {}
    try:
        for item in bahan_input.split(","):
            key, val = item.split(":")
            bahan_baku[key.strip()] = val.strip()
    except:
        print("Format bahan salah. Gunakan format Tepung:500g,Gula:100g")
        return

    try:
        biaya = int(input("Biaya produksi per-n pcs: "))
        harga = int(input("Harga jual per-n pcs: "))
    except ValueError:
        print("Masukkan biaya dan harga dalam angka.")
        return

    if jenis == "1":
        produk = RotiManis(nama, kode, bahan_baku, biaya, harga)
    elif jenis == "2":
        produk = Croissant(nama, kode, bahan_baku, biaya, harga)
    elif jenis == "3":
        produk = Muffin(nama, kode, bahan_baku, biaya, harga)
    elif jenis == "4":
        produk = ButterCookies(nama, kode, bahan_baku, biaya, harga)
    else:
        print("Jenis tidak valid.")
        return

    produk_list.append(produk)
    print("Produk berhasil ditambahkan.")

def tampilkan_menu():
    while True:
        print("\n=== HANARI BAKERY SYSTEM ===")
        print("1. Tampilkan semua produk")
        print("2. Estimasi profit")
        print("3. Simulasi proses produksi")
        print("4. Tambah produk baru")
        print("5. Keluar")
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
            tambah_produk()

        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid.")

tampilkan_menu()