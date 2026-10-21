separator = "----------------------------"

# 1. Pemformatan dengan Posisi Berurutan Default ({})
nama_format = "Depan: {} \tBelakang: {} \tInisial: {}"
hasil = nama_format.format("Budi", "Santoso", "S.")
print(hasil)
hasil = nama_format.format("Siti", "Rahma", "R.")
print(hasil)
print(separator)

# 2. Pemformatan dengan Mengubah Urutan Indeks ({1}, {0})
nama_terbalik = "{1},  {0}"
print(nama_terbalik.format("Depan", "Belakang"))
print(nama_terbalik.format("Budi", "Santoso"))
print(nama_terbalik.format("Siti", "Rahma"))
print(separator)

# 3. Pemformatan dengan Keyword Arguments (Nama Variabel Langsung)
dimensi = "Jenis: {jenis}\nTinggi:{tinggi}, Lebar:{lebar}"
hasil_dimensi = dimensi.format(tinggi=100, lebar=50, jenis="Kotak")
print(hasil_dimensi)