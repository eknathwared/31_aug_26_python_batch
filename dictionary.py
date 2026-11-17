# # pop(k), popitem()

# d = {1: "python", 2: "java", 'a': "apple"}

# x = d.popitem()

# print(x)
# print(d)

# d1 = {1: "python", 2: "java"}

# d2 = {3: "da"}

# d1.update(d2)

# print(d1)

# string = input("Enter a string: ")

# frequency = {}

# for letter in string:
# if letter.isalpha():
# frequency[letter] = frequency.get(letter, 0) + 1

# print("Occurrences of each letter:")

# for letter, count in frequency.items():
# print(letter, ":", count)



def add():
    n1=int(input("enter first number: "))
    n2=int(input("enter second number: "))
    n3=n1+n2
    return n3,n2,n1

def add(a, b):
    c = a + b
    return c

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)

print("Addition is:", result)
