try:
	bal = cur.execute('SELECT balance FROM Account WHERE account_no = :1',(acc,)).fetchall()
	bal = bal[0][0]

	n = bal*2
	n = n - (n%1000)

	print "You can take loan upto :",n
	print "Amount shoubld be in multiple of 1000"
	x = int(raw_input("Enter amount for loan : "))
	duration = int(raw_input("Enter duration in number of months : "))

	if x <= n and x%1000 == 0 and duration >= 12:
		cur.execute('INSERT INTO Loan VALUES(lono.nextval, :1,sysdate,:2,:3)',(cus_id,x,duration))
		con.commit()
		print("Loan Successfully granted")
	else:
		print("Loan not granted")
except:
	print("Please try again\n")