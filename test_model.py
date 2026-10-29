from models.buku_model import BukuModel  # Perbaikan nama class (CamelCase)

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
# print("Menambahkan data buku...")
# model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
# print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

print("\n--- Mengubah Data Buku ID 5 ---")
model.update_buku(5, "Pemrograman Python MVC (Edisi Revisi)", "Guido van Rossum", 2024)
print("Data berhasil diubah!")

print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# 3. Menguji fungsi Delete (Menghapus buku)
print("\n--- Menghapus Buku ID 5 ---")
model.delete_buku(5)
print("Data berhasil dihapus!")

print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")