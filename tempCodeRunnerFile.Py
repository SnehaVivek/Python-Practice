# Strings and Truples 

# String functions 
s = "Data Science is the best"
print(s.upper())
print(s.lower())
print(s.title())
print(s.strip())
print(s.replace('a','a_'))
print(s.split())
print(s.count('a'))
print(s.startswith('D'))


# Insert - to insert value at any position
l1=[1,2,3,4,5]
l1.insert(1,6)
print(l1)


# extend
l1.append(2)
l1.append(9)
print(l1)
print(l1[len(l1)-1])
l1.extend([8,10])
print(l1)
print(l1[len(l1)-1])


# Append - add at last
l1.append(2)
l1.append(3)
l1.append(4)
for i in range(20,30):
    l1.append(i)
print(l1)