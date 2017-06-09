#I am Admin
password = raw_input("Enter Admin Password : ")
for a1 in range(0,10):
	try:
	    if(password == "abcd"):
	        #If password matches the admin table
			print("\nAdmin Menu\n1.Print Closed Accounts History\n2. FD Report of Customer\n3. FD Report of Customer vis-a-vis another Customer\n4. FD Report w.r.t. a particular FD amount\n5. Loan Report of a Customer\n6. Loan Report of a Customer vis-a-vis another customer\n7. Loan Report w.r.t. a particular loan amount\n8. Loan - FD Report of Customers\n9. Report of Customers who are yet to avail a loan\n10. Report of Customers who are yet to open a FD account\n11. Report of Customers who neither have a loan nor a FD account\n")
			x = int(raw_input("Enter your choice : "))
			if x is 1:
				t_table = cur.execute('SELECT * FROM Account WHERE closure_date IS NOT NULL').fetchall()
				for row in t_table:
					print "Account No. : ",row[0]
					print "Customer Id : ",row[1]
					print ""
				if(t_table):
					continue
				else:
					print("No Data Found")
			elif x is 2:
				cus = int(raw_input("Enter Customer Id : "))
				a = cur.execute('SELECT * FROM FixedDeposit WHERE customer_id = :1',(cus,)).fetchall()
				for i in a:
					print i
				if(a):
					continue
				else:
					print("No Data Found")
			elif x is 3:
				cus = int(raw_input("Enter Customer Id : "))
				try:
					a = cur.execute('SELECT SUM(amount) FROM FixedDeposit WHERE customer_id = :1',(cus,)).fetchall()
				except:
					print("yelo hogya na")
				a = a[0][0]
				b = cur.execute('SELECT * FROM FixedDeposit WHERE amount > :1',(a,)).fetchall()
				for i in b:
					print i
			elif x is 4:
				amount = int(raw_input("Enter amount : "))
				a = cur.execute('SELECT customer_id, MAX(amount) FROM FixedDeposit GROUP BY customer_id').fetchall()
				for i in a:
					if(i[1]>=amount):
						b=cur.execute('SELECT * FROM Customer WHERE customer_id = :!',(i[0],)).fetchall()
						print b
			elif(x is 5):
				cus = int(raw_input("Enter Customer Id : "))
				a = cur.execute('SELECT * FROM Loan WHERE customer_id = :1',(cus,)).fetchall()
				for i in a:
					print i
			elif(x is 6):
				cus = int(raw_input("Enter Customer Id : "))
				a = cur.execute('SELECT SUM(amount) FROM Loan WHERE customer_id = :1',(cus,)).fetchall()
				a = a[0][0]
				b = cur.execute('SELECT * FROM Loan WHERE amount > :1',(a,)).fetchall()
				for i in b:
					print i
			elif(x is 7):
				amount = int(raw_input("Enter amount : "))
				a = cur.execute('SELECT customer_id, MAX(amount) FROM Loan GROUP BY customer_id').fetchall()
				for i in a:
					if(i[1]>=amount):
						b=cur.execute('SELECT * FROM Customer WHERE customer_id = :!',(i[0],)).fetchall()
						print b
			elif(x is 8):
				a = cur.execute('SELECT * FROM Customer').fetchall()
				for i in a:
					lo = cur.execute('SELECT SUM(amount) FROM Loan WHERE customer_id = :1',(i[0],)).fetchall()
					lo=lo[0][0]
					fi = cur.execute('SELECT SUM(amount) FROM FixedDeposit WHERE customer_id = :1',(i[0],)).fetchall()
					fi=fi[0][0]
					if(lo>=fi):
						print i
			elif(x is 9):
				a = cur.execute('SELECT * FROM Customer').fetchall()
				for i in a:
					f = cur.execute('SELECT * FROM Loan WHERE customer_id = :1',(i[0],)).fetchall()
					if(f):
						continue
					else:
						print i
			elif(x is 10):
				a = cur.execute('SELECT * FROM Customer').fetchall()
				for i in a:
					f = cur.execute('SELECT * FROM FixedDeposit WHERE customer_id = :1',(i[0],)).fetchall()
					if(f):
						continue
					else:
						print i
			elif(x is 11):
				a = cur.execute('SELECT * FROM Customer').fetchall()
				for i in a:
					f = cur.execute('SELECT * FROM FixedDeposit WHERE customer_id = :1',(i[0],)).fetchall()
					g = cur.execute('SELECT * FROM Loan WHERE customer_id = :1',(i[0],)).fetchall()
					if(f or g):
						continue
					else:
						print i
			else:
				if x is 0:
					x=0
				else:
					continue
			if(x is 0):
				break;
	    else:
	    	print("Wrong Password")
	except:
	    print("Oh No")
	    continue
if(x is not 0):
	print("\nSession Expired Login Again\n")