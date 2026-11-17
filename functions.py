from psycopg import Connection
from datetime import datetime

"""
turns python datetime type into 'yyyy-mm-dd'
"""
def dt_to_str(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d")

"""
turns 'yyyy-mm-dd' to python datetime type
"""
def str_to_dt(dt_sql: str) -> datetime:
    return datetime.strptime(dt_sql, "%Y-%m-%d")

"""
inserts the initial dataset into the database
"""
def insert_sample_data(conn: Connection):
    rows = conn.execute("""SELECT 1 FROM students WHERE email in ('john.doe@example.com', 'jane.smith@example.com', 'jim.beam@example.com')""").fetchall()
    if len(rows) > 0:
        return
    conn.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
    """)

"""
returns all the tuples in the students table
"""
def get_all_students(conn: Connection):
    return conn.execute("SELECT * FROM students").fetchall()

"""
add a student into the database given the attributes
"""
def add_student(conn: Connection, first_name: str, last_name: str, email: str, enrollment_date: datetime):
    conn.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        (%s, %s, %s, %s)
    """, (first_name, last_name, email, enrollment_date))

"""
updates the student email at the given student_id
"""
def update_student_email(conn: Connection, student_id: int, new_email: str):
    conn.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))

"""
delete the student at the given student_id
"""
def delete_student(conn: Connection, student_id: int):
    conn.execute("DELETE FROM students WHERE student_id = %s", (student_id, ))