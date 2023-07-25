#1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
try:
   n = int(input("Select the number of the day of the week: "))
   if n == 1:
     print ("Monday")
   if n == 2:
     print("Tuesday")
   if n == 3:
     print("Wednesday")
   if n == 4:
     print("Thursday")
   if n == 5:
     print("Friday")
   if n == 6:
     print("Saturday")
   if n == 7:
       print("Sunday")
except ValueError as error:
        print("Enter only integer numbers please!")
        print(f"ValueError: {error}")
except Exception as error:
 print(f"Exception occurred: {error}")
