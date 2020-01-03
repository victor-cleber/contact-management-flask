import sqlite3


def create():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS "
                   "contacts(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "name text, phone_number text)")
    conn.commit()
    conn.close()


def insert(name, phone_number):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts "
                   "VALUES(NULL, ?, ?)", (name, phone_number))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * "
                   "FROM  contacts")
    row = cursor.fetchall()
    conn.close()
    print(row)


def search(id, name, phone_number):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id=? OR name=? OR "
                   "phone_number=?", (id, name, phone_number))
    row = cursor.fetchall()
    conn.close()
    print(row)


def edit(id, name, phone_number):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts "
                   "WHERE id=? OR name=? OR phone_number=?",
                   (id, name, phone_number))
    row = cursor.fetchall()
    index = row[0][0]
    name = input("Enter a new name: ")
    phone_number = input("Enter a new phone number: ")
    cursor.execute("UPDATE contacts SET name=?, phone_number=?"
                   "WHERE id=?", (name, phone_number, index))
    conn.commit()
    conn.close()


def delete(id, name, phone_number):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts "
                   "WHERE id=? OR name=? OR phone_number=?",
                   (id, name, phone_number))
    row = cursor.fetchall()
    index = row[0][0]    
    cursor.execute("DELETE FROM contacts "
                   "WHERE id=?",
                   (index,))
    conn.commit()
    conn.close()


option = 8

while option > 6:
    option = int(input('''What do want to do?
                    1 - INSERT contact
                    2 - VIEW ALL contacts
                    3 - EDIT contact
                    4 - DELETE contact
                    5 - SEARCH contact
                    0 - EXIT
    OPTION = '''))
    create()
    if option == 0:
        break
    elif option == 1:
        name = input("Enter your name: ")
        phone_number = input("Enter your number: ")
        insert(name, phone_number)
    elif option == 2:
        view()
    elif option == 3:
        id = int(input("Enter the contact id: "))
        name = input("Enter the contact name: ")
        phone_number = input("Enter the contact number: ")
        edit(id, name, phone_number)
    elif option == 4:
        id = int(input("Enter the contact id: "))
        name = input("Enter the contact name: ")
        phone_number = input("Enter the contact number: ")
        delete(id, name, phone_number)
    elif option == 5:
        id = int(input("Enter the contact id: "))
        name = input("Enter the contact name: ")
        phone_number = input("Enter the contact number: ")
        search(id, name, phone_number)
    option = 8
