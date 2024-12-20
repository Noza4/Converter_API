import pyodbc


def db_connection():
    try:
        return pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=Nika\\SQLEXPRESS;'
            'DATABASE=Converter_db;'
            'Trusted_Connection=yes;'
        )
    except pyodbc.Error as e:
        raise ConnectionError(f"Database connection failed: {e}")


def search(query: str, params):

    conn = db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    except pyodbc.Error as e:
        raise RuntimeError(f"Error Executing Query: {e}")
    finally:
        conn.close()


def add(query, params):

    conn = db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            cursor.commit()
            return f"User Added Successfully"
    except pyodbc.Error as e:
        return RuntimeError(f"Error Executing Query: {e}")
    finally:
        conn.close()


def save(query, params):

    conn = db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            cursor.commit()
            return f"Transaction Added Successfully"
    except pyodbc.Error as e:
        return RuntimeError(f"Error Executing Query: {e}")
    finally:
        conn.close()
