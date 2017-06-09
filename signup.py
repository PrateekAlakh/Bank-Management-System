for i in range(1,11):
    try:
        acc_type = raw_input("\nSelect Account Type (s for saving account and c for current account) : ")
        amount = int(raw_input("Amount initiated : "))
        if (acc_type is 'c' and amount < 5000) or (amount < 0):
            print("Invalid Amount")
            continue
        print("Enter your details:")
        name = raw_input("\nFull Name : ")
        gender = raw_input("\nGender (Enter m for male and f for female) : ")
        address = raw_input("\nAddress : ")
        city = raw_input("\nCity : ")
        state = raw_input("\nState : ")
        try:
            pincode = int(raw_input("\nPincode : "))
        except:
            print("Wrong input TryAgain")
            continue
        cur.execute('INSERT INTO Customer VALUES(cuno.nextval,:1,:2,:3,:4,:5,:6)',(name,gender,address,city,state,pincode))

        con.commit()

        ano = cur.execute('SELECT customer_id FROM Customer where full_name = :1 and address = :2',(name,address))
        acn = cur.fetchall()
        acn = acn[0][0]

        password = raw_input("Set Password : ")
        
        cur.execute('INSERT INTO Account VALUES(acno.nextval,:1,:2,:3,:4,0,sysdate,NULL)',(acn,password,acc_type,amount))

        con.commit()

        ano = cur.execute('SELECT account_no FROM Account where customer_id = :1 and password = :2',(acn,password)).fetchall()
        acn = ano[0][0]

        print "\nYour Account number : ",
        print acn
        print ""

        break
    except:
        print "There is some error please try again\n\n"
        continue