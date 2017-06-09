import cx_Oracle

con = cx_Oracle.connect('PRO/abcd@XE')
cur = con.cursor()

cur.execute('drop table customer')
cur.execute('drop table account')
cur.execute('drop table transaction')
cur.execute('drop table fixeddeposit')
cur.execute('drop table loan')

cur.execute('drop sequence cuno')
cur.execute('drop sequence acno')
cur.execute('drop sequence trno')
cur.execute('drop sequence fdno')
cur.execute('drop sequence lono')

print("Everything Deleted....")

con.close()
