from database import get_database_connection
from functions import insert_sample_data
from pages import page_menu

CONN_INFO = (
    "host=localhost "
    "port=5432 "
    "dbname=a3q1 "
    "user=postgres "
    "password=77SD52MptHVgnjD#CReCUT1zNbNV9b*ya9qZbtyHq@TmwQB@hC8&$9c7Zf^7@twW"
)

if __name__ == "__main__":
    conn = None
    try:
        conn = get_database_connection(CONN_INFO)
        insert_sample_data(conn)
    except Exception as e:
        print(f"ERROR: {e}")
    if conn != None:    
        with conn:
            page_menu(conn)