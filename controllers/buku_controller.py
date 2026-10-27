import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        self.model = BukuModel()
        self.view = BukuView()

        # Menghubungkan tombol dengan Controller
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        self.view.btn_hapus.configure(
            command=self.hapus_data
        )

        self.view.btn_perbarui.configure(
            command=self.perbarui_data
        )

        # Mengisi form otomatis saat baris buku dipilih
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # Memuat data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data buku dari database
        data_buku = self.model.get_all_buku()

        # Nomor tampilan berurutan, ID asli disimpan di iid
        for nomor, buku in enumerate(data_buku, start=1):
            self.view.tabel.insert(
                "",
                "end",
                iid=str(buku["id_buku"]),
                values=(
                    nomor,
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def pilih_data(self, event=None):
        # Memeriksa baris yang dipilih
        selected = self.view.tabel.selection()

        if not selected:
            return

        item = selected[0]
        values = self.view.tabel.item(item, "values")

        if not values:
            messagebox.showerror(
                "Error",
                "Data buku yang dipilih tidak ditemukan."
            )
            return

        # Mengambil data dari baris tabel
        # values[0] = nomor urut
        # values[1] = judul
        # values[2] = penulis
        # values[3] = tahun terbit
        judul = values[1]
        penulis = values[2]
        tahun = values[3]

        # Mengisi form judul buku
        self.view.entry_judul.delete(0, "end")
        self.view.entry_judul.insert(0, judul)

        # Mengisi form nama penulis
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_penulis.insert(0, penulis)

        # Mengisi form tahun terbit
        self.view.entry_tahun.delete(0, "end")
        self.view.entry_tahun.insert(0, tahun)

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

            # Membersihkan form
            self.bersihkan_form()

            # Memuat ulang tabel
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat menyimpan data."
            )

    def hapus_data(self):
        # Memeriksa baris yang dipilih
        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin dihapus!"
            )
            return

        # Mengambil baris yang dipilih
        item = selected[0]
        values = self.view.tabel.item(item, "values")

        if not values:
            messagebox.showerror(
                "Error",
                "Data buku yang dipilih tidak ditemukan."
            )
            return

        # Mengambil ID asli dari iid, bukan nomor urut
        id_buku = int(item)

        # Konfirmasi penghapusan
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"Apakah Anda yakin ingin menghapus buku "
            f"dengan ID {id_buku}?"
        )

        if not konfirmasi:
            return

        # Menghapus data melalui Model
        berhasil = self.model.delete_buku(id_buku)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )

            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Gagal",
                "Data buku gagal dihapus. "
                "Periksa ID, koneksi database, atau "
                "relasi peminjaman buku."
            )

    def perbarui_data(self):
        # Memeriksa baris yang dipilih
        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin diperbarui!"
            )
            return

        # Mengambil baris yang dipilih
        item = selected[0]
        values = self.view.tabel.item(item, "values")

        if not values:
            messagebox.showerror(
                "Error",
                "Data buku yang dipilih tidak ditemukan."
            )
            return

        # Mengambil ID asli dari iid
        id_buku = int(item)

        # Mengambil data baru dari form
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

        # Memperbarui data melalui Model
        berhasil = self.model.update_buku(
            id_buku,
            judul,
            penulis,
            tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )

            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data buku gagal diperbarui. "
                "Periksa koneksi database dan fungsi "
                "update_buku() pada BukuModel."
            )

    def bersihkan_form(self):
        # Membersihkan seluruh kolom form
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

        # Menghapus pilihan baris pada tabel
        selected = self.view.tabel.selection()

        if selected:
            self.view.tabel.selection_remove(*selected)

    # Menjalankan aplikasi
    def run(self):
        self.view.mainloop()