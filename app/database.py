import sqlite3 as sq

global db, cur
db = sq.connect('db/tempdb.db')
cur = db.cursor()
# from os import path

# def get_db_path(database):
# 	return 

# connect = sqlite3.connect((path.dirname(__file__) + path.sep + 'db/tempdb.db'), check_same_thread=False)

def db_table_biology(
		id_lesson: int,
		lvl_lesson: int
    ):
	cur.execute('INSERT INTO biology (id_lesson, lvl_lesson) VALUES (?, ?)', (id_lesson, lvl_lesson))
	db.commit()
	
def db_table_chemistry(
		id_lesson: int,
		lvl_lesson: int
    ):
	cur.execute('INSERT INTO chemistry (id_lesson, lvl_lesson) VALUES (?, ?)', (id_lesson, lvl_lesson))
	db.commit()
	
def db_table_informatics(
		id_lesson: int,
		lvl_lesson: int
    ):
	cur.execute('INSERT INTO informatics (id_lesson, lvl_lesson) VALUES (?, ?)', (id_lesson, lvl_lesson))
	db.commit()
	
def db_table_mathematics(
		id_lesson: int,
		lvl_lesson: int
    ):
	cur.execute('INSERT INTO mathematics (id_lesson, lvl_lesson) VALUES (?, ?)', (id_lesson, lvl_lesson))
	db.commit()
	
def db_table_teacher(
		teacher_id: int,
		user_name: str, 
		username_teacher: str,
		online: int
    ):
	cur.execute('INSERT INTO teacher (teacher_id, user_name, username_teacher, online) VALUES (?, ?, ?, ?, ?, ?)', (teacher_id, user_name, username_teacher, online))
	db.commit()
	
def db_table_client(
		client_id: int,
		id_lesson: int, 
		lvl_lesson: int,
		id_teacher: int,
		accepted_job: int,
        completed_job: int
    ):
	cur.execute('INSERT INTO client (client_id, id_lesson, lvl_lesson, id_teacher, accepted_job, completed_job) VALUES (?, ?, ?, ?, ?, ?)', (client_id, id_lesson, lvl_lesson, id_teacher, accepted_job, completed_job))
	db.commit()


