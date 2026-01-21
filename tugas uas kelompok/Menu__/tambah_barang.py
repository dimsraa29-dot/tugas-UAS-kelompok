def tambah_barang():
    os.system("cls")
    tampil_produk()
    idp = int(input("ID Produk: "))
    qty = int(input("Qty: "))

    for p in produk:
        if p["id"] == idp:
            if qty > p["stok"]:
                input("Stok tidak cukup! ENTER...")
                return
            keranjang.append({
                "id":idp,"nama":p["nama"],
                "harga":p["harga"],
                "qty":qty,"subtotal":p["harga"]*qty
            })
            input("Masuk keranjang! ENTER...")
            return
