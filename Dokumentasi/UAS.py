def input_pembelian(daftar_harga):
    items = []
    while True:
        # Menampilkan daftar barang
        print("Daftar Barang:")
        for index, (nama_barang, harga) in enumerate(daftar_harga.items(), start=1):
            print(f"{index}. {nama_barang} (Rp {harga:,.2f})")

        # Meminta pengguna untuk memilih barang
        pilihan = input("Pilih nomor barang (0 untuk selesai): ")
        
        if pilihan == '0':
            break

        try:
            index_barang = int(pilihan) - 1
            nama_barang = list(daftar_harga.keys())[index_barang]
        except (ValueError, IndexError):
            print("Input tidak valid. Silakan pilih nomor barang yang sesuai.")
            continue

        jumlah = int(input("Masukkan jumlah barang yang dibeli: "))
        items.append((nama_barang, daftar_harga[nama_barang], jumlah))
    
    return items

def generate_struk(items, uang_pembayaran):
    total_harga = sum(harga * jumlah for _, harga, jumlah in items)
    
    # Menampilkan header struk
    struk = "====================== STRUK BELANJA =======================\n"

    # Menampilkan detail pembelian
    struk += "{:<20} {:<10} {:<15} {:<15}\n".format("Nama Barang", "Jumlah", "Harga Satuan", "Subtotal")
    struk += "=" * 60 + "\n"
    for nama_barang, harga, jumlah in items:
        subtotal = harga * jumlah
        struk += "\n"
        struk += "{:<20} {:<10} {:<15,.2f} {:<15,.2f}\n".format(nama_barang, jumlah, harga, subtotal)

    # Jarak
    struk += "\n"

    # Menampilkan total harga
    struk += "=" * 60 + "\n"
    struk += "Total Harga: {:<45,.2f}\n".format(total_harga)

    # Menampilkan jumlah uang pembayaran
    struk += "Uang Pembayaran: {:<40,.2f}\n".format(uang_pembayaran)

    # Menghitung kembalian atau sisa uang
    kembalian = uang_pembayaran - total_harga

    # Menampilkan kembalian atau sisa uang
    struk += "Kembalian: {:<45,.2f}\n".format(kembalian)

    # Menampilkan footer struk
    struk += "=" * 60 + "\n"
    
    return struk

# Daftar harga yang sudah ditentukan di dalam kodingan
daftar_harga = {
    "ES Teh": 8000,
    "ES Jeruk": 10000,
    "Teh Panas": 5000,
    "Jeruk Panas": 8000,
    "Kopi Panas": 5000,
}

# Input manual pembelian
pembelian = input_pembelian(daftar_harga)

# Input manual jumlah uang pembayaran
uang_pembayaran = float(input("Masukkan jumlah uang: "))

# Menampilkan struk belanja
if pembelian:
    struk_belanja = generate_struk(pembelian, uang_pembayaran)
    print(struk_belanja)
else:
    print("Tidak ada pembelian.")
