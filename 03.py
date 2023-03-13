# Напишите фунцию, которая принимает одно число и проверяет, является ли оно простым
our_num = int(input("Введите любое целое положительное число: "))
flag = True
for i in range(2, our_num // 2):
  if our_num % i == 0:
    flag = False
    break
  else:
    flag = True
if flag == True:
  print(f"Число {our_num} является простым")
else:
  print(f"Число {our_num} не является простым")