import csv
import psycopg2
from psycopg2 import OperationalError

def connect_db():
    try:
        
        return psycopg2.connect(
            host="localhost",
            port="5433",
            dbname="postgres",
            user="suppliers",
            password="adal",
            connect_timeout=10,
            sslmode="prefer"
        )
    except OperationalError as e:
        
        print(f"Error connecting to the database: {e}")
        return None

def create_table():
    
    conn = connect_db()
    if conn is None:
        return

   
    cur = conn.cursor()

    try:
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                phone VARCHAR(15) UNIQUE NOT NULL
            );
        """)
        conn.commit()
        print("Table created successfully.")
    except OperationalError as e:
        
        print(f"Error creating table: {e}")
    finally:
        
        cur.close()
        conn.close()

def load_from_csv():
    
    conn = connect_db()
    if conn is None:
        return

    
    cur = conn.cursor()

    try:
        
        with open('C:/MyPythonProjects/TSIS/PyGame/files/phonebook.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
                    row
                )
        conn.commit()
        print("Data loaded from CSV successfully.")
    except (OperationalError, FileNotFoundError, IOError) as e:
        
        print(f"Error loading data from CSV: {e}")
    finally:
        
        cur.close()
        conn.close()



def main():
    create_table()
    while True:
        print("\n1. Load data from CSV")
        print("2. Add data via console")
        print("3. Update data")
        print("4. View all records")
        print("5. Delete data")
        print("6. Exit")
        choice = input("Choose an action: ")
        
        if choice == '1':
            load_from_csv()
        
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()