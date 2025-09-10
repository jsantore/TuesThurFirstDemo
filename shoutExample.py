
class_name = input("what class are you taking next semester:")
num_credits = input("How many credits is that class:")
#adding something here
print(f"You are taking {class_name} next semester for {num_credits} credits")
STUDENTS_IN_CLASS = 23
students_today = 21
students_absent = STUDENTS_IN_CLASS - students_today
percent_here = students_today/STUDENTS_IN_CLASS*100
print(f"There are {STUDENTS_IN_CLASS} registered and {percent_here:.2f}% of there are here today")
