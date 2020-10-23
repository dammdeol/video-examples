import cx_Oracle


def query(conn):

    cursor = None
    try:
        cursor = conn.cursor()

        sql = """
        SELECT film_id, title, description, rental_rate, 
               original_language_id, last_update
        FROM film
        """

        # execute query on server
        cursor.execute(sql)

        # fetch 10 rows from server
        rows = cursor.fetchmany(5)

        for row in rows:
            print(row)

        # find the Python data type of each value in the first row
        datatypes = [type(value) for value in rows[0]]

        # find the db fieldname of each value
        fieldnames = [field[0] for field in cursor.description]
        tmp = cursor.description

        d = dict(zip(fieldnames, datatypes))
        print(d)
        print()

        # https://www.python.org/dev/peps/pep-0249/#cursor-attributes
        for field in cursor.description:
            for attribute in field:
                print(attribute)

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
