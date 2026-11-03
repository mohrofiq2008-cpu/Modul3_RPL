# Sistem Manajemen Perpustakaan

Aplikasi desktop perpustakaan menggunakan Python, CustomTkinter, MySQL, dan pola Model–View–Controller (MVC). Aplikasi menyediakan login dengan role `admin` dan `anggota`. Admin dapat menambah, memperbarui, dan menghapus data buku, sedangkan anggota hanya dapat melihat data buku.

## Struktur Direktori

```text
.
├── Controller/
│   ├── auth_controller.py
│   └── buku_controller.py
├── Models/
│   ├── user_model.py
│   └── buku_model.py
├── views/
│   ├── login_view.py
│   └── buku_view.py
├── tests/
│   ├── test_auth.py
│   └── test_buku.py
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

Sesuaikan nama file jika berbeda pada proyek Anda. Penulisan `Models`, `Controller`, dan `views` harus sama persis dengan nama folder sebenarnya.

## Persyaratan

- Python 3
- Git dan akun GitHub
- Laragon dengan MySQL
- pip

## Instalasi

Clone repositori dan masuk ke folder proyek:

```bash
git clone <URL_REPOSITORI_GITHUB>
cd <NAMA_FOLDER_PROYEK>
python -m venv env
```

Aktifkan virtual environment di Windows:

```powershell
.\env\Scripts\activate
```

Instal dependensi:

```bash
pip install -r requirements.txt
```

## Konfigurasi Database MySQL

1. Buka Laragon dan jalankan layanan MySQL.
2. Buat atau pilih database yang digunakan proyek.
3. Pastikan tabel pengguna (`users`) dan tabel buku beserta kolom yang dibutuhkan sudah tersedia.
4. Periksa `Models/user_model.py` dan `Models/buku_model.py`, lalu sesuaikan host, port, username, password, dan nama database dengan konfigurasi MySQL lokal.

Contoh parameter (sesuaikan dengan database Anda):

```python
host = "localhost"
user = "<USERNAME_MYSQL>"
password = "<PASSWORD_MYSQL>"
database = "<NAMA_DATABASE>"
```

Jangan unggah kredensial database pribadi ke repositori publik. Masukkan file konfigurasi rahasia ke `.gitignore` jika digunakan.

## Menjalankan Aplikasi

Pastikan virtual environment aktif dan MySQL Laragon berjalan, kemudian jalankan:

```bash
python main.py
```

Akun contoh dari praktikum Modul VII:

| Username | Password | Role |
|---|---|---|
| `petugas` | `admin123` | `admin` |
| `mahasiswa` | `user123` | `anggota` |

Akun tersebut hanya dapat digunakan jika sudah tersedia di database lokal.

## Pengujian

```bash
pytest -v
```

## Pemeriksaan Kualitas Kode

Instal Flake8 dan jalankan pemeriksaan:

```bash
pip install flake8
flake8 Models/ Controller/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

## CI dengan GitHub Actions

Konfigurasi workflow berada di `.github/workflows/ci_pipeline.yml`. Workflow berjalan pada push dan pull request ke branch `main`, memasang dependensi, menjalankan Flake8, kemudian menjalankan unit test dengan pytest. Hasilnya dapat dilihat pada tab **Actions** di GitHub.

## Membuat File Executable Windows

Instal PyInstaller:

```bash
pip install pyinstaller
```

Build aplikasi:

```bash
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" main.py
```

Hasil build berada di `dist/AplikasiPerpustakaan.exe`. Aktifkan MySQL Laragon jika aplikasi memerlukan database saat dijalankan.

## Rilis GitHub v1.0.0

1. Buka repositori GitHub, lalu pilih **Releases**.
2. Klik **Draft a new release**.
3. Buat tag `v1.0.0` dan judul `Aplikasi Perpustakaan v1.0.0`.
4. Lampirkan `dist/AplikasiPerpustakaan.exe`.
5. Publikasikan release dan pastikan file dapat diunduh.

Dokumentasi untuk praktikum **Modul VIII – Otomasi CI/CD Pipeline dan Pemaketan Aplikasi**.