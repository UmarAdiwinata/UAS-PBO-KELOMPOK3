def simulasikan_produksi(produk):
    proses = produk.produksi()
    return f"Proses Produksi: {proses}\n" + \
           f"{produk.baking()}\n{produk.packaging()}\n{produk.labeling()}"