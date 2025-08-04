import sqlite3
from contextlib import closing

# ---------- Custom SQLite Functions ----------
def calculate_discount(age):
    try:
        return age * 0.9  # Applies a 10% discount
    except TypeError:
        return None

def len_func(s):
    try:
        return len(s) if s is not None else 0
    except TypeError:
        return None

def substr_func(s, start, length):
    try:
        if s is None:
            return None
        start = int(start)
        length = int(length)
        if start < 0:
            start = len(s) + start
        else:
            start = start - 1  # SQLite substr starts at 1
        return s[start:start + length]
    except (TypeError, ValueError):
        return None

# ---------- Database Setup ----------
def create_table():
    with closing(sqlite3.connect('students.db', timeout=30)) as conn:
        conn.execute('PRAGMA journal_mode = WAL;')  # Enable Write-Ahead Logging
        conn.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
            )
        ''')
        conn.commit()

# ---------- CRUD Functions ----------
def insert_student(name, age, grade):
    with closing(sqlite3.connect('students.db', timeout=30)) as conn:
        conn.execute('PRAGMA journal_mode = WAL;')
        conn.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))
        conn.commit()

def fetch_all():
    with closing(sqlite3.connect('students.db', timeout=30)) as conn:
        conn.execute('PRAGMA journal_mode = WAL;')

        # Register custom functions
        conn.create_function("calculate_discount", 1, calculate_discount)
        conn.create_function("LEN", 1, len_func)
        conn.create_function("SUBSTRING", 3, substr_func)

        cursor = conn.cursor()
        cursor.execute('''
            SELECT
                id,
                name,
                age,
                grade,
                calculate_discount(age) AS discounted_age,
                LEN(name) AS name_length,
                SUBSTRING(name, 1, 3) AS name_prefix
            FROM students
        ''')
        return cursor.fetchall()

def update_student(student_id, name, age, grade):
    with closing(sqlite3.connect('students.db', timeout=30)) as conn:
        conn.execute('PRAGMA journal_mode = WAL;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        if cursor.fetchone():
            cursor.execute('''
                UPDATE students
                SET name = ?, age = ?, grade = ?
                WHERE id = ?
            ''', (name, age, grade, student_id))
            conn.commit()
            print("Student updated successfully!")
        else:
            print(f"No student found with ID {student_id}.")

def delete_student(student_id):
    with closing(sqlite3.connect('students.db', timeout=30)) as conn:
        conn.execute('PRAGMA journal_mode = WAL;')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        if cursor.fetchone():
            cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
            conn.commit()
            print("Student deleted successfully!")
        else:
            print(f"No student found with ID {student_id}.")

def view_all_students():
    students = fetch_all()
    if not students:
        print("No students found.")
    else:
        print("\nAll Students:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}, "
                  f"Discounted Age: {student[4]:.1f}, Name Length: {student[5]}, Name Prefix: {student[6]}")

# ---------- Menu ----------
def menu():
    create_table()  # Ensure table is created
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Insert Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("Invalid age. Please enter a number.")
                continue
            grade = input("Enter grade: ")
            insert_student(name, age, grade)
            print("Student added successfully!")

        elif choice == '2':
            view_all_students()

        elif choice == '3':
            view_all_students()
            try:
                student_id = int(input("Enter student ID to update: "))
                name = input("Enter new name: ")
                age = int(input("Enter new age: "))
                grade = input("Enter new grade: ")
                update_student(student_id, name, age, grade)
            except ValueError:
                print("Invalid input. Please enter valid data.")

        elif choice == '4':
            view_all_students()
            try:
                student_id = int(input("Enter student ID to delete: "))
                delete_student(student_id)
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

