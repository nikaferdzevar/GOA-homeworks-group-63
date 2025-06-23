
# .append() - ამატებს ელემენტს სიის ბოლოში
# .insert() - ამატებს ელემენტს კონკრეტულ ინდექსზე
# .pop() - შლის ელემენტს სიიდან (ნაგულისხმევად ბოლოს), ასევე აბრუნებს მას





my_list = [5, 10, 15, 20, 25]
print("list lenght:", len(my_list))



numbers = []

for i in range(5):
    num = int(input(f"{i+1}) input a number cuh: "))
    numbers.append(num) 

print("your inputed numbers lil brah:", numbers) 
# ngl i forgot some things so i searched it on google and dont you dare to text me that you can help me understand and to get on a call


colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()
print("newer lsit for ya:", colors)


animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1, "monkey") 
print("new list;", animals)


students = []
for i in range(3):
    name = input(f"{i+1}) student name: ")
    students.append(name)

students.insert(0, "Teacher")
students.pop()  


print("list lenght:", len(students))
print("final form list:", students)




# wasted too much time on this bullshit :p