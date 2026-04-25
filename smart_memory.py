import keyword
import sqlite3
from datetime import datetime

class SmartMemory:
    def __init__(self):
        self.__conn = sqlite3.connect("jarvis.db")
        self.__cursor = self.__conn.cursor()
        self.__create_table()

    def __create_table(self):
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT,
                timestamp TEXT
            )
        """)
        self.__conn.commit()

    def save_memory(self, role, content):
        timestamp = datetime.now().isoformat()
        self.__cursor.execute("""
            INSERT INTO messages (role, content, timestamp) VALUES (?, ?, ?)
        """, (role, content, timestamp))
        self.__conn.commit()
        
    def load_history(self):
        self.__cursor.execute("SELECT role, content, timestamp FROM messages ORDER BY id DESC")
        return self.__cursor.fetchall()
    
    def clear_history(self):
        self.__cursor.execute("DELETE FROM messages")
        self.__conn.commit()

    def search_memory(self, keyword):
        self.__cursor.execute("SELECT role, content, timestamp FROM messages WHERE content LIKE ?",(f"%{keyword}%",))
        return self.__cursor.fetchall()
