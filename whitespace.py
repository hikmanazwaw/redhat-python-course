data = "\t  \nabc  def\t  \n"

# 1. strip() - Menghapus kiri dan kanan
result = data.strip()
print(len(data), ":", len(result))
print(repr(result))  # Menggunakan repr() agar karakter spasi/enter terlihat jelas

# 2. rstrip() - Menghapus kanan saja
result = data.rstrip()
print(len(data), ":", len(result))
print(repr(result))

# 3. lstrip() - Menghapus kiri saja
result = data.lstrip()
print(len(data), ":", len(result))
print(repr(result))