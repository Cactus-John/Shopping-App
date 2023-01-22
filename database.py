import sqlite3
from customers import Customers

conn = sqlite3.connect(':memory:')
c = conn.cursor()


QUERY = '''
    CREATE TABLE Shop (
        ProductName text NOT NULL,
        ProductImage IMG,
        PayEUR REAL NOT NULL 
    );
'''

c.execute(QUERY);

QUERY = '''
    INSERT INTO Shop VALUES 
    ('vinyl1', 'da.png', 20.56),
    ('iPhone13','da.png', 950),
    ('vinyl2', 'da.png', 15.23); 
'''

c.execute(QUERY)
conn.commit()

QUERY = '''
    SELECT * FROM Shop;
'''

print(c.execute(QUERY).fetchall())
