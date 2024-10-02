#User Input Data Processor

#Task 1:Input Length Validator

first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()

if len(first_name) > 2 and len(last_name) > 2:
    print(first_name, last_name)
else:
    print("First and Last name must be more than 2 characters.")