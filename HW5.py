import psycopg2


def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
            DROP TABLE phones;
            DROP TABLE user_info;
        """)

        cur.execute(
            """CREATE TABLE IF NOT EXISTS user_info(
                id SERIAL PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                email VARCHAR(50) NOT NULL      
            );
            """)

        cur.execute(
            """CREATE TABLE IF NOT EXISTS phones(
                id SERIAL PRIMARY KEY,
                number INTEGER,
                user_id INTEGER REFERENCES user_info (id)    
            );
            """)
        print("DB Created")
        conn.commit()


def add_client(conn, first_name, second_name, email):
    with conn.cursor() as cur:
        cur.execute(
            """INSERT into user_info (name, surname, email) values (%s, %s, %s);
            """, (first_name, second_name, email,))
        conn.commit()
        print("User", first_name, second_name, email, "Added")


def add_phone(conn, user_id, phone):
    with conn.cursor() as cur:
        cur.execute(
            """INSERT into phones (number, user_id) values (%s, %s);
            """, (phone, user_id,))
        conn.commit()
        print("User #", user_id, phone, "Added")


def change_client(conn, user_id, first_name=None, second_name=None, email=None):
    with conn.cursor() as cur:
        cur.execute(
            """UPDATE user_info 
            SET name = %s, surname = %s, email = %s
            WHERE id = %s;
            """, (first_name, second_name, email, user_id))
        conn.commit()
        print("User #", user_id, first_name, second_name, email, "Changed")


def delete_phone(conn, user_id):
    with conn.cursor() as cur:
        cur.execute(
            """DELETE FROM phones 
            WHERE id = %s;
            """, (user_id,))
        conn.commit()
        print("User #", user_id, "Phones deleted")


def delete_client(conn, user_id):
    with conn.cursor() as cur:
        cur.execute(
            """DELETE FROM user_info 
            WHERE id = %s;
            """, (user_id,))
        conn.commit()
        print("User #", user_id, "deleted")


def find_client(conn, first_name=None, second_name=None, email=None):
    with conn.cursor() as cur:
        cur.execute(
            """SELECT name, surname, email FROM user_info 
            WHERE name = %s OR surname = %s OR email = %s;
            """, (first_name, second_name, email))
        print(cur.fetchone())

print("""СПИСОК КОМАНД:-->>>
        "create" - создать структуру БД (Старая БД сотрётся)
        "add client"- добавить клиента
        "add phone" - добавить телефон для существующего клиента
        "change" - изменить данные о клиенте
        "rm phone" - удалить телефоны для существующего клиента
        "rm client" - удалить существующего клиента
        "find" - найти клиента по его данным (имени, фамилии, email-у или телефону)""")


with psycopg2.connect(database="DB", user="postgres", password="123") as conn:
    while True:
        command = input("Введите команду: ")
        if command == "create":
            create_db(conn)
        elif command == "add client":
            first_name = input("Введите Имя: ")
            second_name = input("Введите Фамилию: ")
            email = input("Введите почтовый адрес:")
            add_client(conn, first_name, second_name, email)
        elif command == "add phone":
            user_id = input("Введите номер пользователя: ")
            phone = input("Введите номер телефона: ")
            add_phone(conn, user_id, phone)
        elif command == "change":
            user_id = input("Введите номер пользователя: ")
            first_name = input("Введите Имя: ")
            second_name = input("Введите Фамилию: ")
            email = input("Введите почтовый адрес: ")
            change_client(conn, user_id, first_name, second_name, email)
        elif command == "rm phone":
            user_id = input("Введите номер пользователя: ")
            delete_phone(conn, user_id)
        elif command == "rm client":
            user_id = input("Введите номер пользователя: ")
            delete_client(conn, user_id)
        elif command == "find":
            first_name = input("Введите Имя: ")
            second_name = input("Введите Фамилию: ")
            email = input("Введите почтовый адрес: ")
            find_client(conn, first_name, second_name, email)
        else:
            print("Повторите попытку")

conn.close()
