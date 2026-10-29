def greeting():
    "This is doc-string of this greeting functions."
    print("Hello function")
    return
greeting() 

# Default argument...........

def showinfo(name,city="Dhaka"):
    print("Name:",name)
    print("City:",city)
showinfo(name="Anish")    

# Keyword Arguments..........

def print_info(name,age):
    print("Name:",name)
    print("Age:",age)


# By keyword argument.
print_info(name="Sohag",age=26)     

# Arbitrary arguments

def students(*args):
    for name in args:
        print(name)
students("Rohim","Karim","Khalek")        

# Function annotation.

def add(a: int,b: int) ->int:
    return a + b
result = add(10,20)
print(result)
