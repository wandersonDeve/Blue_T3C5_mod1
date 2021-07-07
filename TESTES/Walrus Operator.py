#   EXEMPLO WALRUS OPERATOR

#   SEM WALRUS OPERATOR USANDO IF
    #   MODO #01
nums = [10, 20, 30, 40, 50]
if len(nums):
    print(f"There are {len(nums)} elements in the list")

    #   MODO #02
nums = [10, 20, 30, 40, 50]
size = len(nums)
if size:
    print(f"There are {size} elements in the list")


#   COM WALRUS OPERATOR USANDO IF
nums = [10, 20, 30, 40, 50]

if (size := len(nums)):
    print(f"There are {size} elements in the list")

#---------------------------------------------------------------------------------#

#   SEM WALRUS OPERATOR EM LOOP WHILE
command = input("> ")
while command != "quit":
    print("Your input:", command)
    command = input("> ")


#   COM WALRUS OPERATOR EM LOOP WHILE
while (command := input(">> ")) != "quit":
     print("Your input:", command)

#---------------------------------------------------------------------------------#

#   SEM WALRUS OPERATOR EM LOOP FOR
students = [
    {"name" : "Chetan", "marks" : 475},
    {"name" : "Swathi", "marks" : 501},
    {"name" : "Nikhil", "marks" : 584},
    {"name" : "Salil", "marks" : 498},
    {"name" : "Rajat", "marks" : 590},
]

for student in students:
    percentage = (student["marks"]/700)*100
    if percentage > 70:
        print("{} has scored {:0.02f} % ".format(student["name"], percentage))


#   COM WALRUS OPERATOR EM LOOP WHILE
for student in students:
    if (percentage := ((student["marks"]/700)*100)) > 70:
        print("{} has scored {:0.02f} % ".format(student["name"], percentage))

#---------------------------------------------------------------------------------#

#   SEM WALRUS OPERATOR EM LIST COMPREHENSION
import math
[math.sin(x) for x in range(10) if math.sin(x) >= 0]


#   COM WALRUS OPERATOR EM LIST COMPREHENSION
import math
[res for x in range(10) if (res:= math.sin(x)) >= 0]
