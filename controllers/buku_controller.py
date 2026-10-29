
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota", on_logout=None):
        self.user_role = user_role
        self.on_logout = on_logout

        self.model = BukuModel()
        self.view = BukuView()

        # =====================================
        # KONFIGURASI JUDUL JENDELA
        # =====================================
        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: "
            f"{self.user_role.upper()}"
        )

        # =====================================
        # MENGHUBUNGKAN TOMBOL DENGAN FUNGSI
        # =====================================
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        self.view.btn_perbarui.configure(
            command=self.perbarui_data
        )

        self.view.btn_hapus.configure(
            command=self.hapus_data
        )

        self.view.btn_logout.configure(
            command=self.logout
        )

        # Menghubungkan pemilihan baris tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # =====================================
        # PEMBATASAN AKSES ANGGOTA
        # =====================================
        if self.user_role != "admin":
            # Tombol simpan khusus admin
            self.view.btn_simpan.configure(
                state="disabled",
                text="Khusus Admin"
            )

            # Tombol perbarui terkunci
            self.view.btn_perbarui.configure(
                state="disabled",
                text="Perbarui Data (Terkunci)"
            )

            # Tombol hapus terkunci
            self.view.btn_hapus.configure(
                state="disabled",
                text="Hapus Data (Terkunci)"
            )

            # Formulir tidak dapat diubah oleh anggota
            self.view.entry_judul.configure(
                state="disabled"
            )

            self.view.entry_penulis.configure(
                state="disabled"
            )

            self.view.entry_tahun.configure(
                state="disabled"
            )

        # Memuat data buku saat halaman dibuka
        self.muat_data_tabel()

    # =====================================
    # MEMUAT DATA BUKU KE TABEL
    # =====================================
    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for index, buku in enumerate(data_buku, start=1):
            # ID asli database digunakan sebagai iid.
            # Nomor urut hanya untuk tampilan tabel.
            id_buku = str(buku["id_buku"])

            self.view.tabel.insert(
                "",
                "end",
                iid=id_buku,
                values=(
                    index,
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    # =====================================
    # MENGOSONGKAN FORMULIR
    # =====================================
    def kosongkan_form(self):
        if self.user_role != "admin":
            return

        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

        for item in self.view.tabel.selection():
            self.view.tabel.selection_remove(item)

    # =====================================
    # MEMILIH DATA BUKU
    # =====================================
    def pilih_data(self, event=None):
        selected = self.view.tabel.selection()

        if not selected:
            return

        item = selected[0]

        values = self.view.tabel.item(
            item,
            "values"
        )

        if not values:
            return

        # Anggota hanya dapat melihat data buku.
        if self.user_role != "admin":
            return

        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

        # values[0] = nomor urut
        # values[1] = judul buku
        # values[2] = penulis
        # values[3] = tahun terbit
        self.view.entry_judul.insert(0, values[1])
        self.view.entry_penulis.insert(0, values[2])
        self.view.entry_tahun.insert(0, values[3])

    # =====================================
    # MENYIMPAN DATA BUKU
    # =====================================
    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showwarning(
                "Akses Ditolak",
                "Hanya admin yang dapat menambah data buku.",
                parent=self.view
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom formulir harus diisi!",
                parent=self.view
            )
            return

        try:
            tahun = int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka.",
                parent=self.view
            )
            return

        try:
            berhasil = self.model.create_buku(
                judul,
                penulis,
                tahun
            )

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil disimpan!",
                    parent=self.view
                )

                self.kosongkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Error",
                    "Gagal menyimpan data buku.",
                    parent=self.view
                )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan saat menyimpan data:\n{error}",
                parent=self.view
            )

    # =====================================
    # MEMPERBARUI DATA BUKU
    # =====================================
    def perbarui_data(self):
        if self.user_role != "admin":
            messagebox.showwarning(
                "Akses Ditolak",
                "Hanya admin yang dapat memperbarui data buku.",
                parent=self.view
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin diperbarui!",
                parent=self.view
            )
            return

        # Mengambil ID asli database dari iid.
        id_buku = int(selected[0])

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom formulir harus diisi!",
                parent=self.view
            )
            return

        try:
            tahun = int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka.",
                parent=self.view
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah kamu yakin ingin memperbarui data buku?",
            parent=self.view
        )

        if not konfirmasi:
            return

        try:
            berhasil = self.model.update_buku(
                id_buku,
                judul,
                penulis,
                tahun
            )

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil diperbarui!",
                    parent=self.view
                )

                self.kosongkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Error",
                    "Gagal memperbarui data buku.",
                    parent=self.view
                )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Terjadi kesalahan saat memperbarui data:\n{error}",
                parent=self.view
            )

    # =====================================
    # MENGHAPUS DATA BUKU
    # =====================================
    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showwarning(
                "Akses Ditolak",
                "Hanya admin yang dapat menghapus data buku.",
                parent=self.view
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin dihapus!",
                parent=self.view
            )
            return

        # Mengambil ID asli database dari iid.
        id_buku = int(selected[0])

        konfirmasi = messagebox.askyesno(
            "Konfirmasi Hapus",
            "Apakah kamu yakin ingin menghapus data buku ini?",
            parent=self.view
        )

        if not konfirmasi:
            return

        try:
            berhasil = self.model.delete_buku(id_buku)

            if berhasil:
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil dihapus!",
                    parent=self.view
                )

                self.kosongkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data buku gagal dihapus. Periksa apakah buku "
                    "masih memiliki data peminjaman.",
                    parent=self.view
                )

        except Exception as error:
            messagebox.showerror(
                "Gagal Menghapus",
                "Data buku tidak dapat dihapus.\n"
                "Periksa apakah buku masih digunakan oleh "
                f"data peminjaman.\n\nDetail: {error}",
                parent=self.view
            )

    # =====================================
    # LOGOUT DAN KEMBALI KE LOGIN
    # =====================================
    def logout(self):
        konfirmasi = messagebox.askyesno(
            "Konfirmasi Logout",
            "Apakah kamu yakin ingin logout?",
            parent=self.view
        )

        if not konfirmasi:
            return

        # Menutup halaman Buku
        self.view.destroy()

        # Menampilkan kembali halaman Login
        # melalui callback dari AuthController
        if self.on_logout is not None:
            self.on_logout()

    # =====================================
    # MENJALANKAN HALAMAN BUKU
    # =====================================
    def run(self):
        self.view.mainloop()
