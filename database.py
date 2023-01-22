import sqlite3


def sql_database():
    conn = sqlite3.connect('shop.db')
    conn.execute('''CREATE TABLE Shop_db (
                        NAME  BLOB NOT NULL,
                        PASSWORD  BLOB NOT NULL
                ); ''')
    conn.commit()
    conn.close()


def create_user(username, password):
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    params = (username, password)
    cursor.execute("INSERT INTO Shop_db VALUES (?,?)", params)
    conn.commit()
    print('User Creation Successful')
    conn.close()


def data_retrieval(username, password):
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Shop_db WHERE NAME =:NAME", {'NAME': username})
    if cur.fetchone()[1] == password:
        print('LogIn Successful')


def data_update(username):
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    password = input("Enter the new password")
    cur.execute("""UPDATE Shop_db SET PASSWORD = :PASSWORD WHERE NAME =:NAME """,
                {'PASSWORD': password, 'NAME': username})
    print("Update Successful")
    conn.commit()
    conn.close()


def data_delete(username):
    conn = sqlite3.connect('shop.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM Shop_db WHERE NAME =:NAME """, {'NAME': username})
    print("User deletion Successful")
    conn.commit()
    conn.close()


sql_database()
username = input("Your amazon email: ")
password = input("Your amazon password: ")
create_user(username, password)

