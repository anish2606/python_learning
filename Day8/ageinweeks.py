def life_in_weeks():
    weeks = 52
    age = int(input("Enter you age : "))
    age_in_weeks = int((age) *52)
    print(age_in_weeks)

life_in_weeks()

# life remaining when compared to 90 years

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")
 
 
life_in_weeks(12)
