import sqlite3

DB_NAME = 'Assignment_2/students.db'

def connect_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                grade TEXT,
                email TEXT
            )
        ''')
        conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")

def add_student(conn):
    name = input("Enter student name: ")
    grade = input("Enter student grade (K-12): ")
    valid_grades = [str(i) for i in range(1, 13)] + ["K"]
    if grade not in valid_grades:
        print("Invalid grade. Only K or 1-12 are accepted.")
        return
    email = input("Enter student email: ")
    if '@' not in email:
        print("Invalid email. Must contain '@'.")
        return
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, grade, email) VALUES (?, ?, ?)", (name, grade, email))
        conn.commit()
        print("Student added successfully.")
    except Exception as e:
        print(f"Error adding student: {e}")

def view_students(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        if not rows:
            print("No student records found.")
        else:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}, Email: {row[3]}")
    except Exception as e:
        print(f"Error retrieving students: {e}")

def update_student(conn):
    try:
        student_id = input("Enter the ID of the student to update: ")
        if not student_id.isdigit():
            print("Invalid ID. Must be an integer.")
            return
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()
        if not student:
            print("Student not found.")
            return
        name = input(f"Enter new name (current: {student[1]}): ") or student[1]
        grade = input(f"Enter new grade (current: {student[2]}): ") or student[2]
        valid_grades = [str(i) for i in range(1, 13)] + ["K"]
        if grade not in valid_grades:
            print("Invalid grade. Only K or 1-12 are accepted.")
            return
        email = input(f"Enter new email (current: {student[3]}): ") or student[3]
        if '@' not in email:
            print("Invalid email. Must contain '@'.")
            return
        cursor.execute("UPDATE students SET name = ?, grade = ?, email = ? WHERE id = ?", (name, grade, email, student_id))
        conn.commit()
        print("Student updated successfully.")
    except Exception as e:
        print(f"Error updating student: {e}")

def delete_student(conn):
    try:
        student_id = input("Enter the ID of the student to delete: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()
        if not student:
            print("Student not found.")
            return
        if not student_id.isdigit():
            print("Invalid ID. Must be an integer.")
            return
        confirm = input(f"Are you sure you want to delete student with ID {student_id} - {student[1]}? (y/n): ")
        if confirm.lower() != 'y':
            print("Delete cancelled.")
            return
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student deleted successfully.")
    except Exception as e:
        print(f"Error deleting student: {e}")

def main():
    conn = connect_db()
    if not conn:
        return
    create_table(conn)
    while True:
        print("\nStudent Manager Menu:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            add_student(conn)
        elif choice == '2':
            view_students(conn)
        elif choice == '3':
            update_student(conn)
        elif choice == '4':
            delete_student(conn)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please select 1-5.")
    conn.close()

if __name__ == "__main__":
    main() 