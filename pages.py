from psycopg import Connection
import functions

"""
fills the screen with empty lines to reduce clutter
"""
def clear_screen():
    print("\n" * 100)

"""
shows all the students in the given database
press enter to exit the page
"""
def page_get_all_students(conn: Connection):
    clear_screen()
    print("GET ALL STUDENTS")
    print()
    rows = functions.get_all_students(conn)
    for row in rows:
        print(f"student_id: {row[0]}, first_name: {row[1]}, last_name: {row[2]}, email: {row[3]}, enrollment_date: {row[4]}")
    input("...")

"""
repeatedly prompting the user to add students into the database until user inputs ';;'
"""
def page_add_student(conn: Connection):
    clear_screen()
    print("ADD STUDENTS")
    print()
    row = []
    while True:
        field = (
            "first_name" if len(row) == 0 else 
            "last_name" if len(row) == 1 else
            "email" if len(row) == 2 else
            "enrollment_date" if len(row) == 3 else ""
        )
        data = input(f"{field}: ").strip()
        if data == ";;":
            return
        if len(data) == 0:
            print(f"ERROR: {field} cannot be empty")
            continue
        if len(row) == 3:
            try:
                data = functions.str_to_dt(data)
            except:
                print(f"ERROR: invalid date format")
                continue
        row.append(data)
        if len(row) == 4:
            try:
                functions.add_student(conn, row[0], row[1], row[2], row[3])
            except Exception as e:
                print(f"ERROR: {e}")
            row.clear()
            print()
            
"""
repeatedly prompts the user to update student emails until user inputs ';;'
"""
def page_update_student_email(conn: Connection):
    clear_screen()
    print("UPDATE STUDENT EMAIL")
    print()
    row = []
    while True:
        field = (
            "student_id" if len(row) == 0 else
            "new email" if len(row) == 1 else ""
        )
        data = input(f"{field}: ").strip()
        if data == ";;":
            return
        if len(data) == 0:
            print(f"ERROR: {field} cannot be empty")
            continue
        if len(data) == 0:
            try:
                data = int(data)
            except:
                print("ERROR: invalid data type")
                continue
        row.append(data)
        if len(row) == 2:
            try:
                functions.update_student_email(conn, row[0], row[1])
            except Exception as e:
                print(f"ERROR: {e}")
            row.clear()
            print()


"""
repeatedly prompting the user to delete students until user inputs ';;'
"""
def page_delete_student(conn: Connection):
    clear_screen()
    print("DELETE STUDENT")
    print()
    while True:
        data = input("student_id: ").strip()
        if data == ";;":
            return
        if len(data) == 0:
            print(f"ERROR: student_id cannot be empty")
            continue
        try:
            data = int(data)
        except:
            print("ERROR: invalid data type")
            continue
        try:
            functions.delete_student(conn, data)
        except Exception as e:
            print(f"ERROR: {e}")
        print()

"""
repeatedly prompting the user with the menu until user inputs ';;'
entering a number will make the user enter the corresponding page
"""
def page_menu(conn: Connection):
    while True:
        clear_screen()
        print("MENU") 
        print("input ';;' to exit out of any page")
        print("'...' means press enter to continue")
        print("1 - get all students")
        print("2 - add student")
        print("3 - update student email")
        print("4 - delete student")
        inp = input().strip()
        if inp == ";;":
            return
        elif inp == "1":
            page_get_all_students(conn)
        elif inp == "2":
            page_add_student(conn)
        elif inp == "3":
            page_update_student_email(conn)
        elif inp == "4":
            page_delete_student(conn)
        else:
            print("ERROR: invalid input")
            input("...")