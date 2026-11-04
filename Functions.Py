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

