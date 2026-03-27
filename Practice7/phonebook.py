import csv
import sys
import os
from connect import get_conn, create_table

def from_csv(file_path):
    conn = get_conn()
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as f:
            r = csv.DictReader(f)
            with conn.cursor() as cur:
                for row in r:
                    cur.execute(
                        "INSERT INTO contacts (username, first_name, phone) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                        (row['username'], row['first_name'], row['phone'])
                    )
            conn.commit()
        print("CSV data imported successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def from_console():
    username = input("Enter unique username: ")
    first_name = input("Enter first name: ")
    phone = input("Enter phone number: ")
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO contacts (username, first_name, phone) VALUES (%s, %s, %s)",
                (username, first_name, phone)
            )
        conn.commit()
        print("Contact added.")
    except Exception as e:
        print(f"Failed to add contact: {e}")
    finally:
        conn.close()

def upd_contact():
    username = input("Enter the username of the contact to update: ")
    field = input("What would you like to update? (first_name/phone): ").lower()
    new_value = input(f"Enter new {field}: ")
    if field not in ['first_name', 'phone']:
        print("Invalid field.")
        return
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(f"UPDATE contacts SET {field} = %s WHERE username = %s", (new_value, username))
        conn.commit()
        print("Update successful.")
    conn.close()

def search_contact():
    print("Filter by: 1. Name  2. Phone Prefix  3. All")
    choice = input("> ")
    conn = get_conn()
    with conn.cursor() as cur:
        if choice == '1':
            name = input("Enter name: ")
            cur.execute("SELECT * FROM contacts WHERE first_name ILIKE %s", (f"%{name}%",))
        elif choice == '2':
            prefix = input("Enter phone prefix: ")
            cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{prefix}%",))
        else:
            cur.execute("SELECT * FROM contacts")
        results = cur.fetchall()
        for row in results:
            print(row)
    conn.close()

def del_contact():
    t = input("Enter username or phone to delete: ")
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM contacts WHERE username = %s OR phone = %s", (t, t))
        conn.commit()
        print("Contact deleted if it existed.")
    conn.close()

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'contacts.csv')

    create_table()
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Import CSV\n2. Add Contact\n3. Update Contact\n4. Search\n5. Delete\n6. Exit")
        cmd = input("Select an option: ")
        
        if cmd == '1': 
            from_csv(csv_path)
        elif cmd == '2': from_console()
        elif cmd == '3': upd_contact()
        elif cmd == '4': search_contact()
        elif cmd == '5': del_contact()
        elif cmd == '6': break