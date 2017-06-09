import cx_Oracle
import os
os.system('clear')
con = cx_Oracle.connect('PRO/abcd@XE')
cur = con.cursor()
for i in range(0,25):
	print("MAIN MENU")
	print("\n1. Sign Up\n2. Sign In\n3. Admin Sign In\n4. Quit\n")
	a = int(raw_input("Enter your choice : "))
	if a is 1:
	    execfile('signup.py')
	elif a is 2:
	    execfile('signin.py')
	elif a is 3:
	    execfile('adminsignin.py')
	elif a is 4:
	    print "Quitting..."
	    exit()
	else:
	    print("Try Again\n\n")