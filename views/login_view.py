import customtkinter as ctk

class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # 1. TAMBAHKAN BARIS INI (Mengubah mode ke terang/putih)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.title("Login Sistem Perpustakaan")
        self.geometry("360x320")
        self.resizable(False, False)

        # 2. UBAH BARIS INI (Menambahkan fg_color="#FFFFFF" agar latar frame putih)
        self.frame = ctk.CTkFrame(self, fg_color="#FFFFFF")
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(self.frame, text="LOGIN SISTEM", font=("Arial", 18, "bold"), text_color="#0F172A").pack(pady=(20, 15))

        # 3. UBAH BARIS INPUT (Menambahkan fg_color="#FFFFFF")
        self.entry_username = ctk.CTkEntry(self.frame, placeholder_text="Username", fg_color="#FFFFFF")
        self.entry_username.pack(pady=10, padx=20, fill="x")

        self.entry_password = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*", fg_color="#FFFFFF")
        self.entry_password.pack(pady=10, padx=20, fill="x")

        self.btn_login = ctk.CTkButton(self.frame, text="Masuk", fg_color="blue")
        self.btn_login.pack(pady=20, padx=20, fill="x")