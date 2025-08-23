import random
import string

#Q1
# l = [11,12,13,14]
# i)
# l.append(50)
# l.append(60)

# ii)
# l.remove(11)
# l.remove(13)

# iii)
# l.sort()
# print(l)

# iv)
# l.sort(reverse=True)
# print(l)

# v)
# flag = -1
# for i in range(0,len(l)):
#     if l[i] == 13:
#         flag = i
#         break
# if flag == -1:
#     print("not found")
# else:
#     print("found at",i+1,"position")

# vi)
# length = 0
# for i in range(len(l)):
#     length+=1
# print(length,"is the length of the list")

# vii)
# sum = 0
# for i in l:
#     sum += i
# print(sum)

# viii)
# sum = 0
# for i in l:
#     if i % 2 != 0:
#         sum += i
# print(sum)

# ix)
# sum = 0
# for i in l:
#     if i % 2 == 0:
#         sum += i
# print(sum)

# x)
# for x in l:
#     flag = True
#     for i in range(2,int((x**0.5)+1)):
#         if x % i == 0:
#             flag = False
#             break
#     if flag and x > 1:
#         print(f"{x} is prime")

# xi)
# l.clear()

# xii)
# del l

# Q2
# l = []
# n = int(input("enter the size of the list:"))
# for i in range(n):
#     x = int(input(f"enter element no. {i+1}:"))
#     l.append(x)
# sum = 0
# for i in l:
#     sum += i
# print(sum)

# Q3
# l = []
# n = int(input("enter the size of the list:"))
# for i in range(n):
#     x = int(input(f"enter element no. {i+1}:"))
#     l.append(x)
# prod = 1
# for i in l:
#     prod *= i
# print(prod)

# Q4
# for i in range(3):
#     for j in range(4):
#         for k in range(6):
#             print("*",end=' ')
#     print()

# Q5
# d= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# d[1] = 8.8
# print(d)
# del d[2]
# print(d)
# if 6 in d:
#     print("yes")
# else:
#     print("no")
# print(len(d))
# print(sum(d.values()))
# d[3] = 7.1
# print(d)
# d.clear()
# print(d)

# Q6
# s1={10,20,30,40,50,60}
# s2={40,50,60,70,80,90}
# i)
# s1.add(55)
# s1.add(60)
# print(s1)
# ii)
# s1.discard(10)
# s1.discard(30)
# print(s1)
# iii)
# for i in s1:
#     if i == 40:
#         print("Yes")
#     else:
#         print("no")
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))

# Q7
# i)
# for x in range(100):
#     len = random.randint(6,8)
#     str1 = ''.join(random.sample(string.ascii_letters,len))
#     print(str1)
# ii)
# for n in range(600,801):
#     flag = True
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             flag = False
#             break
#     if flag and n > 1:
#         print(f"{n} is prime")
#     else:
#         continue
# iii)
# for i in range(100,10000):
#     if i%7==0 and i%9==0:
#         print(i)

# Q8
# exam_st_date = (11, 12, 2025)
# print("Exams will start from:",exam_st_date[0],"/",exam_st_date[1],"/",exam_st_date[2])

# Q9
# l = []
# n = int(input("enter the size of the list:"))
# for i in range(n):
#     x = int(input(f"enter element no. {i+1}:"))
#     l.append(x)
# print("the elements that are divisible are:")
# for i in l:
#     if i%5==0:
#         print(i)

# Q10
# flag = True
# n = int(input("enter the number to be checked:"))
# if n%2 == 0:
#     flag = True
# else:
#     flag = False
# if flag is True:
#     print("the number is even")
# else:
#     print("the number is odd")

# Q11
# string = "Hi i am Emma. I, Emma, am 18 years old!"
# count = 0
# for i in string.split():
#     if 'Emma' in i:
#         count += 1
# print(f"the substring is found {count} time(s) in the string")

# Q12
# l = [1,2,3,4,5,6]
# odd = []
# even = []
# for i in l:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd)
# print(even)

# Q13
# positions = [(2,3), (4,5), (6,7), (7,8)]
# for i in positions:
#     if i[0]%2 == 0:
#         print(i,i[1])

# Q14
# sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
# for i in sensor_data.values():
#     if i > 3:
#         print(i)

# Q15
# commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
# commands_executed = {"MOVE", "TURN_LEFT", "STOP"}
# print(commands_received.difference(commands_executed))
