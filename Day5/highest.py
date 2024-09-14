marks= [1,4,6,8,2,7,3,10,9]

max_mark = 0

for mark in marks:
    if mark > max_mark: 
        max_mark = mark

print(f"Maximum scored marks is: {max_mark}")
