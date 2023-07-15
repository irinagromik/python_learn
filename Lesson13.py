# i = 1
# while i<= 10:
#     print(i)
# i#     i = i +1
#
# n = int(input())
# if n >= 1 and n <= 20:
#     print(n **2, sep='!', end='\n')
#
# def is_leap(year):
#     leap = False
#
#     if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
#         return True
#     else:
#         return False
#
#
# year = int(input())
# print(is_leap(year))

n = int(input())
for i in range(n):
   print(i+1, sep=' ', end='')