# Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, которая заменяет оценки 
# Василия, но наоборот: все максимальные – на минимальные, а минимальные на максимальные.
import random
list_lenght = int(input("Введите длину списка: "))
our_list = [random.randint(1, 5) for _ in range(list_lenght)]
print(our_list)
max_score = max(our_list)
min_score = min(our_list)
# for i in range(list_lenght):
#   if our_list[i] > max_score:
#     max_score = our_list[i]
#   if our_list[i] < min_score:
#     min_score = our_list[i]
print(f"Минимальная оценка: {min_score}, максимальная оценка: {max_score}")
for i in range(len(our_list)):
  if our_list[i] == max_score:
    our_list[i] = max_score + 1
  if our_list[i] == min_score:
    our_list[i] = max_score
  if our_list[i] == max_score + 1:
    our_list[i] = min_score
print(our_list)