import mysql.connector

def menu():
    print(f"Available options: \n"
          f"1. Add new student entry\n"
          f"2. Delete student entry\n"
          f"3. Display student entry\n"
          f"4. Search for existing entry\n"
          f"5. Update student entry\n"
          f"6. Exit\n")

    selector = int(input("Enter the option (1 - 6): "))

    if selector == 1:
        register()
    elif selector == 2:
        delete()
    elif selector == 3:
        display_table()
    elif selector == 4:
        search()
    elif selector == 5:
        update()
    elif selector == 6:
        close()
    else:
        print("Invalid input. Enter valid option.")
        menu()

connection = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="Poojan@019",
                                     db="student")

print(connection)

cursor = connection.cursor()
global table_name
global table_name2

menu()

def checker():
    global table_name
    table_name = input("Enter the table name to use: ")
    try:
        record_check = "select * from " + table_name + ";"
        cursor.execute(record_check)
        records = cursor.fetchall()
    except:
        table_option = input("Entered table does not exist, Do you want to create new one (y/n)? ")
        if table_option == 'y':
            table_create = (f"create table {table_name}("
                            f"ID int not null,"
                            f"Name varchar(30) not null,"
                            f"Major varchar(30) not null,"
                            f"Tuition int not null,"
                            f"Age int not null);")
            cursor.execute(table_create)
            connection.commit()
            print(f"Table {table_name} has been created! Proceeding to entries.")
        else:
            exit()

def table_exist():
    global table_name2
    table_name2 = input("Enter table name to use: ")
    try:
        record_check = f"select * from {table_name2};"
        cursor.execute(record_check)
        record = cursor.fetchall()
    except:
        print("Table does not exist.")
        menu()

def register():
    checker()
    student_id = int(input("Enter student ID: "))
    name = input("Enter name: ")
    major = input("Enter student Major: ")
    tuition = int(input("Enter student tuition fee: "))
    age = int(input("Enter student Age: "))
    insert_statement = f"insert into {table_name} values({student_id}, {name}, {major}, {tuition}, {age});"
    cursor.execute(insert_statement)
    connection.commit()
    menu()

def delete():
    table_exist()
    student_id = int(input("Enter student ID to delete: "))
    confirmation = input("Do you want to proceed? (y/n): ")
    if confirmation == "y":
        delete_statement = f"delete from {table_name2} where ID={student_id};"
        cursor.execute(delete_statement)
        connection.commit()
        print(f"Student with {student_id} has been deleted.")
        menu()
    else:
        menu()

def update():
    table_exist()
    student_id = int(input("Enter student ID: "))
    confirmation = input("Do you want to proceed? (y/n): ")
    while confirmation == "y":
        update_field_name = input("Enter the field name you want to update: ")
        new_value = input("Enter the new value: ")
        value_update = f"update {table_name} set {update_field_name}='{new_value}' where ID={student_id};"
        cursor.execute(value_update)
        connection.commit()
        confirmation = input("Do you want to edit more values? (y/n): ")
    menu()

def search():
    table_exist()
    search_param = input("Enter the entry you want to search: ")
    search_field = f"select {search_param} from student;"
    cursor.execute(search_field)
    connection.commit()

def display_table():
    table_exist()
    print_table = f"select * from {table_name}"
    cursor.execute(print_table)
    connection.commit()

def close():
    connection.close()
    print(f"Database closed.")