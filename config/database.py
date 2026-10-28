import mysql.connector

# Fungsi ini tetap ada agar buku_model.py tidak error
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="perpustakaan"
    )

# Tambahkan kelas Database ini agar user_model.py dari modul berjalan lancar
class Database:
    def get_connection(self):
        return get_connection()