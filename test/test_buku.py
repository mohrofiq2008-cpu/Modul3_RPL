
import sys
from pathlib import Path
from unittest.mock import MagicMock

# Menambahkan folder utama proyek ke jalur pencarian Python
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from models.buku_model import BukuModel


def test_get_all_buku():
    # Membuat objek model tanpa menjalankan __init__
    model = BukuModel.__new__(BukuModel)

    # Mengganti koneksi database dengan mock
    model.conn = MagicMock()

    data_buku = [
        {
            "id_buku": 1,
            "judul": "Belajar Python",
            "penulis": "Andi",
            "tahun_terbit": 2025
        },
        {
            "id_buku": 2,
            "judul": "Belajar MySQL",
            "penulis": "Budi",
            "tahun_terbit": 2026
        }
    ]

    # Mengatur hasil data yang dikembalikan database
    cursor = model.conn.cursor.return_value
    cursor.fetchall.return_value = data_buku

    # Memanggil fungsi yang diuji
    hasil = model.get_all_buku()

    # Memastikan hasil sesuai dengan data yang diharapkan
    assert hasil == data_buku

    # Memastikan query dijalankan
    cursor.execute.assert_called_once()
