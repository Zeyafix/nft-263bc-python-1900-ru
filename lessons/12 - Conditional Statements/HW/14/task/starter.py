card_id = int(input("Card ID: "))
month = int(input("Month: "))
year = int(input("Year: "))
cvv_cvc = int(input("CVV/CVC: "))

test_card_id = "5869586958695869"
test_month = "03"
test_year = "28"
test_cvv_cvc = "094"

check_success = 0

if test_card_id == str(card_id):
    check_success += 1
if test_month == str(month):
    check_success += 1
if test_year == str(year):
    check_success += 1
if test_cvv_cvc == str(cvv_cvc):
    check_success += 1

print()
if check_success == 4:
    print("Success!")
if check_success == 3:
    print("Error!")
