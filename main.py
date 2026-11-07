import psycopg2

try:
    connection = psycopg2.connect(
        dbname="estateagency_db",
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432",
    )

    print("PostgreSQL connected successfully!")

    connection.close()

except Exception as e:
    print("Database error:", repr(e))