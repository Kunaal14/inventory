import pandas
from pandas import DataFrame
from pandas import Series
stock = {}

already_ate =  []
food_record = []

#food = input("What food was eaten : ")
#person = input("Who ate the food? ")

def menu():
	print("\n")
	print("press 1: To add stock")
	print("press 2: To check stock in inventory")
	print("press 3: To enter purchase")
	print("press 4: To check the coustomers who ate food")
	print("press q: To quit the program")
	print("\n")
	


def add_stock():
	while True:
		
		adding = input("\nWhat food to be added to the stock : (---TO EXIT TYPE 'quit'---)")
		add_stock = adding.upper()
		if add_stock == "QUIT"  :
			break

		try:
			new_amount = int(input("quantity of the food added to the stock "))
		#accountant_name = input("Enter yout name ")
		#stock.update({add_stock: +amount})
			if add_stock in stock:
				amount = stock[add_stock]
				amount += new_amount
				stock[add_stock] = amount
			else:
				stock[add_stock] = new_amount
		except (ValueError, TypeError) as err:
			print('---------------Enter valid amount--------------')


	
	
	


def check_stock():
	#for key, value in stock.items():
	#	print("{}:{}".format(key, value))
	updated_stock = Series(stock)
	print(updated_stock)


def enter_purchase():
	while True:
		string = input("\nWhat food was taken : (---TO EXIT TYPE 'quit'---)")
		food = string.upper()
		if food == "QUIT":
			break
		food_eater = input("Who ate the food? ")
		try:
			how_much = int(input('How much food was taken : '))
		except (ValueError, TypeError) as err:
			print('----------Enter valid amount--------------\n')
		
		person = food_eater.upper()
		if food in stock:
			#if person in already_ate:
			#	print('{} is sent to brig'.format(person))
			#else:
			if stock[food] > 0 :
				stock[food] -= how_much
				already_ate.append(person)
				food_record.append(food)
				#print(already_ate)
				#print(food_record)
				record = Series(person, index = food_record)
				print(record)
				print("\n{} ate {}".format(person, food))
			else:
				print("\n{} does not ate as we are out of {}".format(person, food))
			
		else:
			print("\n{} are out of stocks".format(food))




def coustomers():
	coustomers = Series(already_ate)
	print(coustomers)




while True:
	menu()
	num = input("What would you like to do?  ")

	if num == '1':
		add_stock()
	elif num == '2':
		check_stock()
	elif num == '4':
		coustomers()
	elif num == '3':
		enter_purchase()
	elif num == 'q':
		break

print('\nthe program has ended')




