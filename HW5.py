import psycopg2


def del_db(conn, cur):
    cur.execute("""
        DROP TABLE phones;
        DROP TABLE user_info;
    """)
    print("DB Deleted")
    conn.commit()


def create_db(conn, cur):
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


def add_client(conn, cur, first_name, second_name, email):
    cur.execute(
        """INSERT into user_info (name, surname, email) values (%s, %s, %s);
        """, (first_name, second_name, email,))
    conn.commit()
    print("User", first_name, second_name, email, "Added")


def add_phone(conn, cur, user_id, phone):
    cur.execute(
        """INSERT into phones (number, user_id) values (%s, %s);
        """, (phone, user_id,))
    conn.commit()
    print("User #", user_id, phone, "Added")


def change_client(conn, cur, user_id, first_name, second_name, email):
    if first_name != None:
        cur.execute(
            """UPDATE user_info 
            SET name = %s
            WHERE id = %s;
            """, (first_name, user_id))
        conn.commit()
        print("User #", user_id, "First name changed to", first_name)
    elif second_name != None:
        cur.execute(
            """UPDATE user_info 
            SET surname = %s
            WHERE id = %s;
            """, (second_name, user_id))
        conn.commit()
        print("User #", user_id, "Second name changed to", second_name)
    elif email != None:
        cur.execute(
            """UPDATE user_info 
            SET email = %s
            WHERE id = %s;
            """, (email, user_id))
        conn.commit()
        print("User #", user_id, "Email changed to", email)
    # else:
    #     pass


def delete_phone(conn, cur, user_id):
    cur.execute(
        """DELETE FROM phones 
        WHERE id = %s;
        """, (user_id,))
    conn.commit()
    print("User #", user_id, "Phones deleted")


def delete_client(conn, cur, user_id):
    cur.execute(
        """DELETE FROM user_info 
        WHERE id = %s;
        """, (user_id,))
    conn.commit()
    print("User #", user_id, "deleted")


def find_client(cur, first_name, second_name, email):
    cur.execute(
        """SELECT name, surname, email FROM user_info 
        WHERE name = %s OR surname = %s OR email = %s;
        """, (first_name, second_name, email))
    print(cur.fetchone())


if __name__ == "__main__":
    print("""СПИСОК КОМАНД:-->>>
            "create" - создать структуру
            "del" - удалить БД
            "add client"- добавить клиента
            "add phone" - добавить телефон для существующего клиента
            "change" - изменить данные о клиенте
            "rm phone" - удалить телефоны для существующего клиента
            "rm client" - удалить существующего клиента
            "find" - найти клиента по его данным (имени, фамилии, email-у или телефону)""")

    with psycopg2.connect(database="DB", user="postgres", password="123") as con:
        while True:
            with con.cursor() as cur:
                command = input("Введите команду: ")
                if command == "create":
                    create_db(con, cur)
                elif command == "del":
                    del_db(con, cur)
                elif command == "add client":
                    first_name = input("Введите Имя: ")
                    second_name = input("Введите Фамилию: ")
                    email = input("Введите почтовый адрес:")
                    add_client(con, cur, first_name, second_name, email)
                elif command == "add phone":
                    user_id = input("Введите номер пользователя: ")
                    phone = input("Введите номер телефона: ")
                    add_phone(con, cur, user_id, phone)
                elif command == "change":
                    first_name = None
                    second_name = None
                    email = None
                    user_id = input("Введите номер пользователя: ")
                    obj = input("""
Что Вы хотите изменить?
    Имя
    Фамилия
    Почта: 
    """)
                    if obj == "Имя":
                        first_name = input("Введите Имя: ")
                    elif obj == "Фамилия":
                        second_name = input("Введите Фамилию: ")
                    elif obj == "Почта":
                        email = input("Введите почтовый адрес: ")
                    else:
                        print("Повторите попытку")
                    change_client(con, cur, user_id, first_name, second_name, email)
                elif command == "rm phone":
                    user_id = input("Введите номер пользователя: ")
                    delete_phone(con, cur, user_id)
                elif command == "rm client":
                    user_id = input("Введите номер пользователя: ")
                    delete_client(con, cur, user_id)
                elif command == "find":
                    first_name = None
                    second_name = None
                    email = None
                    obj = input("""
По какому параметру искать?
    Имя
    Фамилия
    Почта: 
    """)
                    if obj == "Имя":
                        first_name = input("Введите Имя: ")
                    elif obj == "Фамилия":
                        second_name = input("Введите Фамилию: ")
                    elif obj == "Почта":
                        email = input("Введите почтовый адрес: ")
                    else:
                        print("Повторите попытку")
                    find_client(cur, first_name, second_name, email)
                else:
                    print("Повторите попытку")
        conn.close()
