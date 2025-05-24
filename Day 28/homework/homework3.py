

input_number = int(input("Enter a number: "))
is_prime = True
if input_number < 2:
    is_prime = False
else:
    for i in range(2, int(input_number ** 0.5) + 1):
        if input_number % i == 0:
            is_prime = False
            break
if is_prime:
    print("This is a prime number")
else:
    print("This isn't a prime number")


    