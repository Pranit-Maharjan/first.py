student = {
    "name": "Hotoke",
    "age": 21,
    "course": "BCSIT",
    }
print(student["name"])
print(student["age"])
print(student["course"])
student["age"] = 22     #update value
student["college"] = "ABC College"     #add new key value
print(student)
del student["course"]
print(student)

print(student.keys())
print(student.values())
print(student.items())

#to convert list into tuples
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple (my_list)
print(my_tuple)

#to convert tuple into list
my_tuple = (1, 2, 3, 4, 5)
my_list= list(my_tuple)
print(my_list)

#to convert string into list
my_string = "Hello World"
my_list = list(my_string)
print(my_list)

#to convert string into tuple
my_string = "Hello World"
my_tuple = tuple(my_string)
print(my_tuple)

#to convert list into string
my_list = ['H', 'e', 'l', 'l', 'o']
my_string = ''.join(my_list)
print(my_string)
 

 #to convert tuple into string
my_tuple = ('H', 'e', 'l', 'l', 'o')
my_string = ''.join(my_tuple)
print(my_string)

#to convert dict into tuple
my_dict = {"name": "Hotoke", "age": 21, "course": "BCSIT"}
my_tuple = tuple(my_dict.items())
print(my_tuple)

#to convert dict into list
my_dict = {"name": "Hotoke", "age": 21, "course": "BCSIT"}
my_list = list(my_dict.items())
print(my_list)
