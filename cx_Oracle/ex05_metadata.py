import cx_Oracle
import decimal


def output_type_handler(cursor, name, defaultType, size, precision, scale):
    # map all DB CLOBs to Python str
    if defaultType == cx_Oracle.DB_TYPE_CLOB:
        return cursor.var(str, arraysize=cursor.arraysize)

    # map all DB columns used for money to Python Decimal
    if name in ("RENTAL_RATE", "REPLACEMENT_COST", "AMOUNT", "PRICE"):
        return cursor.var(decimal.Decimal, arraysize=cursor.arraysize)


def query(conn):

    cursor = None
    try:
        cursor = conn.cursor()

        sql = """
        SELECT film_id, title, description, rental_rate, 
               original_language_id, last_update
        FROM film
        """

        # prior to executing sql
        # cursor.outputtypehandler = output_type_handler

        # execute query on server
        cursor.execute(sql)

        # fetch 5 rows from server
        rows = cursor.fetchmany(5)

        # https://www.python.org/dev/peps/pep-0249/#cursor-attributes
        col_names = [attrib[0] for attrib in cursor.description]
        print(col_names)

        # optional: convert tuple to nametuple
        # Row = namedtuple("Row", col_names)
        # cursor.rowfactory = lambda *args: Row(*args)

        # find the Python data type of each value in the first row
        datatypes = [type(value) for value in rows[0]]
        print(datatypes)
        print()

        for row in rows:
            print(row)

        # Python String Format Specifiers: https://pyformat.info/
        # for row in rows:
        #     print("{0}, {1:15.15}, {2:20.20}, {3}, {4}, {5}".format(*row))
        # print()

        # for row in rows:
        #     print("{0:02d}, {3!s}, {5!r}".format(*row))
        # print()

        # everything that applies to .format() applies to f-strings
        # for row in rows:
        #     print(f"{row[0]:02d}, {row[3]!s}, {row[5]!r}")
        # print()

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
