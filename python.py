# num = int(input("Enter a number:"))
#
# if num % 2 == 1:
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd.")

def classify_age(age):
    if age < 0:
        return "invalid age(age cannot be negative)"
    elif age <= 12:
        return "child"
    elif age <= 19:
        return "teenager"
    elif age <= 59:
        return "Adult"
    elif age <= 65:
        return "senior"