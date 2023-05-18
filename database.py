import sqlite3

s = "`subject`"
ta = "`task`"
te = "`teacher`"

class Database:
    def __init__(self): # подключение к БД
        self.connection = sqlite3.connect("../database.db")
        self.cursor = self.connection.cursor()

    def check_teacher(self, tg_id): # проверка наличия преподователя в БД
        with self.connection:
            res = self.cursor.execute("SELECT (tg_id) FROM `teacher` WHERE tg_id = ?", (tg_id,))
            return res.fetchone() is not None
    
    # Тут просто объединил все запросы в один для заполнения всех полей сразу
    def add_teacher(self, tg_id, fullname, subject, grade):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO {te} (tg_id, fullname, subject, grade) VALUES (?, ?, ?, ?)", (tg_id, fullname, subject, grade))