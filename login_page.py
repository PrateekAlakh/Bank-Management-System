from datetime import datetime

cus_id = cur.execute('SELECT customer_id FROM Account WHERE account_no = :1',(acc,)).fetchall()
cus_id = cus_id[0][0]
for i in range(0,10):
    print("Choose Wisely\n\n1. Address Change\n2. Open New Account\n3. Money Deposit\n4. Money Withdrawal\n5. Transfer Money\n6. Print Statement\n7. Account Closure\n8. Avail Loan\n0. Customer Logout")
    x = int(raw_input("Enter your choice : "))
    if(x is 1):
        #Changing Address
        address = raw_input("Enter address : ")
        city = raw_input("City : ")
        state = raw_input("State : ")
        pincode = int(raw_input("Pincode : "))
        
        cur.execute('UPDATE Customer SET address = :1, city = :2, state = :3, pincode = :4 WHERE customer_id = :5',(address,city,state,pincode,cus_id))
        print("Address successfully changed\n")
        con.commit()
    elif(x is 2):
        #Open New Account
        execfile('newaccountpage.py')
    elif(x is 3):
        #Money Deposit
        amount = int(raw_input("Enter Amount to be deposited : "))
        typet = 'd'
        bal = cur.execute('SELECT balance FROM Account WHERE account_no = :1',(acc,)).fetchall()
        bal = bal[0][0]
        bal = bal + amount
        cur.execute('UPDATE Account SET balance = :1 WHERE account_no = :2',(bal,acc))
        cur.execute('INSERT INTO Transaction VALUES (trno.nextval,:1,:2,sysdate,:3,:4)',(acc,typet,bal,amount))
        con.commit()
    elif(x is 4):
        #Money Withdrawl
        perm = cur.execute('SELECT EXTRACT(MONTH FROM last_date),withdrawl_count FROM Account WHERE account_no = :1',(acc,)).fetchall()
        pern = cur.execute('SELECT EXTRACT(MONTH FROM sysdate) FROM DUAL').fetchall()
        wcount = perm[0][1]
        perm = perm[0][0]
        pern = pern[0][0]
        if(perm != pern):
            cur.execute('UPDATE Account SET withdrawl_count = 0 WHERE account_no = :1',(acc,))
        elif(wcount == 10):
            print("Permission Denied")
            continue
        amount = int(raw_input("Enter Amount to be withdrawl : "))
        typet = 'w'
        bal = cur.execute('SELECT balance,type FROM Account WHERE account_no = :1',(acc,)).fetchall()
        acc_type = bal[0][1]
        bal = bal[0][0]
        if(acc_type is 'c' and (bal-amount) < 5000):
            print('Not enough balance')
            continue
        if(bal-amount < 0):
            print('Not enough balance')
            continue
        cur.execute('UPDATE Account SET withdrawl_count = withdrawl_count+1 WHERE account_no = :1',(acc,))
        cur.execute('INSERT INTO Transaction VALUES (trno.nextval,:1,:2,sysdate,:3,:4)',(acc,typet,bal,amount))
        con.commit()
    elif(x is 6):
        #Print Statement
        date = raw_input('Enter the date (MM-DD-YYYY) : ')
        date = date.split('-')
        date = datetime(int(date[2]),int(date[0]),int(date[1]))
        a = cur.execute('SELECT * FROM Transaction WHERE account_no = :1 and transaction_time > :2',(acc,date)).fetchall()
        for row in a:
            for coloumn in row:
                print coloumn,
            print''

    elif(x is 5):
        #Transfer Money
        acc2 = int(raw_input('Enter Account No. to transfer money : '))
        a = cur.execute('SELECT account_no,balance FROM Account WHERE account_no = :1',(acc2,))
        if(a):
            amount = int(raw_input('Enter amount to Transfer : '))
            a = cur.fetchall()
            bal = a[0][1]
            my = cur.execute('SELECT balance,type FROM Account WHERE account_no = :1',(acc,)).fetchall()
            mytype = my[0][1]
            mybal = my[0][0]
            if(mytype is 'c' and (mybal-amount) < 5000):
                print('Not enough balance')
                continue
            if((mybal-amount) < 0):
                print('Not enough balance')
                continue
            mybal = mybal-amount
            #acc
            bal = bal + amount
            #acc2
            cur.execute('UPDATE Account SET balance = :1 WHERE account_no = :2',(mybal,acc))
            typet = 'w'
            cur.execute('INSERT INTO Transaction VALUES (trno.nextval,:1,:2,sysdate,:3,:4)',(acc,typet,mybal,amount))
            cur.execute('UPDATE Account SET balance = :1 WHERE account_no = :2',(bal,acc2))
            typet = 'd'
            cur.execute('INSERT INTO Transaction VALUES (trno.nextval,:1,:2,sysdate,:3,:4)',(acc2,typet,bal,amount))
            con.commit()
        else:
            exit()
    elif(x is 7):
        #Account Closure
        cur.execute('UPDATE Account SET closure_date = sysdate WHERE account_no = :1',(acc,))
        con.commit()
        break
    elif(x is 8):
        #Avail Loan
        execfile('loanapply.py')
        break
    else:
        print("Wrong Input Try Again")
        break
    if(x is 0):
        #Logout
        break