from config.database import get_connection

class BukuModel:
    def __init__(self):
        self.conn = get_connection()

    def get_all_buku(self):
        cursor = None

        try:
            cursor = self.conn.cursor(dictionary=True)

            query = """
                SELECT id_buku, judul, penulis, tahun_terbit
                FROM buku
            """
            cursor.execute(query)

            data = cursor.fetchall()
            return data

        except Exception as e:
            print(f"Error mengambil data buku: {e}")
            return []

        finally:
            if cursor is not None:
                cursor.close()

    def create_buku(self, judul, penulis, tahun):
        cursor = None

        try:
            cursor = self.conn.cursor()

            query = """
                INSERT INTO buku (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (judul, penulis, tahun))

            self.conn.commit()
            return True

        except Exception as e:
            print(f"Error menyimpan buku: {e}")
            self.conn.rollback()
            return False

        finally:
            if cursor is not None:
                cursor.close()

    def delete_buku(self, id_buku):
        cursor = None

        try:
            cursor = self.conn.cursor()

            query = "DELETE FROM buku WHERE id_buku = %s"
            cursor.execute(query, (id_buku,))

            # Menyimpan perubahan ke database MySQL
            self.conn.commit()

            # Memastikan ada data yang terhapus
            berhasil = cursor.rowcount > 0

            if not berhasil:
                print(f"Tidak ada buku dengan ID {id_buku}.")

            return berhasil

        except Exception as e:
            self.conn.rollback()
            print(f"Error menghapus buku: {e}")
            return False

        finally:
            if cursor is not None:
                cursor.close()

    def update_buku(self, id_buku, judul, penulis, tahun):
        cursor = None

        try:
            cursor = self.conn.cursor()

            query = """
                UPDATE buku
                SET judul = %s,
                    penulis = %s,
                    tahun_terbit = %s
                WHERE id_buku = %s
            """
            cursor.execute(
                query,
                (judul, penulis, tahun, id_buku)
            )

            self.conn.commit()

            # True jika ada baris yang berubah
            return cursor.rowcount > 0

        except Exception as e:
            self.conn.rollback()
            print(f"Error memperbarui buku: {e}")
            return False

        finally:
            if cursor is not None:
                cursor.close()