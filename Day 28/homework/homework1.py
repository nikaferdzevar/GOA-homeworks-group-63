positive_count = 0
negative_count = 0

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("Positive numbers count: ", positive_count)
print("Negative numbers count: " , negative_count)
