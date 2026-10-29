#Python code to print "Hello World"

print("Hello World!")   

#Access Private Variable from outside class 

class MyClass:
    def __init__(self):
        self.__private_variable = "I am Private"

    def get_private(self):
        return self.__private_variable
obj = MyClass()
# print(obj.__private_variable)   # This is attribute error.
#print(obj.get_private())    
print(obj._MyClass__private_variable) # used of technique is name mangling.

class MyClass:
    def __init__(self):
        self.__private_var = "I am Private Variable"

    def __private_method(self):
        return "I am private method"
    def show_private(self):
        return self.__private_var +" and "+ self.__private_method()
obj = MyClass()
print(obj.show_private())     

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # Private
        self.__balance = balance                 # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

account = BankAccount("12345", 1000)

# Direct access will fail
try:
    account.__balance += 500  # ✗ AttributeError
except AttributeError:
    print("Direct access to private variable failed!!!")

# Access using methods
print("Your account balance is: ", account.get_balance())   # ✓ 1000

account.deposit(500)
print("Your account balance after deposit is: ", account.get_balance())  # ✓ 1500cco 

# Literal in Python Integer type.

x = 0o34 
print("0o34 in octal is:",x, type(x))

x = 0X1c
print ("0X1c in Hexadecimal is", x, type(x)) 

#Using literal notation of complex number
x = 2+3j
print ("2+3j complex literal is", x, type(x))
y = 2.5+4.6j
print ("2.5+4.6j complex literal is", x, type(x))



