# 1) შექმენით 5 ელემენტიანი სია, სადაც ჩაწერთ თქვენს საყვარელი მანქანების სახელს

idk = ["mclaren", "ferrari", "mercedes", "BMW", "Toyota"]

print(idk)
# et valia

# 2) შექმენით რიცხვების სია, სადაც ჩაწერთ 0-დან 10-ის ჩათვლით ყველა ლუწ რიცხვს

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []  
for number in list:
    if number % 2 == 0:
        even_numbers.append(number)
print("even numbers are: " + str(even_numbers))

