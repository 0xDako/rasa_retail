import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE orders
#              (text, trans text, symbol text, qty real, price real)''')


# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# EXISTING ORDERS
# Create table
c.execute('''CREATE TABLE orders
             (order_date, order_number, order_email, color, size, status)''')

# data to be added
purchases = [('2006-01-05',123456,'example@rasa.com','blue', 9, 'shipped'),
             ('2021-01-05',123457,'me@rasa.com','black', 10, 'order pending'),
             ('2021-01-05',123458,'me@gmail.com','gray', 11, 'delivered'),
            ]

# add data
c.executemany('INSERT INTO orders VALUES (?,?,?,?,?,?)', purchases)

# AVAILABLE INVENTORY
# Create table
c.execute('''CREATE TABLE inventory
             (size, color)''')

# data to be added
inventory = [(7, 'blue'),
             (8, 'blue'),
             (9, 'blue'),
             (10, 'blue'),
             (11, 'blue'),
             (12, 'blue'),
             (7, 'black'),
             (8, 'black'),
             (9, 'black'),
             (10, 'black')
            ]

# add data
c.executemany('INSERT INTO inventory VALUES (?,?)', inventory)

c.execute('''CREATE TABLE roles
            (id, name)''')

roles = [(1, 'admin'),
        (2, 'seller'),
        (3,'customer')]

c.executemany('INSERT INTO roles VALUES (?,?)', roles)


c.execute('''CREATE TABLE users 
    (id, login, password, role,
    FOREIGN KEY(role) REFERENCES roles(id))''')


users = ([1,'loginAdmin', 'passwordAdmin', 1],
        [2,'loginSeller', 'passwordSeller', 2],
        [3,'loginCustomer', 'passwordCustomer', 3])

c.executemany('INSERT INTO users VALUES (?,?, ?, ?)', users)


c.execute('''CREATE TABLE currentUser
    (user,
    FOREIGN KEY(user) REFERENCES users(id))''')



# Save (commit) the changes
conn.commit()

# end connection
conn.close()