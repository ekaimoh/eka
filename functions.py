def my_func():
    print("Hello,welcome to my function")
my_func()

def mfunc():
    print("Are you sure you want to join?")
    print("Are you sure you want to join?")
    print("Are you sure you want to join?")
mfunc()
mfunc()
mfunc()
def my_string():
    hello = "Good Morning sir, welcome back to my application"
    print(hello)
my_string()

def my_string1(name):
    print('Hello,' + name + ' welcome back to my application')
my_string1('John')
my_string1('Estery')
my_string1('Corne')

def my_string2(name,age):
    print('Hello,' + name + ' your age is ' + str(age) + 'years')
my_string2('Moses',21)
my_string2('Trecy',34)

def person(firstname,lastname,age):
    print('Hello,' +  firstname + '' + lastname + ' your age is ' + str(age) + 'years')
person('Adebah', ' Lolung', 45)
# person(lastname='Njoroge', age = 34,Firstname='Musa')

# Create a function that takes in two numbers and perform the
# summation then display


def calc_multiple(x,y):
    return x*y

print(calc_multiple(10,20))
print(calc_multiple(34,.67))

def calc_age(a,b):
    c=a+b
    return c
print(calc_age(10,21))

def add_five(age):
    next_five_years = age+5
    return next_five_years
specific_age = add_five(23)
print(specific_age)

def calc_your_age(name,age):
    if age >5 and age<7:
        print(f'{name}you can move to Grade 1')
    elif age == 5:
        print(f'{name} you can join kindergarten')
    elif age<=4 and age>0:
        print(f'{name} can stay at home')

print(calc_your_age('Sam',6))
print(calc_your_age('Jane',2))

# create a function called great that takes a person name as
# an argument and returns a greating message.if th name is 'Alice' or 'Bob' the function
# should return a personalised greating.For any another name it should
# return a greatic greating.
def great(name):
    if name == 'Alice':
        return f"Hello, Alice! Nice to see you again."
    elif name == 'Bob':
        return f"Hello, Bob! How's it going?"
    else:
        return f"Greetings, {name}! Hope you're having a great day."

# Example usage:
print(great('Alice'))  # Output: Hello, Alice! Nice to see you again.
print(great('Bob'))    # Output: Hello, Bob! How's it going?
print(great('John'))   # Output: Greetings, John! Hope you're having a great day.
