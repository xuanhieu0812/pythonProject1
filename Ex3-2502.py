# year = int(input('input the number year: '))
# position = int(input('whats position: '))
# salary = 0
#
# if year >= 5:
#     if position == 1:
#         salary == 15000
#     elif position == 2:
#         salary == 11000
#     elif position == 3:
#         salary == 10000
# else:
#     if position == 1:
#         salary == 12000
#     elif position == 2:
#         salary == 10000
#     elif position == 3:
#         salary == 7000

years_of_working = int(input("years of working: "))
position = int(input("position (1,2,3):"))
salary = 0
if years_of_working >= 5:
    if position == 1:
        salary = 15000
    elif position == 2:
        salary = 11000
    elif position == 3:
        salary = 10000
else:
    if position == 1:
        salary = 12000
    elif position == 2:
        salary = 10000
    elif position == 3:
        salary = 7000
print("your salary is ", salary)



