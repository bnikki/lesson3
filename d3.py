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

#2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання
try:
  j = int(input("Enter first number: "))
  k = int(input("Enter second number: "))
  if j == k:
    print("The numbers are equal")
  else:
    print("Numbers are not equal")
    if j < k:
     for i in range (j, k +1):
      print(i)
except ValueError as error:
        print("Enter only integer numbers please!")
        print(f"ValueError: {error}")
except Exception as error:
 print(f"Exception occurred: {error}")

#3. Користувач вводить два числа та матем дію: + - * або /
#Залежно від введеної матем дії вивести результат
try:
 h = int(input("Enter first number: "))
 l = int(input("Enter second number: "))
 math_action = input("Enter math action: + - * / ")
 match math_action:
    case "+":
        print(f"{h} {math_action} {l} = {h + l}")
    case "-":
        print(f"{h} {math_action} {l} = {h - l}")
    case "*":
        print(f"{h} {math_action} {l} = {h * l}")
    case "/":
        if l != 0:
            print(f"{h} {math_action} {l} = {h / l}")
        else:
            print("Division by zero!")
    case _:
        print("Incorrect math action!")
except ValueError as error:
        print("Enter only integer numbers please!")
        print(f"ValueError: {error}")
except Exception as error:
 print(f"Exception occurred: {error}")





