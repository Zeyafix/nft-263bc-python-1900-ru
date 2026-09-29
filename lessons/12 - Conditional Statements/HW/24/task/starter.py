salary = int(input("Enter salary: "))

SALARY_MIN = 400
SALARY_MID = 1200
SALARY_MAX = 2000
tax_percent = 0

if salary >= SALARY_MIN:
    tax_percent = 5
    tax_coef = 1 - tax_percent / 100
    salary = salary * tax_coef
    has_covered_med_tax = True
    has_covered_soc_tax = True
if salary >= SALARY_MID:
    tax_percent = 10
    tax_coef = 1 - tax_percent / 100
    salary = salary * tax_coef
    has_covered_med_tax = True
    has_covered_soc_tax = False
if salary >= SALARY_MAX:
    tax_percent = 15
    tax_coef = 1 - tax_percent / 100
    salary = salary * tax_coef
    has_covered_med_tax = False
    has_covered_soc_tax = False

print(f"NET: {salary}")

if has_covered_med_tax == True:
    print("The company covers medical insurance.")
if has_covered_soc_tax == True:
    print("The company covers social insurance.")
