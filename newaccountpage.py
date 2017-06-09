for i in range(1,10):
    print('Open New Account')
    print("1. Open Saving Account\n2. Open Current Account\n3. Open FD Account")
    try :
        x = int(raw_input("Enter your choice : "))
    except:
        print("Wrong Input Try Again")
        continue
    if x is 1:
        #open saving account
        acc_type = 's'
        amount = int(raw_input("Enter amount : "))
        if(amount<0):
            print("Wrong Input\n")
            continue

        password = raw_input("Set Password : ")
        
        cur.execute('INSERT INTO Account VALUES(acno.nextval,:1,:2,:3,:4,0,sysdate,NULL)',(cus_id,password,acc_type,amount))

        con.commit()

        # acn = cur.execute('SELECT account_no FROM Account where customer_id = :1 and password = :2',(cus_id,password)).fetchall()
        # acn = acn[0][0]

        acn = cur.execute('SELECT acno.currval FROM dual').fetchall()
        acn = acn[0][0]

        print "\nYour Account number : ",
        print acn
        print ""
        break
    elif x is 2:
        #open current account
        acc_type = 'c'
        try:
            amount = int(raw_input("Enter amount : "))
        except:
            print("Wrong Input")
            continue
        if(amount<0):
            print("Wrong Input\n")
            continue

        password = raw_input("Set Password : ")
        
        cur.execute('INSERT INTO Account VALUES(acno.nextval,:1,:2,:3,:4,0,sysdate,NULL)',(cus_id,password,acc_type,amount))

        con.commit()

        # ano = cur.execute('SELECT account_no FROM Account where customer_id = :1 and password = :2',(cus_id,password)).fetchall()
        # acn = acn[0][0]
        
        acn = cur.execute('SELECT acno.currval FROM dual').fetchall()
        acn = acn[0][0]



        print "\nYour Account number : ",
        print acn
        print ""
        break
    elif x is 3:
        #open FD account
        try:
            amount = int(raw_input("Enter the amount : "))
            duration = int(raw_input("Enter duration in number of months : "))
        except:
            print("Wrong Input")
            continue
        if amount < 1000:
            print("Invalid Amount")
            continue
        cur.execute('INSERT INTO FixedDeposit VALUES(fdno.nextval, :1,sysdate,:2,:3)',(cus_id,amount,duration))
        con.commit()
        break
    elif x is 0:
        break
    else:
        print("Wrong Input Try Again")
        continue