import psycopg2


def UI():
    print("Hello, Welcome to our restaurant!")
    user = input("Press 1 if you are a Customer, 2 if you are a Employee, 3 if you are a manager: ")
    if user == '1':
        phone = input("Please enter your 10 digit phone number: ")
        Customer(phone)
    elif user == '2':
        eid = input("Please enter your employee ID: ")
    elif user == '3':
        managerid = input("Please enter your manager ID: ")


def Customer(phone):
    isfound = False
    cur.execute("select * from accountholder")
    rows = cur.fetchall()
    # Checks to see if user is in database
    for r in rows:
        user_phone = r[0]
        if user_phone == phone:
            isfound = True
            break
    # Create account for user
    if isfound == False:
        firstname = input("Please enter your first name: ")
        lastname = input("Please enter your last name: ")
        email = input("Please enter your email: ")
        cur.execute("insert into accountholder (phone, firstname, lastname, email) values (%s, %s, %s, %s)",
                    (phone, firstname, lastname, email))
        print("Your account has been created!")
    # shows the users their info
    # query = "SELECT * FROM accountholder WHERE phone= '%s';" %phone
    cur.execute("SELECT * FROM accountholder WHERE phone= '%s'" % phone)
    view_accountview = cur.fetchall()
    print(view_accountview)


# def employee(eid):


# def manager(managerid):

# connect to database project in postgres
con = psycopg2.connect(
    host="localhost",
    database="Data-Diner",
    user="postgres",
    password="Password"
)

# cursor
cur = con.cursor()
UI()

# error check later, we must make sure all inputs are valid
# note: all queries must be passed as strings. psycopg2 formats it on their end as the correct format.

'''
cur.execute("insert into accountholder (phone, firstname, lastname, email) values (%s, %s, %s, %s)",
            ('9417796813', 'Marisa', 'McElhiney', 'MarisaMcElhiney4@gmail.com'))

# executing query
cur.execute("select * from accountholder")

# fetching rows of our query
# will be in format (name)
rows = cur.fetchall()

# iterating through our query
for r in rows:
    print(f"{r[0]}, {r[1]}, {r[2]}, {r[3]}")
'''
# necessary to commit all changes made from the python code
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
