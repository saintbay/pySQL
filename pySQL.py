#1
import psycopg2

def read_all_rows():
    try:
        connection = psycopg2.connect(
            dbname="postgress",
            user="postgress",
            password="postgress",
            host="12312.12341.111",
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM postgress")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()
    except Exception as e:
        print("Error:", e)

read_all_rows()

#2
import psycopg2

def read_one_row(row_id):
    try:
        connection = psycopg2.connect(
            dbname="postgress",
            user="postgress",
            password="postgress",
            host="12312.12341.111",
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM postgress WHERE id = %s", (row_id,))
        row = cursor.fetchone()
        if row:
            print(row)
        else:
            print("Row not found")
        cursor.close()
        connection.close()
    except Exception as e:
        print("Error:", e)


read_one_row(1) 
#3
import psycopg2

def create_row(data):
    try:
        connection = psycopg2.connect(
            dbname="postgress",
            user="postgress",
            password="postgress",
            host="12312.12341.111",
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO postgress (column1, column2) VALUES (%s, %s)", data)
        connection.commit()  # Фиксируем транзакцию
        cursor.close()
        connection.close()
        print("Row created successfully")
    except Exception as e:
        print("Error:", e)

def update_row(row_id, new_data):
    try:
        connection = psycopg2.connect(
            dbname="postgress",
            user="postgress",
            password="postgress",
            host="12312.12341.111","
        )
        cursor = connection.cursor()
        cursor.execute("UPDATE postgress SET column1 = %s, column2 = %s WHERE id = %s", (*new_data, row_id))
        connection.commit()  
        cursor.close()
        connection.close()
        print("Row updated successfully")
    except Exception as e:
        print("Error:", e)

def delete_row(row_id):
    try:
        connection = psycopg2.connect(
            dbname="postgress",
            user="postgress",
            password="postgress",
            host="12312.12341.111",
        )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM postgress WHERE id = %s", (row_id,))
        connection.commit()  
        cursor.close()
        connection.close()
        print("Row deleted successfully")
    except Exception as e:
        print("Error:", e)


create_row(("Value1", "Value2"))  
update_row(1, ("NewValue1", "NewValue2"))  
delete_row(1)  
