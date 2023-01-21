import sqlite3
from customers import Customers

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE customers (
            ID int,
            First_name text,
            Last_name text,
            Pay int )""")

c.execute('''CREATE TABLE albums (
            Artist text,
            Name text,
            Album_cost int )''')

c.execute('''CREATE TABLE songs (
            ID int,
            Name text,
            Duration text )''')


#def insert_customers(customer):
#    with conn:
#        c.execute("INSERT INTO customers VALUES (:ID, :First_name, :Last_name, :Pay )",
#                  {'ID': customer.ID, 'First_name': customer.First_name, 'Last_name': customer.Last_name, 'Pay': customer.Pay})


#def insert_albums(alb):
#    with conn:
#       c.execute("INSERT INTO albums VALUES (:ID, :Artist, :Name, :Album_cost )",
#                 {'ID': alb.ID, 'Artist': alb.Artist, 'Name': alb.Name, 'Album_cost': alb.Album_cost})


#def insert_song(song):
#    with conn:
#        c.execute("INSERT INTO songs VALUES (:ID, :Name, :Song)",
#                 {'ID': song.ID, 'Name': song.Name, 'Song': song.Song})


#def update_pay(customer, pay):
#   with conn:
#       c.execute("""UPDATE customers SET pay = :pay
#                    WHERE First_name = :First_name AND Last_name = :Last_name""",
#                 {'First_name': customer.First_name, 'Last_name': customer.Last_ame})


#cust = Customers('1', 'User', 'You', 10000)
#insert_customers(cust)

c.execute("INSERT INTO customers VALUES (1, 'Luka', 'G', 50000)")
c.execute("INSERT INTO customers VALUES (2, 'Alojz', 'R', 60000)")

c.execute("SELECT * FROM customers")

results = c.fetchall()

for row in results:
    print(row)

conn.commit()
conn.close()


