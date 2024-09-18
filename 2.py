#to print your name 
print("preeti")

#to print your name using user input 
name=input("enter your name:")
print(name)

#WAP to find the current age 
current_year=int(input("enter the current year:"))
born_year=int(input("enter your born year:"))
print("age=",current_year-born_year)

#WAP for currency convertor 
#before starting any program you have to think the input parameter required in programs
#e.g in currency convertor u need currency amount in inr and converted currency index rate 

print("convert rupees into dollars ")
rupeesamount=int(input("enter the amount in Rs."))
RsintoDollars  =(rupeesamount/84)   #84 is the index rate 
print(rupeesamount,"convert into dollar",RsintoDollars)


print("convert dollars into rupees ")
dollarsamount=int(input("enter the amount in Dollar"))
DollarsintoRs  =(dollarsamount*84)    
print(dollarsamount,"convert into dollar",DollarsintoRs)

#WAP to check you are eligible to vote or not 
userage=int(input("enter your age:"))
#for voting you must greater than 17 
if userage>17:
    print("eligible to vote")
else:
    print("not eligible to vote ")

# if age>17 and female- then can apply for govt job 
#if male- then can apply for private job

gender=input("enter your gender")
if userage>17:
    if gender=='female':
        print("eligible for govt jobs")
    elif gender=='male':
        print("eligible for private job")#else will print this if you input any gender other than male so use elif 
    else:
        print("gender not defined")
else:
    print("not eligible for any job")

                 #or 
                 
if userage>17 and gender=='female':
    print("eligible for govt. job")
elif userage>17 and gender=='male':
    print("eligible for private job")
else:
    print("not eligible for any job")
    
#WAP to check the greatest no. among 3 no.
first=int(input("enter the first number:"))
second=int(input("enter the second number:"))
third=int(input("enter the third number:"))

if first >second and first > third:
    print(first,"is greatest")
elif second>first and second > third:
    print(second,"is greatest")
else:
    print(third," is greatest")

#data collection:to store multiple data (list,set,tuple,dictionary)
#list- it can store diff types of data , data can change
friendname=["jyoti","saloni",1,2,3]
print(type(friendname))
print(friendname)



