# Lists
# names = ['John','Smith','Andrew']
# Tuple
# names = ('John','Smith','Andrew')
# Sets
# names = ('John','Smith','Andrew')
# Dictionary
# students = {'John': 100, 'smith':300, 'Andrew':200}

# lsts

employees = ['peter','John','smith','Ruth','Esther','Annastacia']
print(employees)
print(employees[2])
print(employees[0])
print(employees[4])
print(employees[5])
print(employees[1:5])
print(employees[0:2])
print(employees[3:5])
employees[1] = 'Alex'
print(employees)
employees[3] = 'Moses'
print(employees)
employees.append('Zack')
print(employees)
employees.append('Pauline')
employees.insert(0, 'jack')
print(employees)
employees.extend(['kamau','mutua','Wafula'])
print(employees)
marks = [200,321,324,455]
print(max(marks))
print(min(marks))
print(sum(marks))
# Tuple
Languages = ('Python','Java','php','kotlin')
print(Languages)
print(Languages[1])
print(Languages[3:6])
mytuple = (1,2,3,4,5,6,7,8,9)
print(max(mytuple))
print(min(mytuple))
print(sum(mytuple))
# sets
mysets = {1,2,3,4,5,6,7,8,9}
print(mysets)
number = 4
if number in mysets:
    output = number
    print(output)
majina = {'John','Smith','Ruth','Esther'}
name = 'Esther'
if name in majina:
    jina = name
    print(jina)
name = 'Smith'
if name in majina:
    jina = name
    print(jina)
majina.add('Charles')
print(majina)
majina.update(['Njoroge','Collins','Peter'])
print(majina)
# Dictionary
Books = {
    'Title': 'The code',
    'Author':'John Doe',
    'Year Published': 2000
}
print(Books)

print(Books['Year Published'])
Books['Year Published'] = 2003
print(Books)
Books['Version'] = 'version one'
print(Books)
if 'Title' in Books:
    print('yes it is not in the dictionary')
else:
    print('No it is not in the dictionary')

# create a dictionary named 'stedents' enter necessary details that defined a student.
# Check for the existing the values in it then add one key-value pair.

# Dictionary
students = {
    'secretary': 'first student',
    'assistance': 'second student',
    'member': 'third student',
}

print(students)
if 'member 2' in students:
    print('yap there is one')
else:
    print('nop there is no one')

students['member 2'] = 'member 3'
print(students)