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

