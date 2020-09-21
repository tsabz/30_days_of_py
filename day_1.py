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

my_user_users = [user_1, user_2]

for user in my_user_users:
    print(user['name'])


user_3 = {"id": 2, "name": "xy28*", "email": "abc@gmail.com"}
user_4 = {"id": 1, "name": "Nick Person"}

my_users = [user_3, user_4]

for user in my_users:
    if "email" in user:
        print(user["email"])

selected_user = {} 
my_user_lookup = 2

for user in my_users:
    if user["id"] == my_user_lookup:
        selected_user = user

print(selected_user)

