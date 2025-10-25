#سوال اول

Name = input("enter your name: ")
Lname = input("enter your last name: ")
Age = input("enter your age: ")
Height = input("enter your height: ")

print (f"your name: {Name} \n your last name: {Lname} \n your age: {Age} \n your height: {Height}")


#سوال دوم

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

print ((num1 * num2) , (num1 + num2) , (num1 - num2))


#سوال سوم

Full_Name = "Amirhossein Zare"
Last_Name = Full_Name.split(" ")[1]

print (Last_Name)


#سوال چهارم

Numbers = input("enter 3 len number: ")
Sum = int(Numbers[0]) + int(Numbers[1]) + int(Numbers[2])

print (Sum)


#سوال پنجم

text = input("enter a string: ")

print(text[0] == text[-1])


#سوال ششم

grades = []

n1 = float(input("enter grade one: "))
n2 = float(input("enter grade two: "))
n3 = float(input("enter grade three: "))

grades.append(n1)
grades.append(n2)
grades.append(n3)

print("grades: ", grades)

average = (n1 + n2 + n3) / 3
print("average of grades: ", average)