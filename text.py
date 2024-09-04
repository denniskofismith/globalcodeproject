import sqlite3

def setup_database():
    conn = sqlite3.connect('final.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS motion_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

setup_database()
print("successfull")