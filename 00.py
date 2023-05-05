# some_str='heLLo'
# # for letter in some_str:
# #     print(letter)

# # for ind in range(0, len(some_str)):
# #     print(some_str[ind])
# # print(some_str[-2])
# print(some_str[1:4:2])
import random
some_list = []
for _ in range(10):
    number = random.randint(1, 10)
    some_list.append(number)
print(some_list)
print(some_list.count(7))
print(7 in some_list)
# some_list = [int(input()) for _ in range(10)]
# print(some_list)
# import time
# some_list = [random.randint(1,10000) for i in range(10**7)]
# some_set = set(some_list)

# start1 = time.perf_counter()
# print(99999 in some_list)
# end1 = time.perf_counter()


# start = time.perf_counter()
# print(99999 in some_set)
# end = time.perf_counter()
# print((end1-start1)/(end-start))
# some_dict = {'яблоко': 'apple','апельсин':'orange'}
# print(some_dict.get('груша', 'такого ключа нет'))
# # print(some_dict['груша'])
# some_dict['виноград']='grape'
# print(some_dict)

# a = [1,2,3]
# b = ['1','2','3']
# c ={}
# for ind in range(0,len(a)):
#     c[a[ind]] = b[ind]
# print(c)