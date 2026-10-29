import hashlib
from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if self.conn:
            cursor = None

            try:
                cursor = self.conn.cursor(dictionary=True)
                password_hash = self.hash_password(password)

                query = f"""
                    SELECT id_user, username, role
                    FROM {self.table_name}
                    WHERE username = %s AND password = %s
                """

                cursor.execute(query, (username, password_hash))
                user = cursor.fetchone()

                return user

            except Exception as e:
                print(f"Error autentikasi: {e}")
                return None

            finally:
                if cursor:
                    cursor.close()

        print("Koneksi database tidak tersedia.")
        return None

    # === TUGAS NO. 1: Tambahkan metode register_user ===
    def register_user(self, username, password, role="anggota"):
        if self.conn:
            cursor = None

            try:
                cursor = self.conn.cursor()

                # Hash password sebelum disimpan
                password_hash = self.hash_password(password)

                query = f"""
                    INSERT INTO {self.table_name}
                    (username, password, role)
                    VALUES (%s, %s, %s)
                """

                cursor.execute(
                    query,
                    (username, password_hash, role)
                )

                self.conn.commit()
                return True

            except Exception as e:
                print(f"Error Register: {e}")
                self.conn.rollback()
                return False

            finally:
                if cursor:
                    cursor.close()

        print("Koneksi database tidak tersedia.")
        return False
