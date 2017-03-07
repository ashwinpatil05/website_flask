import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost", #server IP where your database is
                           user = "root", #db user name
                           passwd = "", #Enter Your password here
                           db = "pythonprogramming")
    c = conn.cursor()

    return c, conn
		
