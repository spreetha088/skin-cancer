import mysql.connector
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_project'
)

cursor = con.cursor()

def user():
    print('''Select option:
        1. Vaccine details
        2. Death details
        3. Recovery details''')
    option = int(input("Enter your option: "))
    return option

def vaccine():
    print('''
        1. Insert data
        2. View data
        3. Update data
        4. Delete data
        5. Back to main menu''')
    select = int(input("Select one: "))
    return select

def insert():
    try:
        id_number = input("Enter your vaccination id: ")
        name = input("Enter your name: ")
        vaccine_name = input("Enter your vaccine name: ")
        no_of_dose = int(input("Enter your no. of dose: "))

        query = "INSERT INTO vaccine (id_number, name, vaccine_name, no_of_dose) VALUES (%s, %s, %s, %s)"
        val = (id_number, name, vaccine_name, no_of_dose)

        cursor.execute(query, val)
        con.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def viewdata():
    try:
        cursor.execute("SELECT * FROM vaccine")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update():
    try:
        column_name = input("Which column do you want to update: ")
        new_data = input("Enter the new data: ")
        id_number_to_update = input("Enter the vaccination id to update: ")

        query = f"UPDATE vaccine SET {column_name} = %s WHERE id_number = %s"
        val = (new_data, id_number_to_update)

        cursor.execute(query, val)
        con.commit()
        print("Updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete():
    try:
        column_name = input("Which column do you want to delete: ")
        del_data = input(f"Enter the data you want to delete in {column_name}: ")

        query = f"DELETE FROM vaccine WHERE {column_name} = %s"
        val = (del_data,)

        cursor.execute(query, val)
        con.commit()
        print("Deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def death_details():
    print('''Select one:
        1. Insert death details
        2. View death details
        3. Update death details
        4. Delete death details
        5. Back to previous menu''')
    select = int(input("Select one: "))
    return select

def death_insert():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        reason = input("Enter reason for death: ")
        date = input("Enter death date: ")
        hospital_name = input("Enter hospital name: ")

        query = "INSERT INTO covid_death (name, age, reason, date, hospital_name) VALUES (%s, %s, %s, %s, %s)"
        val = (name, age, reason, date, hospital_name)

        cursor.execute(query, val)
        con.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def death_viewdata():
    try:
        cursor.execute("SELECT * FROM covid_death")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def death_update():
    try:
        column_name = input("Which column do you want to update: ")
        data = input("Enter new data: ")
        update_name = input("Enter the name to update: ")

        query = f"UPDATE covid_death SET {column_name} = %s WHERE name = %s"
        val = (data, update_name)

        cursor.execute(query, val)
        con.commit()
        print("Updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def death_delete():
    try:
        column_name = input("Which column do you want to delete: ")
        del_data = input(f"Enter the data you want to delete in {column_name}: ")

        query = f"DELETE FROM covid_death WHERE {column_name} = %s"
        val = (del_data,)

        cursor.execute(query, val)
        con.commit()
        print("Deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def recovery_details():
    print('''Select one:
        1. Insert recovery details
        2. View recovery details
        3. Update recovery details
        4. Delete recovery details
        5. Back to previous menu''')
    select = int(input("Select one: "))
    return select

def recovery_insert():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        admitted_date = input("Enter admitted date: ")
        discharged_date = input("Enter discharged date: ")

        query = "INSERT INTO recovery_details (name, age, admitted_date, discharged_date) VALUES (%s, %s, %s, %s)"
        val = (name, age, admitted_date, discharged_date)

        cursor.execute(query, val)
        con.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def recovery_viewdata():
    try:
        cursor.execute("SELECT * FROM recovery_details")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def recovery_update():
    try:
        column_name = input("Which column do you want to update: ")
        data = input("Enter new data: ")
        update_name = input("Enter the name to update: ")

        query = f"UPDATE recovery_details SET {column_name} = %s WHERE name = %s"
        val = (data, update_name)

        cursor.execute(query, val)
        con.commit()
        print("Updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def recovery_delete():
    try:
        column_name = input("Which column do you want to delete: ")
        del_data = input(f"Enter the data you want to delete in {column_name}: ")

        query = f"DELETE FROM recovery_details WHERE {column_name} = %s"
        val = (del_data,)

        cursor.execute(query, val)
        con.commit()
        print("Deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
def admin():
    print('''
     1. View vaccine details
     2. View death details
     3. View recovery details
     4. Back to menu''')
    option = int(input("Enter your choice: "))  # Change to int
    return option

def view_vaccine():
    try:
        cursor.execute("SELECT * FROM vaccine")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def view_death():
    try:
        cursor.execute("SELECT * FROM covid_death")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def view_recovery():
    try:
        cursor.execute("SELECT * FROM recovery_details")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

while True:
    print('''ARE YOU...
        1.USER
        2.ADMIN
        3.Exit''')
    choice = input("Enter your choice: ")
    
    try:
        choice = int(choice)  # Convert the choice to an integer
    except ValueError:
        print("Invalid choice. Please enter a valid option.")
        continue

    if choice == 1:
        option = user()
        if option == 1:
            while True:
                select = vaccine()
                if select == 1:
                    insert()
                elif select == 2:
                    viewdata()
                elif select == 3:
                    update()
                elif select == 4:
                    delete()
                elif select == 5:
                    break
        # ... (Rest of your user-related code remains unchanged)
        elif option == 2:
            while True:
                select = death_details()
                if select == 1:
                    death_insert()
                elif select == 2:
                    death_viewdata()
                elif select == 3:
                    death_update()
                elif select == 4:
                    death_delete()
                elif select == 5:
                    break
        elif option == 3:
            while True:
                select = recovery_details()
                if select == 1:
                    recovery_insert()
                elif select == 2:
                    recovery_viewdata()
                elif select == 3:
                    recovery_update()
                elif select == 4:
                    recovery_delete()
                elif select == 5:
                    break
                
    elif choice == 2:
        option = admin()
        if option == 1:
            view_vaccine()
        elif option == 2:
            view_death()
        elif option == 3:
            view_recovery()
        elif option == 4:
            break
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select a valid option.")
