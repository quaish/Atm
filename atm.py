print("Welcome to ATM")
card=input("insert u r card: ")
am = 20000
if card == "yes" :
	lan= input("Enter u r language: ")
	if lan == "english" or lan == "hindi":
		pin = int(input("Enter u r 4 dight pin: "))
		if pin == 5050:
			print('1 - Withdraw')
			print("2 - Balance enquiry")
			print("3 - Deposite")
			ch =int(input("Choose transactions: "))
			if ch == 1 :
				wdraw = int(input("Enter withdraw amount: "))
				print('take u r amount: ',wdraw)
				print("now u r avlable amount is: ",am - wdraw)
			elif ch == 2 :
				print("Your avlable amount: ",am)
			elif ch == 3 :
				depo =int(input("Enter amount u want to deposite: "))
				if depo > 0 :
					print("New amount is: ",depo + am)
				else:
					print("invalid amount")
			else:
				print("worng choice")
# https://www.slideshare.net/DGMediaSchool/gerbners-model-of-communicationpp