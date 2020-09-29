# #hello

# ## lists and dictionaries 

# arr1 = [1,2,3]
# arr2 = [2,3,4]

# arr3 = {}

# arr3[arr1[0]] = arr2[0] # {1: 2}
# arr3[arr1[1]] = arr2[1] # {1: 2, 2: 3}

# print(arr3)


# def get_strings(city):
    
#     counter = 0
#     arr3 = {}
#     letters = []

#     for letter in city:
#         letters = letter
#         print(letters)


# print(get_strings("Chicago"))

        
# user_1 = {"name" : "Tonia Saba"}
# user_2 = {"name" : "James Stark"}


# my_user = {}

# my_user[user_1["name"]] = user_2["name"] #{'Tonia Saba': 'James Stark'}

# print(my_user)

# my_user_users = [user_1, user_2]

# for user in my_user_users:
#     print(user['name'])


# user_3 = {"id": 2, "name": "xy28*", "email": "abc@gmail.com"}
# user_4 = {"id": 1, "name": "Nick Person"}

# my_users = [user_3, user_4]

# for user in my_users:
#     if "email" in user:
#         print(user["email"])

# selected_user = {} 
# my_user_lookup = 2

# for user in my_users:
#     if user["id"] == my_user_lookup:
#         selected_user = user

# print(selected_user)


# for x in range(0,10):
#     if user in my_users:
#         if user["id"] == x:
#             print(user)






# matrix = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] 

# hashsum = {}

# hashsum = matrix[0][0], matrix[1][1], matrix[2][2], matrix[0][2], matrix[1][1], matrix[2][0]

# sum_of_hashsum = sum(hashsum)

# print(sum_of_hashsum) #30


# def sum_diagonals(matrix):
#     hashsum = {}
#     hashsum = matrix[0][0], matrix[1][1], matrix[2][2], matrix[0][2], matrix[1][1], matrix[2][0]
#     sum_of_hashsum = sum(hashsum)
#     return sum_of_hashsum #30


# print(sum_diagonals([ [ 1, 3, 3 ], [ 4, 2, 6 ], [ 7, 2, 9 ], [ 7, 2, 9 ] ])) #24



# ages = [9, 10, 9]

# for age in ages:
# 	print(ages[age])



# def summation(num):
#     print(sum(range(1,num + 1)))


# summation(100)
    
### TWO SUM ###

# nums = [2,7,11,15]
# arr3 = {}
# target = 9

# for i in range(len(nums) - 1):
#     for r in range(i + 1, len(nums)):
#         if nums[i] != nums[r]:
#             if nums[i] + nums[r] == target:
#                 arr3.append(i)
#                 arr3.append(r)

# print(arr3)

# for i in range(len(nums) - 1):
#     for r in range(i + 1, len(nums)):
#         arr3[r] = [i]

# print(arr3)      

# for i in nums:
#     for r in nums:
#         arr3[i] = [r]

# print(arr3)

# nums = [2,7,11,15]
# arr = []

# for i in range(len(nums) - 1):
#     for r in range(i + 1, len(nums)):
#         print("*******")
#         print(r)
#         arr.append(r)


# # print(arr)


# arr = [3,2,4]
# target = 6

# def twoSum(target,arr):
#     for i in range(len(arr)):
#         for k in range(i + 1,(len(arr))):
#             if arr[i] + arr[k] == target:
#                 return [i,k]

# print(twoSum(6,[3,2,4]))




arr = [1,2,3,4]
target = 5

# def twoSum(arr, target):
#     for i in range(len(arr)):
#         for k in range(len(arr)):
#             if arr[i] + arr[k] == target:
#                 return [i,k]

# print(twoSum([1,2,3,4], 5))



# def twoSum(arr, target):
#     hashmap = {}
#     for i in range(len(arr)):
#         hash_map = arr[i]
    

