import cx_Oracle

con = cx_Oracle.connect('PRO/abcd@XE')
cur = con.cursor()
cur.execute('CREATE TABLE Customer(customer_id number(16) primary key,full_name varchar2(50),gender varchar(1),address varchar2(100),city varchar2(20),state varchar2(20),pincode number(6))')
print("Customer Table Created Successfully...\n")

cur.execute('CREATE TABLE Account(account_no number(16) primary key,customer_id number(16),password varchar2(50),type varchar2(1),balance number(10),withdrawl_count number(2),last_date date,closure_date date)')
print("Account Table Created Successfully...\n")

cur.execute('CREATE TABLE Transaction(transaction_id number(10) primary key,account_no number(16),type varchar2(1),transaction_time date,balance number(10),amount number(10))')
print("Transaction Table Created Successfully...\n")

cur.execute('CREATE TABLE FixedDeposit (fd_id number(6) primary key,customer_id number(16),created_time date,amount number(10) ,duration number(4))')
print("FixedDeposit Table Created Successfully...\n")

cur.execute('CREATE TABLE Loan(loan_id number(6) primary key,customer_id number(16),created_time date,amount number(10), duration number(4))')
print("Loan Table Created Successfully...\n")

cur.execute('Create sequence cuno start with 1 increment by 1 minvalue 1')
print("Customer Id Sequence Created Successfully...\n")

cur.execute('Create sequence acno start with 1 increment by 1 minvalue 1')
print("Account Number Sequence Created Successfully...\n")

cur.execute('Create sequence trno start with 1 increment by 1 minvalue 1')
print("Transaction Id Sequence Created Successfully...\n")

cur.execute('Create sequence fdno start with 1 increment by 1 minvalue 1')
print("FD Id sequence created successfully...\n")

cur.execute('Create sequence lono start with 1 increment by 1 minvalue 1')
print("Loan Id sequence created successfully...\n")

con.close()