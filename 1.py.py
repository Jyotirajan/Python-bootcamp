print("preeti")
name="preeti"
grade='a'
salary=56666
print(name)
print(grade)
print(salary)
       #or
print(name,grade,salary)

print(name+grade)  #salary is int type so we can not concatinate it with string type 
#i.e we have to change it first into string type to do so.

#type casting- it converts datatypes into another datatypes

salary=str(salary)
print(name+grade+salary)

#data types
salary=56666
print(type(salary))
print(type(name))

#salary into float 
salary=float(salary)
print(salary)
print(type(salary))

#input from the user
age=input("enter your age:")
print(age)
gender=input("enter your gender:")
print(gender)

#input function default return type is string  

#find age by current year and born year
current_year=int(input("enter the current year:"))
born_year=int(input("enter your born year:"))
print("age=",current_year-born_year)
