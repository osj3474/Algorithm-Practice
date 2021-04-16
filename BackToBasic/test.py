# problem
N = 10
pro_lst = [0,1,2,3,4,6,7,8,9]

# # solution 1
# entire_lst = [i for i in range(N)]
# for i, value in enumerate(pro_lst):
#     if i != value:
#         print(value-1)
#         break

# solution 2
# miss = N-1
# for i in range(miss):
#     print('{}'.format(i))
#     print(i, pro_lst[i])
#     bit = i ^ pro_lst[i]
#     print('bit : ', bit)
#     miss ^= i ^ pro_lst[i]
#     print('miss : ',miss)
#     print()
# print(miss)