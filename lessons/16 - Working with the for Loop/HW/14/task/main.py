rows = int(input("Row count: "))
seats = int(input("Seats per row: "))
row = 1
while row <= rows:
    seat = 1
    while seat <= seats:
        print(f"Row {row}, seat {seat}")
        seat += 1
    row += 1
