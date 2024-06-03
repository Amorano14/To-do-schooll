import random as rn

try:
    your_name = input("What is your name ? \n - ")
except IndentationError:
    print("Write smth")
    quit()

if not your_name.isalpha():
    print("You must name yourself bruh")
    quit()

try:
    good_student = int(input("Are you good student , rate you from 1-10 \n - "))
except IndentationError and ValueError:
    print("Write smth , that int")
    quit()

if  good_student > 10 or good_student < 1:
    print("You must rate yourself from 1 to 10 , lol")
    quit()

do_dict={"Wake up":7,
         "Brush teeth":7.5,
         "Breakfast":7.75,
         "Go school":8,
         "Return from school":14,
         "Lunch Time":14.25,
         "Show mark":14.75,
         "Doing homework":20,
         "Shower":22,
         "Sleep":23
         }

punish_dict = {"Go outside":5,"Read books":3,"Help in garden":2,"Help dad":1,"Help mum":1,"Cook dinner":1}

try:
    num_of_marks = int(input(f"{your_name} , how many marks are you got today ? \n - "))
except IndentationError and ValueError:
    print("Write smth")
    quit()

if num_of_marks < 0 or num_of_marks > 10:
    print("You must type number => 0 , and <= 10")
    quit()

marks = []
marks_average = 0
sum_marks = 0

for i in range(num_of_marks):
    marks.append(rn.randint(1*good_student,10))
    sum_marks += marks[i]

marks_average = sum_marks//num_of_marks

one_time = int(do_dict.get("Show mark")+0.25)
sec_time = do_dict.get("Doing homework")
ideal_free_time = sec_time-one_time
free_time = int((sec_time-one_time)-5*(10-marks_average)/9)
punish_time = ideal_free_time-free_time
count_punish_time = 0
punish_ch = list(punish_dict.keys())
one_time_cop = one_time

while punish_time > 0:
    rand_punish = rn.choice(punish_ch)
    rand_punish_time = punish_dict.get(rand_punish)
    count_punish_time = rand_punish_time
    if count_punish_time > punish_time:
        continue
    punish_time -= count_punish_time
    do_dict.update({rand_punish:one_time_cop})
    one_time_cop += rand_punish_time

do_dict.update({"Play Computer":one_time_cop})

what_do = list(do_dict.keys())
time_do = list(do_dict.values())

for i in range(len(what_do)):

    for j in range(0, len(what_do) - i - 1):

      if time_do[j] > time_do[j + 1]:
        temp = time_do[j]
        time_do[j] = time_do[j+1]
        time_do[j+1] = temp
        temp = what_do[j]
        what_do[j] = what_do[j+1]
        what_do[j+1] = temp

print("My rootine today:")

for i in range(len(time_do)):
    if time_do[i]%int(time_do[i])==0:
        print(f"{i+1}) {what_do[i]} , time - {time_do[i]}:00")
    else:
        print(f"{i+1}) {what_do[i]} , time - {int(time_do[i])}:{int((time_do[i]-int(time_do[i]))*60)}")

print("")
print("My marks today: \n")
for i in range(len(marks)):
    if i == len(marks)-1:
        print(f"{marks[i]}")
        break
    print(f"{marks[i]}",end=" , ")