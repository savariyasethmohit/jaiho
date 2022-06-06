# import addfunction as ad
# var=ad.modulo(4,5)
# print(var)


# 1. connection with database.
# 2. issuing SQL statement
# 3. stored procedure
# 4.  closing the coonection

# 1. Connecting to a Data Base
# 2. Creating Tables
# 3. Insert Operation.
# 4. Update Operation.
# 5. Delete Operation.
# 6. Read Operation.
#      Fetch one()
#      Fetch all()
#      Row count()
# --------------------------------------------------------------------------------------
"""
import sqlite3

conn = sqlite3.connect("lite2.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quality INTEGER,price REAL)")
cur.execute("INSERT INTO store VALUES(Glass,8,10.5)")

conn.commit()
conn.close()
print("Connection Close.")"""
# ----------------------------------------------------------------------------------------

"""
import sqlite3

conn=sqlite3.connect ("tut2.db")
conn=sqlite3.connect ("tut355.db") # connection to a database

c=conn.cursor () # cursor creation
def create_table()
    c.execute ("CREATE TABLE IF NOT EXISTS TableName4 (Srno INTEGER, Name TEXT, studentClass TEXT, Address TEXT)")
    # query exection with help of c.execute()
def data_entry ()
    c.execute ("INSERT INTO TableName4 VALUES (1, ravi', 1, 'Jntu')")
    c.execute ("INSERT INTO TableName4 VALUES (2, srinivas 1A, Jntu)")
    print("inside data entry function")
    conn.commit() # Storing the data permanently
    c.execute ("INSERT INTO TableName4 VALUES (3, mohan, 1 kukatpally')")
    conn.commit()
    #c close ()
    conn.close ()
create_table ()
data_entry ()
"""

# ------------------------------------------------------------------------------------------
# f1 = open("abc.txt","r")
# l = f1.read()
# count = 0
# for i in l:
#     if (i=="A" or i=="B" or i=="C" or i=="c" or i=="a" or i=="b"):
#         print(i)
# f1.close()

# -------------------------------------------------------------------------------------------

# thread is a sub part of process


# Python program to illustrate the concept
# of threading
# importing the threading module
# """import threading
#
# def print_cube(num):
# 	"""
# 	# function to print cube of given num
# 	"""
# 	print("Cube: {}".format(num * num * num))
#
# def print_square(num):
# 	"""
# 	# function to print square of given num
# 	"""
# 	print("Square: {}".format(num * num))
#
# if __name__ == "__main__":
# 	# creating thread
# 	t1 = threading.Thread(target=print_square, args=(10,))
# 	t2 = threading.Thread(target=print_cube, args=(10,))
#
# 	# starting thread 1
# 	t1.start()
# 	# starting thread 2
# 	t2.start()
#
# 	# wait until thread 1 is completely executed
# 	t1.join()
# 	# wait until thread 2 is completely executed
# 	t2.join()
#
# 	# both threads completely executed
# 	print("Done!")
# """



