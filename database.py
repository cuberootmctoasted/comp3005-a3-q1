import psycopg

"""
gets the postgresql database connection given the connection info
"""
def get_database_connection(conn_info: str):
    conn = psycopg.connect(conn_info)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students
        (
        student_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        enrollment_date DATE
        )
    """)
    return conn