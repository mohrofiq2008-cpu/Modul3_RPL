import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        self.app_utama = None

        # Menghubungkan tombol Login
        self.view.btn_login.configure(
            command=self.proses_login
        )

    def proses_login(self):
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get()

        # Validasi username dan password
        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan Password wajib diisi!"
            )
            return

        # Autentikasi pengguna
        user = self.model.autentikasi(
            username,
            password
        )

        if user:
            role = user["role"]

            messagebox.showinfo(
                "Login Berhasil",
                f"Selamat datang, {user['username']} ({role})"
            )

            # Sembunyikan halaman Login
            self.view.withdraw()

            # Buka halaman utama perpustakaan
            # on_logout menghubungkan Logout ke halaman Login
            self.app_utama = BukuController(
                user_role=role,
                on_logout=self.tampilkan_login
            )

            self.app_utama.run()

        else:
            messagebox.showerror(
                "Login Gagal",
                "Username atau Password salah!"
            )

            # Kosongkan kolom Password
            self.view.entry_password.delete(0, "end")

    def tampilkan_login(self):
        # Kosongkan form Login
        self.view.entry_username.delete(0, "end")
        self.view.entry_password.delete(0, "end")

        # Tampilkan kembali jendela Login
        self.view.deiconify()
        self.view.lift()
        self.view.focus_force()

        # Hapus referensi aplikasi sebelumnya
        self.app_utama = None

    def run(self):
        self.view.mainloop()