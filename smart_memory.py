import sqlite3
from datetime import datetime

class SmartMemory:
    def __init__(self):
        self.__conn = sqlite3.connect("jarvis.db")
        self.__cursor = self.__conn.cursor()
        self.__create_table()

    def __create_table(self):
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT,
                timestamp TEXT
            )
        """)
        self.__conn.comit()

    def save_memory(self, role, content):
        timestamp = datetime.now().isoformat()
        self.__cursor.execute("""
            INSERT INTO users (role, content, timestamp) VALUES (?, ?, ?)
        """, (role, content, timestamp))
        self.__conn.commit()
        
    def load_history(self):
        self.__cursor.execute("SELECT role, content, timestamp FROM users ORDER BY id DESC")
        return self.__cursor.fetchall()
    
