import cx_Oracle


def query(conn):

    cursor = None
    try:
        cursor = conn.cursor()

        sql = """
        SELECT first_name, last_name
        FROM actor
        WHERE last_name = 'AKROYD'
        ORDER BY last_name, first_name
        """

        # execute query on server
        cursor.execute(sql)

        # fetch one row from server
        row = cursor.fetchone()
        print(row)

        # fetch one row from server
        row = cursor.fetchone()
        print(row)

    except cx_Oracle.DatabaseError as err:
        print(err)
    finally:
        if cursor:
            cursor.close()


def main():

    conn = None
    try:
        conn = cx_Oracle.connect(
            "sakila", "sakila", "localhost/orclpdb1.localdomain", encoding="UTF-8"
        )
        query(conn)
    except Exception as err:
        print(err)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
