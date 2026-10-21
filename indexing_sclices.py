kalimat = "Belajar Python"
pemisah = " | "

# 1. Indexing (Mengambil karakter berdasarkan posisi nomor indeksnya)
# Indeks positif dihitung dari depan (mulai dari 0), indeks negatif dari belakang (mulai dari -1)
print(kalimat[0], kalimat[8], kalimat[-1], kalimat[-6], sep=pemisah)
# Penjelasan:
# - kalimat[0]  -> 'B' (huruf pertama)
# - kalimat[8]  -> 'P' (huruf P pada kata Python)
# - kalimat[-1] -> 'n' (huruf terakhir)
# - kalimat[-6] -> 'P' (huruf P dihitung dari belakang)

# 2. Slicing (Memotong string dari indeks awal sampai sebelum indeks akhir)
# Format: [awal:akhir]
print(kalimat[0:7], kalimat[8:], kalimat[:7], sep=pemisah)
# Penjelasan:
# - kalimat[0:7]  -> 'Belajar' (indeks 0 sampai 6)
# - kalimat[8:]   -> 'Python' (dari indeks 8 sampai habis)
# - kalimat[:7]   -> 'Belajar' (dari awal sampai sebelum indeks 7)

# 3. Slicing dari Belakang (Menggunakan indeks negatif)
print(kalimat[-6:-1], kalimat[-6:], sep=pemisah)
# Penjelasan:
# - kalimat[-6:-1] -> 'Pytho' (dari indeks -6 sampai sebelum -1)
# - kalimat[-6:]   -> 'Python' (dari indeks -6 sampai habis)
print()

# 4. Extended Slicing (Menggunakan langkah/step: [awal:akhir:langkah])
alfabet = "abcdefghijklmnopqrstuvwxyz"

# Mengambil huruf dari indeks 2 sampai 18, dengan lompatan 3 huruf
print(alfabet[2:18:3])  # cfilor

# Mengambil semua huruf mulai dari indeks 18 sampai habis dengan langkah 1
mulai = 18
print(alfabet[mulai::1])  # 'stuvwxyz'

# Mengambil seluruh string dengan langkah 1 (menyalin string utuh)
print(alfabet[::1])  # 'abcdefghijklmnopqrstuvwxyz'