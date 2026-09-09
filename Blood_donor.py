import mysql.connector

class BloodDonorManager:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="#Hari205183",
                database="blood_db"
            )
            return self.connection
        except Exception as e:
            return None

connection_instance = BloodDonorManager()
connection_instance.get_connection()