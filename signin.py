for i in range(0,3):
    try:
        acc = int(raw_input("Enter your Account Number : "))
        password = raw_input("Enter Password : ")
    except:
        continue
    try:
        a = cur.execute('SELECT password FROM Account WHERE account_no = :1 and closure_date is NULL',(acc,))
    except:
        print("Database error")
        continue
    a = cur.fetchall()
    if(a):
        a = a[0][0]
        
        if(a == password):
            execfile('login_page.py')
            break
        else:
            print('Wrong password try again')
    else:
        print("Invalid Account Number")
