import sqlite3

CREATE_TABLES = """
   CREATE TABLE IF NOT EXISTS Students (
        id  INTEGER PRIMARY KEY,
        name TEXT ,
        mail TEXT,
        note REAL ) """
ADD_STUDENT = "INSERT INTO Students(name, mail,note ) VALUES(?,?,?) "
SHOW_ALL_STDS = "SELECT * FROM Students"
GET_STD_BY_NAME = "SELECT * FROM Students WHERE name = ?"
GET_THE_FIRST_NOTE = "SELECT name, MAX(note) FROM Students "
GET_THE_FIRST_THREE = "SELECT * FROM Students ORDER BY note DESC LIMIT 3"
AVERAGE = "SELECT AVG(note) FROM Students"

con = sqlite3.connect('data.db')

def create_tables(con):
    with con :
        con.execute(CREATE_TABLES)
    

    
def ADD_student(conn, name, mail, note):
    with conn:
        conn.execute(ADD_STUDENT, (name, mail, note))
        print('Student has been added')
    


def see_all_students(conn):
    with conn:
        return conn.execute(SHOW_ALL_STDS).fetchall()
    
    

def First_note(conn):
    with conn:
        note = conn.execute(GET_THE_FIRST_NOTE).fetchone()
        print(f'The First note of the Year is {note}')
   
    

def lock_up_std_by_name(conn, name):
    with conn:
        return conn.execute(GET_STD_BY_NAME, (name,))
    
    
def the_first_three(conn):
    with conn:
       return conn.execute(GET_THE_FIRST_THREE).fetchall()
    


def add_many_stds(con,data):
    with con:
        con.executemany(ADD_STUDENT,data)
        print('the command executed succsefully')
    con.commit()
    


