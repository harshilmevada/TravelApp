import sqlite3
from datetime import datetime


def connect_to_database():
    return sqlite3.connect('Apicalldata.db')

def create_table():
    conn = connect_to_database()
    cursor = conn.cursor()
    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS mytable (
        id INTEGER PRIMARY KEY,
        runCode TEXT,
        date TEXT,
        apiCall INTEGER
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def fistTime():
    conn = connect_to_database()
    cursor = conn.cursor()

    insert_data_query = '''
    INSERT INTO mytable (runCode, date, apiCall)
    VALUES (?, ?, ?)
    '''
    person_name = 'Api Call'
    current_date = datetime.now().date().strftime("%m-%Y")
    apiCall = 1
    cursor.execute(insert_data_query, (person_name, current_date, apiCall))
    conn.commit()
    conn.close()

def getData():
    conn = connect_to_database()
    cursor = conn.cursor()

    select_data_query = '''
    SELECT date, apiCall
    FROM mytable
    WHERE runCode = ?
    '''

    cursor.execute(select_data_query, ("Api Call",))
    result = cursor.fetchone()

    conn.commit()
    conn.close()

    if result:
        return {'date': result[0], 'apiCall': result[1]}
    else:
        return None

def updateData(newCall, newDate):
    conn = connect_to_database()
    cursor = conn.cursor()

    update_query = '''
    UPDATE mytable
    SET apiCall = ?,
        date = ?
    WHERE runCode = ?
    '''

    try:
        cursor.execute(update_query, (newCall, newDate, "Api Call"))
        conn.commit()
    except sqlite3.Error as e:
        print("Error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    # create_table()
    # fistTime()
    updateData(3, "01-2024")
    data = getData()
    if data:
        print(f"Date: {data['date']}, API Call: {data['apiCall']}")
    else:
        print("No record found for 'Api Call'.")
