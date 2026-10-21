# 1. Operator Penggabungan String / Concatenation (+)
nama_depan = "Budi"
nama_belakang = "Santoso"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)  # Budi Santoso

# 2. Penggabungan String Otomatis (Tanpa Tanda +)
# Catatan: Python otomatis menyambung string berdampingan
nama_lengkap_2 = "Budi" " " "Santoso"
print(nama_lengkap_2)  # Budi Santoso

# 3. Operator Pengulangan / Asterisk (*)
bintang = "*" * 12
tagar = 5 * "#"
print(bintang, ":", tagar)  # ************ : #####

# 4. Operator Keanggotaan / Membership Operator (in)
# Digunakan untuk mengecek apakah suatu teks ada di dalam string lain
kalimat = "Halo selamat pagi"

# 'p' ada di kalimat? True
# 'pagi' ada di kalimat? True
# 'malam' ada di kalimat? False
print('p' in kalimat, 'pagi' in kalimat, 'malam' in kalimat)  
# Output: True True False