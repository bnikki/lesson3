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

