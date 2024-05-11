#Basics Problems:
#1.
print("Hello World!\nHow are you?")

#2.
print("It's a beautiful day!")

#3.
print("He said,\"Python is awesome!\"")

#4.
print("\\")

#5.
print("Name \tAge \nAlice \t25 \nBob \t30")

#6.
print("C:\Windows\System32\drivers\etc\hosts")

#7.
print("Roses are red,\nVoilets are blue,\nSugar is sweet\nAnd so are you")

#8.
first_name = "Python"
last_name = "Programmer"
full_name = first_name + " " + last_name
print(full_name)

#9.
for i in range(5,0,-1):
    print("*" * i)

#10.
a = "Python"
print(a[2:5])

#11.


#12.
print("\tHello World")

#13.
print("CALUCULATOR FOR CALCULATE THE AREA OF RECTANGLE")
l = int(input("Enter the Length of the Rectangle (in Meter): "))
b = int(input("Enter the Breadth of the Rectangle (in Meter): "))
print("The Area of Rectangle is: "+ str(l*b) + " Sq. Meter")

#14. Challenging Problem:
user_emotion = input("How are you feeling: ")
if user_emotion == "Happy" or "happy":
    print(":)")
elif user_emotion == "Sad" or "sad":
    print(":(")
elif user_emotion == "Angry" or "angry":
    print("''")
elif user_emotion == "Surprised" or "surprised":
    print("''!")
else:
    print("Not clearly specified the emotions?")

Problem based on Variables & Data types:
#1.
user_name = "Atharva"
user_address = "Pune, Maharashtra, India"
user_age = "22"
user_contact = "7666624817"
print("I am "+user_name+". \nI am "+ user_age+" years old.\nCurrently I am living in "+ user_address+".\nMy contact number is "+user_contact+ ".\nThank you")

#2.
print("CHECKING FOR VOTER ELIGIBILITY")
age = int(input("Enter your age:"))
if age>=18:
    print("you are eligible for vote.")
elif age<18:
    print("you are not eligible for voting.")
else:
    print("Enter correct age.")

#3.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The Addition of the Numbers: " + str(num2+num1))
print("The Subtraction of the Numbers: " + str(num2 - num1))
print("The Multiplication of the Numbers: " + str(num2 * num1))
print("The Division of the Numbers: " + str(num1 / num2))

#4.
length = int(input("Enter the length of the Rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))
print("The Area of the Rectangle is: "+str(length*breadth)+" Sq. Mtr"+"\nThe perimeter of the Rectangle is: "+str(2*length + 2*breadth)+" Mtr")

#5.
print("TEMPERATURE CONVERTER")
temp1 = int(input("Enter the Temperature in Deg C: "))
temp2 = (temp1*9/5) + 32
print("The temperature in fahrenheit is: "+str(temp2))

#6.
#This will run till you stop the program
while 1>0:
#     user_name = input("Enter your Full Name: ")
#     print("The length of your the name is: " + str(len(user_name)))
#
print("Hello")