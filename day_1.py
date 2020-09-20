#hello

## lists and dictionaries 

arr1 = [1,2,3]
arr2 = [2,3,4]

arr3 = {}

arr3[arr1[0]] = arr2[0] # {1: 2}
arr3[arr1[1]] = arr2[1] # {1: 2, 2: 3}

print(arr3)

        
user_1 = {"name" : "Tonia Saba"}
user_2 = {"name" : "James Stark"}


my_user = {}

my_user[user_1["name"]] = user_2["name"] #{'Tonia Saba': 'James Stark'}

print(my_user)
