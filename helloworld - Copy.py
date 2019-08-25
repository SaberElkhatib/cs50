"""mylist = ("list1", "list2", "list3")
mytuple = ["tuple1", "tuple2", "tuple3"]
myset = {"set1", "set2", "set3"}

print(mylist)
print(mytuple)
print(myset)

myset.update(mylist)
print(myset)"""
"""def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(5)"""
"""
class Student:
  def __init__(self, fname, lname):
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

"""
#The program can continue, without leaving the file object open
"""print("Type your name.")
x = input()
print("Hello, ",x)"""
"""fileName = "test.txt"
f = open(fileName, "a")
print("add your inputes to the file",fileName)
myinput = "\n\n" + input()
f.write(myinput)
f.close()

#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())
"""

"""
#Creating Data Base:

#Creating the text file
print("Type the method for openning the file r for Read, w for Write, a for append")
method = input()
# testing the methode
if method == "w" or method == "a" :
	
	f = open("database.txt", method)

#gettig the first name
	print("Enter your First Name and press Enter")
	fName = input()

#getting the last name
	print("Enter your Last Name and press Enter")
	lName = input()

#getting the age
	print("Enter your age and press Enter")
	age = input()

#concatinating the inputs in a sentence
	txt = "\nHello " + fName + " " + lName + ",Your Age is " + age

#writing the sentene to the file
	f.write(txt)
	f.close()

#opening the file for reading
	f = open("database.txt", "r")
	print(f.read())

#closing the file after reading
	f.close()

#for any other input for the opening method rather than w or a
else:
	f = open("database.txt", "r")
	print(f.read())
"""
""""
import os
print("Enter the file nam with extension to check if it exists")

fileName = input()
if os.path.exists(fileName):
	message = "File named: " + fileName + " exists type remove and press Enter to remove"
	print(message)
	response = input()
	if response == "remove":
		os.remove(fileName)
	else:
		print("Invalid Response")
else:
	message = "File named: " + fileName + " does not exist, make sure of the file name and file extension" 
	print(message)"""


import mysql.connector

mydb = mysql.connector.connect (
	host = "localhost",
	user = "root",
	passwd = "$@ber48C@10",
	database = "mypythondatabase2"
)

mycursor = mydb.cursor()
"""
sql = "DELETE FROM customers WHERE address LIKE %s"
addr = ("%s", )
mycursor.execute(sql, addr)

adding = "INSERT INTO customers (name, Address) VALUES(%s,%s)"
name = ("AA Saber", "Giza")
mycursor.execute(adding, name)
"""
sql = "UPDATE customerS SET name= %s WHERE name= %s"
val = ("Saber", "AA Saber")
mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM customers ORDER BY name LIMIT 10")
result = mycursor.fetchall()

mydb.commit()
for x in result:
	print(x)