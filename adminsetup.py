import cx_Oracle
con = cx_Oracle.connect('PRO/abcd@XE')
cur = con.cursor()
cur.execute('CREATE TABLE Admin (admin_id number(3),password varchar2(20)')
print("Admin Table Created Successfully...\n")

cur.execute('INSERT INTO Admin VALUES(1,'passw')')

con.commit()
