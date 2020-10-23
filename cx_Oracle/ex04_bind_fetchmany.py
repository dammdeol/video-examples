import cx_Oracle


def query(conn):

    cursor = None
    try:
        cursor = conn.cursor()

        # use bind variable
        sql = """
        SELECT first_name, last_name
        FROM actor
        WHERE last_name = :last_name
        ORDER BY last_name, first_name
        """
        # demo sql error by changing above

        # assume name came from user input or another program
        name = "AKROYD"

        # execute query on server supplying the bind variables
        cursor.execute(sql, last_name=name)
        # demo execute error by changing above

        # DO NOT construct SQL string using string formating
        # or string concatentation involving user input
        # This would create a possible SQL Injection security risk
        # https://cx-oracle.readthedocs.io/en/latest/user_guide/sql_execution.html#sql-queries

        # fetch all rows from server
        rows = cursor.fetchall()

        for row in rows:
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

