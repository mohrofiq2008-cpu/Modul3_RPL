import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")
        
        self.buku_ids = []

        # Hubungkan tombol ke fungsinya masing-masing
        self.view.btn_simpan.configure(command=self.simpan_data)
        if hasattr(self.view, 'btn_update'):
            self.view.btn_update.configure(command=self.perbarui_data)
        if hasattr(self.view, 'btn_hapus'):
            self.view.btn_hapus.configure(command=self.hapus_data)

        # Event ketika baris pada tabel diklik/dipilih
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data_tabel)

        # Otorisasi role: Kunci semua tombol jika bukan admin
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            if hasattr(self.view, 'btn_update'):
                self.view.btn_update.configure(state="disabled")
            if hasattr(self.view, 'btn_hapus'):
                self.view.btn_hapus.configure(state="disabled")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
            
        data_buku = self.model.get_all_buku()
        self.buku_ids = []
        
        for index, buku in enumerate(data_buku, start=1):
            self.buku_ids.append(buku["id_buku"])
            self.view.tabel.insert("", "end", values=(index, buku["judul"], buku["penulis"], buku["tahun_terbit"]))

    def pilih_data_tabel(self, event):
        """Mengisi otomatis kolom form input saat baris tabel diklik"""
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item[0])["values"]
            
            # Bersihkan form lalu isi dengan data yang dipilih
            self.bersihkan_form()
            self.view.entry_judul.insert(0, item_data[1])   # Judul Buku
            self.view.entry_penulis.insert(0, item_data[2]) # Penulis
            self.view.entry_tahun.insert(0, item_data[3])   # Tahun Terbit

    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def perbarui_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk memperbarui data!")
            return

        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris buku di tabel yang ingin diperbarui!")
            return

        item_index = self.view.tabel.index(selected_item[0])
        id_buku = self.buku_ids[item_index]

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi untuk update!")
            return

        if hasattr(self.model, 'update_buku') and self.model.update_buku(id_buku, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris buku di tabel yang ingin dihapus!")
            return

        item_index = self.view.tabel.index(selected_item[0])
        id_buku = self.buku_ids[item_index]

        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus buku ini?"):
            if hasattr(self.model, 'delete_buku') and self.model.delete_buku(id_buku):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data.")

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def run(self):
        self.view.mainloop()