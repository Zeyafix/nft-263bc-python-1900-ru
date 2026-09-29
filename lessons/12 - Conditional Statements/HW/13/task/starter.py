from datetime import datetime

print("1. Show current date")
print("2. Show current time")
choice = int(input("Choice: "))
print("===========================")
if choice == "1":
    print(datetime.now().date())
if choice == "2":
    print(datetime.now().time())
else:
    print("Incorrect choice!")
