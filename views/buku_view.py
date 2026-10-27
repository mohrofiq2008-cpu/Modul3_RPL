import customtkinter as ctk
from tkinter import ttk


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Konfigurasi jendela utama
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("1200x700")
        self.minsize(1000, 600)

        # Tema aplikasi
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Konfigurasi grid utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # =====================================
        # NAMA PENGGUNA POJOK KANAN ATAS
        # =====================================
        self.label_nama = ctk.CTkLabel(
            self,
            text="Moh Rofiq As Shadiq Tolinggi_F5212530096",
            font=("Arial", 12, "bold"),
            text_color="white"
        )
        self.label_nama.place(
            relx=0.985,
            y=10,
            anchor="ne"
        )

        # =====================================
        # FRAME KIRI: FORM DATA BUKU
        # =====================================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0,
            column=0,
            padx=10,
            pady=(40, 10),
            sticky="nsew"
        )

        self.frame_kiri.grid_columnconfigure(0, weight=1)

        self.label_form = ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Buku",
            font=("Arial", 20, "bold")
        )
        self.label_form.grid(
            row=0,
            column=0,
            padx=10,
            pady=20
        )

        # Input judul buku
        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Judul Buku",
            height=35
        )
        self.entry_judul.grid(
            row=1,
            column=0,
            padx=18,
            pady=12,
            sticky="ew"
        )

        # Input nama penulis
        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Penulis",
            height=35
        )
        self.entry_penulis.grid(
            row=2,
            column=0,
            padx=18,
            pady=12,
            sticky="ew"
        )

        # Input tahun terbit
        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Tahun Terbit (Misal: 2020)",
            height=35
        )
        self.entry_tahun.grid(
            row=3,
            column=0,
            padx=18,
            pady=12,
            sticky="ew"
        )

        # =====================================
        # TOMBOL SIMPAN DATA
        # =====================================
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green",
            hover_color="darkgreen",
            height=35
        )
        self.btn_simpan.grid(
            row=4,
            column=0,
            padx=18,
            pady=(25, 10),
            sticky="ew"
        )

        # =====================================
        # TOMBOL PERBARUI DATA
        # Nama disesuaikan dengan Controller
        # =====================================
        self.btn_perbarui = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data (Update)",
            fg_color="blue",
            hover_color="darkblue",
            height=35
        )
        self.btn_perbarui.grid(
            row=5,
            column=0,
            padx=18,
            pady=5,
            sticky="ew"
        )

        # Alias untuk kompatibilitas dengan kode lama
        self.btn_update = self.btn_perbarui

        # =====================================
        # TOMBOL HAPUS DATA
        # =====================================
        self.btn_hapus = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data (Delete)",
            fg_color="red",
            hover_color="darkred",
            height=35
        )
        self.btn_hapus.grid(
            row=6,
            column=0,
            padx=18,
            pady=5,
            sticky="ew"
        )

        # =====================================
        # FRAME KANAN: TABEL DAFTAR BUKU
        # =====================================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0,
            column=1,
            padx=(0, 10),
            pady=(40, 10),
            sticky="nsew"
        )

        self.frame_kanan.grid_columnconfigure(0, weight=1)
        self.frame_kanan.grid_rowconfigure(1, weight=1)

        self.label_tabel = ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Koleksi Buku",
            font=("Arial", 20, "bold")
        )
        self.label_tabel.grid(
            row=0,
            column=0,
            padx=10,
            pady=20
        )

        # =====================================
        # STYLE TABEL
        # =====================================
        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=25,
            fieldbackground="white"
        )

        style.configure(
            "Treeview.Heading",
            background="white",
            foreground="black",
            font=("Arial", 10, "bold")
        )

        # =====================================
        # TABEL BUKU
        # =====================================
        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=(
                "id_buku",
                "judul",
                "penulis",
                "tahun_terbit"
            ),
            show="headings",
            selectmode="browse"
        )

        self.tabel.heading("id_buku", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun_terbit", text="Tahun")

        self.tabel.column(
            "id_buku",
            width=60,
            anchor="center"
        )
        self.tabel.column(
            "judul",
            width=220,
            anchor="center"
        )
        self.tabel.column(
            "penulis",
            width=180,
            anchor="center"
        )
        self.tabel.column(
            "tahun_terbit",
            width=100,
            anchor="center"
        )

        self.tabel.grid(
            row=1,
            column=0,
            padx=15,
            pady=(0, 15),
            sticky="nsew"
        )