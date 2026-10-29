marks = int(input("Enter the number you got?: "))
result = ""

if marks < 30:
    result = "Failed"
elif marks > 80:
    result = "passed fill the all the requirements."
else:
    result = "Passed"
print("Result will be: ",result)     

# If statement problem.

discount = 0
amount = 1200

if amount > 1000:
    discount = amount * 10 / 100

print("Amount:",amount - discount)

# If else statement problem.

age = int(input("Enter the age: "))
print("Age:",age)
if age >= 18:
    print("Eligible for pay vote.")
else:
    print("Not eligible for pay vote.")   

# Another if else statement problem.

amount = 2500
discount = 0
print("Amount:",amount)
if amount > 10000:
    discount = amount * 20 / 100
else:
    if amount > 5000:
        discount = amount * 10 / 100
    else:
        if amount > 1000:
            discount = amount * 5 / 100
        else:
            discount = 0
print("Payable amount:",amount - discount)  

# Problem if elif else statement.

amount = int(input("Enter the amount: "))

if amount > 10000:
    discount = amount * 20 / 100
elif amount > 5000:
    discount = amount * 10 / 100
elif amount > 1000:
    discount = amount * 5 / 100
else:
    discount = 0
print("Payable amount:",amount - discount)                  

# Nested if statement.

num = 36 
print("Num:",num)
if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by 2 & 3")
print("Execution ended here.......")        

num=8
print ("num = ",num)
if num%2==0:
   if num%3==0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num%3==0:
      print ("divisible by 3 not divisible by 2")
   else:
      print ("not Divisible by 2 not divisible by 3")

x = int(input("Enter the number: "))
print("X:",x)

if x > 0:
    print("Entered number is positive.")
elif x < 0:
    print("Entered number is Negative.")
else:
    print("Entered number is Zero.")        

x = int(input("Enter your age: "))
y = input("Are you a citizen (yes/no)? ")
if x >= 18:
    if y.lower() == "yes":
        print("Eligible to vote.")
    else:
        print("Must be a Citizen to vote.")
else:
    print("Must be at least 18 years old to vote.")        


