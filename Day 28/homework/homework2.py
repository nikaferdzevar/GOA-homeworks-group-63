greater_th_ten = 0

for i in range(3):
    num = int(input("Enter number: "))
    if num > 10:
        greater_th_ten += 1

if greater_th_ten == 3:
    print("All the numbers that are larger than ten.")
else:
    print("Some numbers that are less than or equal to ten.")


