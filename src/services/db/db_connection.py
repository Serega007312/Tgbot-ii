import psycopg2
from src.services.db.config import host, password,user, db_name

#try:
#    connection = psycopg2.connect(
#        host=host,
#        user=user,
#        password=password,
#        database=db_name
#    )
#    connection.autocommit = True
#    print("Подключился к бд")
#    #cursor = connection.cursor()
#    with connection.cursor() as cursor:
#        cursor.execute(
#            "UPDATE users SET money = 200 WHERE id_users = 12;"
#        )
#        print(cursor.fetchone())
#        connection.close()
#    #with connection.cursor() as cursor:
#    #    cursor.execute(
#    #        "SELECT money FROM users WHERE id_users=12;"
#    #    )
#    #    print(cursor.fetchone()[0])
#    #    connection.close()
#except Exception as ex_:
#    print(ex_)
#finally:
#    #connection.close()
#    print('Соединение разорвано')

def insert_user(id):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        print("Подключился к бд")
        with connection.cursor() as cursor:
            cursor.execute(
               f"INSERT INTO users (id_users, money) VALUES ({int(id)}, 0 );"
           )
            print(cursor.fetchone())
            connection.close()
    except Exception as ex_:
        print(ex_)
    finally:
        # connection.close()
        print('Соединение разорвано')

def select_user(id):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        print("Подключился к бд")
        with connection.cursor() as cursor:
            cursor.execute(
               f"SELECT money FROM users WHERE id_users={id};"
           )
            otvet = cursor.fetchone()
            connection.close()
            return otvet

    except Exception as ex_:
        print(ex_)
    finally:
        # connection.close()
        print('Соединение разорвано')


def updata_money(id, money):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        print("Подключился к бд")
        with connection.cursor() as cursor:
            cursor.execute(
               f"UPDATE users SET money = {money} WHERE id_users = {id};"
           )
            print(cursor.fetchone())
            connection.close()
    except Exception as ex_:
        print(ex_)
    finally:
        # connection.close()
        print('Соединение разорвано')


#if __name__ == "__main__":
#    select_user(12332412)