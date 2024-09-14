import random

letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
special_chars=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+']

print("Welcome to the Pypassword generator")
nr_letters = int(input("How many letters do you need to enter ? \n"))
nr_numbers = int(input("How many numbers do you need to enter? \n"))
nr_char = int(input("How many special characters do you need to enter? \n"))

#passwd=""

#for i in range(0, nr_letters ):
    #passwd += random.choice(letters)

#for i in range(0, nr_numbers ):
    #passwd += random.choice(numbers)

#for i in range(0, nr_char ):
    #passwd += random.choice(special_chars)

#print (passwd)

#high level

password=""

password_list=[]

for i in range(0, nr_letters):
    password_list.append(random.choice(letters))

for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_char):
    password_list.append(random.choice(special_chars))

password = random.shuffle(password_list)
print(password_list)

for char in password_list:
    password+= i

print(f"Your password is : {password}")