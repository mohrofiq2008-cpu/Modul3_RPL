import customtkinter as ctk
from tkinter import ttk, messagebox


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("1200x650")

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORM DATA ANGGOTA
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0, column=0, padx=10, pady=10, sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Input Nama Anggota
        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Anggota"
        )
        self.entry_nama.pack(
            pady=10, padx=15, fill="x"
        )

        # Input Alamat
        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Alamat"
        )
        self.entry_alamat.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol Simpan Data
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green",
            command=self.simpan_data
        )
        self.btn_simpan.pack(
            pady=(20, 5), padx=15, fill="x"
        )

        # Tombol Perbarui Data
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data (Update)",
            fg_color="blue",
            command=self.perbarui_data
        )
        self.btn_update.pack(
            pady=5, padx=15, fill="x"
        )

        # Tombol Hapus Data
        self.btn_hapus = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data (Delete)",
            fg_color="red",
            hover_color="darkred",
            command=self.hapus_data
        )
        self.btn_hapus.pack(
            pady=5, padx=15, fill="x"
        )

        # FRAME KANAN: TABEL DATA ANGGOTA
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0, column=1, padx=10, pady=10, sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Anggota Perpustakaan",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Kolom Tabel Anggota
        kolom = ("id", "nama", "alamat")

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )

        # Judul Kolom
        self.tabel.heading("id", text="ID")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        # Lebar Kolom
        self.tabel.column(
            "id", width=50, anchor="center"
        )
        self.tabel.column(
            "nama", width=200
        )
        self.tabel.column(
            "alamat", width=350
        )

        self.tabel.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # Mengisi formulir saat baris dipilih
        self.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # Nomor ID anggota otomatis
        self.nomor_id = 1

    # =====================================
    # FUNGSI SIMPAN DATA ANGGOTA
    # =====================================
    def simpan_data(self):
        nama = self.entry_nama.get().strip()
        alamat = self.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama anggota dan alamat harus diisi!"
            )
            return

        self.tabel.insert(
            "",
            "end",
            values=(self.nomor_id, nama, alamat)
        )

        self.nomor_id += 1
        self.kosongkan_form()

        messagebox.showinfo(
            "Berhasil",
            "Data anggota berhasil disimpan!"
        )

    # =====================================
    # FUNGSI MEMILIH DATA ANGGOTA
    # =====================================
    def pilih_data(self, event=None):
        pilihan = self.tabel.selection()

        if not pilihan:
            return

        data = self.tabel.item(
            pilihan[0], "values"
        )

        self.entry_nama.delete(0, "end")
        self.entry_nama.insert(0, data[1])

        self.entry_alamat.delete(0, "end")
        self.entry_alamat.insert(0, data[2])

    # =====================================
    # FUNGSI PERBARUI DATA ANGGOTA
    # =====================================
    def perbarui_data(self):
        pilihan = self.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota pada tabel terlebih dahulu!"
            )
            return

        nama = self.entry_nama.get().strip()
        alamat = self.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama anggota dan alamat harus diisi!"
            )
            return

        data_lama = self.tabel.item(
            pilihan[0], "values"
        )

        self.tabel.item(
            pilihan[0],
            values=(data_lama[0], nama, alamat)
        )

        self.kosongkan_form()

        messagebox.showinfo(
            "Berhasil",
            "Data anggota berhasil diperbarui!"
        )

    # =====================================
    # FUNGSI HAPUS DATA ANGGOTA
    # =====================================
    def hapus_data(self):
        pilihan = self.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota yang ingin dihapus!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data anggota ini?"
        )

        if konfirmasi:
            self.tabel.delete(pilihan[0])
            self.kosongkan_form()

            messagebox.showinfo(
                "Berhasil",
                "Data anggota berhasil dihapus!"
            )

    # =====================================
    # FUNGSI KOSONGKAN FORMULIR
    # =====================================
    def kosongkan_form(self):
        self.entry_nama.delete(0, "end")
        self.entry_alamat.delete(0, "end")

        for item in self.tabel.selection():
            self.tabel.selection_remove(item)

    
    # =====================================
    # FUNGSI HAPUS DATA ANGGOTA
    # =====================================
    def hapus_data(self):
        pilihan = self.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota yang ingin dihapus!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data anggota ini?"
        )

        if konfirmasi:
            self.tabel.delete(pilihan[0])

            # Mengurutkan ulang ID mulai dari 1
            for nomor, item in enumerate(
                self.tabel.get_children(), start=1
            ):
                data = list(
                    self.tabel.item(item, "values")
                )
                data[0] = nomor

                self.tabel.item(
                    item,
                    values=tuple(data)
                )

            # Memperbarui nomor ID berikutnya
            self.nomor_id = len(
                self.tabel.get_children()
            ) + 1

            self.kosongkan_form()

            messagebox.showinfo(
                "Berhasil",
                "Data anggota berhasil dihapus!"
            )



# =====================================
# MENJALANKAN APLIKASI
# =====================================
if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()
