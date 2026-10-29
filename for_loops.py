zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
simple is better than complex.
complex is better than complicated.
"""
for char in zen:
    if char not in "aeiou":
        print(char,end="") 

# Python for tuples.

numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0

for num in numbers:
    total += num
print("Total:",total)     

# Python for Loop with Lists

numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0

for num in numbers:
    if num % 2 == 0:
        print("numbers divisible by 2 :",num) 

# Python for Loop with Range Objects

for num in range(5):
   print (num, end=' ')
print() 

