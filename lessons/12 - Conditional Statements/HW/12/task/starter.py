code = input("Enter code: ")

first_digit = code // 100 % 10

print()
if first_digit == 0:
    print("Input error")
if first_digit == 1:
    print("Informational")
if first_digit == 2:
    print("Success")
if first_digit == 3:
    print("Redirection")
if first_digit == 4:
    print("Client Error")
if first_digit == 5:
    print("Server Error")
if first_digit > 6:
    print("Input error")
