n = int(input())
if n%2 ==0 : 
  print("Even")
else:
  print("Odd")

n = int(input("Number: " ))
if n>0 : 
  print("Positive")
elif n<0:
  print("Negative")
else:
  print("Zero")

a = int(input("First no."))
b = int(input("Second no."))
if a>b : 
  print(a)
elif b>a :
  print(b)
else :
  print(a)

b = int(input("Balance"))
w = int(input("Withdraw"))
if b>0 && b>=w :
   print("Possible")
else:
   print("Not Possible")

a = int(input(" Type your Age"))
if a>=18 : 
   print("Eligible to vote")
else :
   print(18-a, " many more yaers left to vote")

a= int(input("1st no."))
b= int(input("2st no."))
c= int(input("3st no."))
if a>b :
   if a>c :
      print("largest no.", a)
   elif a==c:
      print("largest no.", a)
   else:
      print("largest no.", c)
elif a==b and a>c:
   print("largest no.", a)
else:
   if b>c:
     print("largest no.", b)
   elif b==c:
      print("largest no.", b)
   else:
      print("largest no.", c)

u= int(input("Units consumed"))
if u<=100 and u>=0:
   print("cost: " , u*5)
if u>100 and u<=200:
   print("cost: ", u*7)
if u>200:
   print("cost: ", u*10)
