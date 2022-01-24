#                                               Задача 1
# a = 34
# b = 18

# print(a,b)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# name = input("Как вас зовут? ")
# print(a, b, name)

#                                               Задача 2
# time = int(input("Введите время в секундах "))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

#                                               Задача 3
# n = int(input("Введите число - "))
# total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
# print("Сумма чисел n + nn + nnn - %d" % total)

#                                               Задача 4
# n = int(input("Введите целое положительное число "))
# number_max = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > number_max:
#         number_max = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Наибольшая цифра в числе ", number_max)
#         break

#                                               Задача 5
# profit = float(input("Введите выручку фирмы "))
# costs = float(input("Введите издержки фирмы "))
# if profit > costs:
#     print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
#     people = int(input("Введите количество сотрудников фирмы "))
#     print(f"прибыль в расчете на одного сторудника сотавила {profit / people:.2f}")
# elif profit == costs:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма работает в убыток")

#                                               Задача 6
# a = int(input("Введите результаты пробежки первого дня в км "))
# b = int(input("Введите общий желаемый результат в км "))
# result_days = 1
# result_km = a
# while result_km < b:
#         a = a + 0.1 * a
#         result_days += 1
#         result_km = result_km + a
# print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
