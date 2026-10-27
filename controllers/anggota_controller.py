class AnggotaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Menghubungkan tombol dengan fungsi
        self.view.btn_simpan.config(
            command=self.simpan_data
        )
        self.tampilkan_data()

    def tampilkan_data(self):
        data = self.model.get_all_anggota()

        # Sesuaikan bagian ini dengan tabel GUI
        # untuk menampilkan seluruh data anggota

    def simpan_data(self):
        # Ambil data dari form anggota
        # Panggil metode tambah pada AnggotaModel
        # Perbarui tampilan tabel setelah berhasil
        pass