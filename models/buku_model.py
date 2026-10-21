from config.database import get_connection


class BukuModel:
    def __init__(self):
        self.conn = get_connection()

    def get_all_buku(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id_buku, judul, penulis, tahun_terbit FROM buku"
        )
        data = cursor.fetchall()
        cursor.close()
        return data

    def create_buku(self, judul, penulis, tahun):
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO buku (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (judul, penulis, tahun))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error menyimpan buku: {e}")
            self.conn.rollback()
            return False