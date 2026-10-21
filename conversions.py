separator = "----------------------------------------"

# 1. Konversi ke tipe data integer (bilangan bulat)
hasil_input = input("Masukkan sebuah angka bulat (contoh: 25): ")
angka = int(hasil_input)
print("Angka Anda ditambah 10 adalah:", angka + 10)
print("String dari", hasil_input, "dikonversi ke berbagai basis angka (radix):")
fmt = "Basis 10: {}\tBasis 2: {}\tBasis 8: {}\tBasis 16: {}"
# Catatan: int(str, base) mengonversi string dengan basis tertentu ke desimal (basis 10)
print(fmt.format(int(hasil_input), int(hasil_input, 2), int(hasil_input, 8), int(hasil_input, 16)))
print(separator)

# 2. Konversi ke tipe data float (pecahan/desimal)
nilai_desimal = input("Masukkan nilai desimal (contoh: 85.5): ")
jumlah_input = float(nilai_desimal) + float(hasil_input)
print(nilai_desimal, "+", hasil_input, "=", jumlah_input)
print(separator)

# 3. Konversi integer ke format string biner, oktal, dan heksadesimal
print(angka, "sebagai string dalam berbagai format basis:")
fmt = "Biner: {}\tOktal: {}\tHeksadesimal: {}"
print(fmt.format(bin(angka), oct(angka), hex(angka)))
print(separator)

# 4. Fungsi ord() dan chr() untuk karakter ASCII/Unicode
# ord() mengubah karakter menjadi kode angka, chr() sebaliknya
print('ord("A") =', ord("A"), '     chr(66) =', chr(66))
print(separator)

print("Total penjumlahan dari input adalah", jumlah_input)