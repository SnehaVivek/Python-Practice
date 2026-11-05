# Functions Practice Questions and Solutions

# This function calculates the area of a rectangle given its length and width. It takes two parameters, length and width, multiplies them to find the area, and returns the result. The user is prompted to input the length and width, which are then passed to the function to calculate and print the area.
def calculate_area(length,width):
    area = length*width
    return area
l=int(input("length"))
b=int(input("width"))
print(calculate_area(l,b))


# This function helps to display employee details.
def employee_detail_random(name, department, salary):
    print("name: ", name)
    print("department: ", department)
    print("salary: ", salary)
    return
n,d,s= input("Name,Department,Salary: ").split()
employee_detail_random(n,d,s)

# This function helps to display employee details in random order.
def employee_detail(name, department, salary):
    print("salary: ", salary)
    print("department: ", department)
    print("name: ", name)
    return
n,d,s= input("Name,Department,Salary: ").split()
employee_detail(n,d,s)

# This function calculates the discount on a given amount. It takes one parameter, amount, applies a first discount of 10% and then a second discount of 20% on the reduced amount, and prints the final discounted amount. The user is prompted to input the amount, which is then passed to the function to calculate and print the discounted price.
def calculate_discount(amount):
    firstdiscount = amount*0.9
    seconddiscount = firstdiscount*0.8
    print(seconddiscount)
    return
a = int(input("Amount: "))
calculate_discount(a)

# This function calculates the sum, difference, product, and quotient of two numbers. It takes two parameters, a and b, performs the calculations, and prints the results.
def calculate_operations(a,b):
   print("Add: ", a+b)
   if a>=b :
      print("Add: ", a-b)
   else: 
      print("Sub: ", b-a)
   print("Multiply: ", a*b)
   if b!=0:
      print("Divide: ", a/b)
   return
s,t = map(int, input("1st no.,2nd no. :").split())
calculate_operations(s,t)

# Function to calculate the total shopping bill, apply a default 5% discount or a custom 15% discount, and return the final payable amount.
def shopping_bill(item_price, quantity, discount=5):
    total_price = item_price * quantity
    discount_amount = total_price * discount / 100
    final_amount = total_price - discount_amount
    print("Total Price:", total_price)
    print("Discount Amount:", discount_amount)
    print("Final Payable Amount:", final_amount)
    return final_amount
print("With 5% Discount:")
shopping_bill(2000, 3)
print("\nWith 15% Discount:")
shopping_bill(2000, 3, 15)

# Global Variables

# This function adds a specified amount of money to a global balance variable and returns the updated balance. 
balance=10000
def add(money):
    global balance
    balance+=money
    return balance
print(add(2000))

# This function keeps track of how many times it has been called by using a global variable count. 
count=0
def update():
    global count
    count+=1
    return
print(update())