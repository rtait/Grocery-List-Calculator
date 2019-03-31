

'''
The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop through the grocery list
Section 3 - provide output to the console
'''

#Creating the empty data structures
grocery_item = {}
grocery_history = []

#Variable used to check if the while loop condition is met
stop = 'go'
#q is entered by user when the list is complete
while stop!='q':

  # input of the name of the grocery item purchased.
  item_name=input('Item name: \n')
    
  # input of the quantity of the grocery item purchased.
  quantity=input("Quantity purchased: \n")
    
  # input of the cost of the grocery item input (this is a per-item cost).
  cost=input("Price per item: \n")

  #Adding data to the dictionary
  grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)};


    #Add the grocery_item to the grocery_history list using the append function
  grocery_history.append(grocery_item.copy())
    #input from the user to complete or continue loop
  stop=input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")

#variable to hold the total amount
grand_total=0;
#'for' loop 

for index, item in enumerate(grocery_history):
  
  #Calculate the total cost for the grocery_item.
  item_total = float(item['price']*item['number']);
  #Add the item_total to the grand_total
  grand_total = (grand_total + item_total);
  #Output the information for the grocery item to match this example:
  print('%d %s @ %.2f ea $%.2f' % (item['number'], item['name'],item['price'], item_total))
  #2 apple	@	$1.49	ea	$2.98
 
  
  #Setting the item_total equal to 0
item_total=0
#Print the grand total
print(str('Grand total: $%.2f' % grand_total))


