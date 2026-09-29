avg_rating = int(input("Student average rating: "))
student_age = int(input("Student age: "))
has_debt = input("Student has debt (Y/N): ") == "N"
has_recommendation = input("Student has recommendation (Y/N): ") == "Y"

condition = (avg_rating >= 80 or (student_age > 21 and avg_rating >= 80)) and (not has_debt and (has_recommendation or (student_age > 21 and not has_debt) or (student_age <= 21 and not has_debt)))
print()
if condition:
    print("Student can receive a scholarship.")
else:
    print("Student cannot receive a scholarship.")
