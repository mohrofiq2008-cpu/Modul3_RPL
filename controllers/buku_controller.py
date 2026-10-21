
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self):
        self.model = BukuModel()
        self.view = BukuView()

        # Menghubungkan tombol Simpan Data dengan Controller
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        # Memuat data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data buku dari database
        data_buku = self.model.get_all_buku()

        # Menampilkan nomor ID berurutan pada GUI
        for nomor, buku in enumerate(data_buku, start=1):
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    nomor,
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def simpan_data(self):
        # Mengambil data dari form
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Memeriksa form kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Memastikan tahun berupa angka
        try:
            tahun = int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        # Menyimpan data melalui Model
        berhasil = self.model.create_buku(
            judul,
            penulis,
            tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            # Membersihkan form setelah berhasil
            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

            # Memuat ulang tabel
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat menyimpan data."
            )

    # Menjalankan aplikasi
    def run(self):
        self.view.mainloop()