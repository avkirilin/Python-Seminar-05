# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

count_N = int(input("Введите номер числа Фибоначчи, который необходимо показать: "))
def fibonacci_method (number):
  if number in [1, 2]:
    return 1
  return fibonacci_method(number - 1) + fibonacci_method(number - 2)
list_1 = []
for i in range (1, count_N + 1):
  list_1.append(fibonacci_method(i))
print(f"{count_N}-е число Фибоначчи равно: {list_1[-1]}")