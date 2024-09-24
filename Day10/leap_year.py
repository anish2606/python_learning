def is_leap(year):
    if year % 4 ==0:
        print(f"{year} is a Leap year")
    elif year % 100 == 0:
        print (f"{year} is a leap year")
    elif year % 400 == 0:
        print (f"{year} is not a leap year")

is_leap(int(input("What is the year you are entering?: ")))
