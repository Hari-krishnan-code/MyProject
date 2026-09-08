from asyncio import log

import mysql.connector

class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="#Hari205183",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(DbConnect):
    pass

connection_instance = DbConnect()
connection_instance.get_connection()