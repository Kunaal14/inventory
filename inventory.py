stock = {'apples':30, 'oranges':22, 'mangoes':23}
already_ate = ['john']

#food = input("What food was eaten : ")
#person = input("Who ate the food? ")

def menu():
	print("\n\n")
	print("press 1: To add stock")
	print("press 2: To check stock")
	print("press 3: To enter purchase")
	print("press q: To quit the program")
	print("\n\n")
	


def add_stock():
	add_stock = input("What food to be added to the stock ")
	amount = int(input("quantity of the food added to the stock "))
	stock[add_stock] += amount
	


def check_stock():
	for key, value in stock.items():
		print("{}:{}".format(key, value))
	


def enter_purchase():
	food = input("What food was eaten : ")
	person = input("Who ate the food? ")
	if food in stock:
		if person in already_ate:
			print('{} is sent to brig'.format(person))
		else:
			if stock[food] > 0 :
				stock[food] -= 1
				already_ate.append(person)
				print(already_ate)
				print("{} ate {}".format(person, food))
			else:
				print("{} does not ate as we are out of {}".format(person, food))
			
	else:
		print("{} are out of stocks".format(food))




while True:
	menu()
	num = input("What would you like to do?  ")

	if num == '1':
		add_stock()
	elif num == '2':
		check_stock()
	elif num == '3':
		enter_purchase()
	elif num == 'q':
		break

print('the program has ended')




