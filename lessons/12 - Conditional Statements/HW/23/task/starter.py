a = 0

b = int(input("Enter work experience (full years):"))
if b >= 10:
    a += 10
if b >= 1:
    a += b

c = input("Enter education (1 – specialized, 2 – basic, 3 – none):")
if c == 1:
    a += 2
elif c == 2:
    a += 1
else:
    a += 0

print()
print("Rate the skill level on a scale of 1 to 8, where 1 is a low level and 8 is a high level.")
d = int(input("Enter communication skill level: "))
e = int(input("Enter technical skill level: "))
f = int(input("Enter leadership skill level: "))
g = int(input("Enter the level of analytical abilities: "))
h = int(input("Enter the teamwork level: "))

j = (d + e + f + g + h) // 5

if d <= 3:
    print("- There are communication issues.")
elif e < 5:
    print("- Technical skills are weak.")
elif f < 3:
    print("- Lacks leadership skills.")
elif g < 5:
    print("- Weak analytical skills.")
elif h < 4:
    print("- Teamwork is weak.")

print()
if 0 <= a and a <= 5:
    print("Candidate's level is low; hiring is not recommended.")
if 5 <= a and a <= 10:
    print("The candidate is at a mid-level; additional training and development are required.")
if 10 <= a and a <= 16:
    print("The candidate is of a high caliber; recommendation to consider them for the position.")
if 16 <= a and a <= 20:
    print("The candidate is highly qualified; hiring is recommended.")
