#list
friendname=["jyoti","saloni","shrishti",1]
print("before",friendname)

#to add the new elements in list
friendname.append("preeti")  #append adds the value at the end
#print after adding new name
print("after",friendname)

#to add the name in specific position 
friendname.insert(0,"sanya")
print("add name at index  0",friendname)

#to remove the name from list 
friendname.remove("preeti")
#print after removing name from the list
print(friendname)

#to remove all elements
# friendname.clear()
# print(friendname)

friendname.pop()  #it removes last element #pop will follow the step 
print(friendname)  #we can also give index no. 

# to sort the list       (sort works in similar type of data )
friendname.sort()
print(friendname)

#for loop
for names in friendname:
    print(names)
    
#to print the number from  1 to 10 
for i in range(1,11):
    print(i)

#even number from 1 to 10   
for i in range(2,11,2):
    print(i)
            #or 
for i in range(1,11):
     if i%2==0:
        print(i)
        
#sets    (set is unordered ,changable can not store duplicate values ,unsorted)
#unconvertable 
#we use set when we don't want to change any value (like aadhar card no.)
sets={"preeti","jyoti","saloni"}
sets.add("shrishti")
sets.remove("shrishti")
#sets[0]="xxxx"(it will give error)    #exception handelling- fixing error 
print(sets)
print(type(sets))

#list
list=["jyoti","saloni","shrishti","sanya","swasti"]
for i in list:
    print(i)

list.reverse()
print(list)

list.clear()
print(list)

# using while print 1 to 10
i=1
while i<=10:
    print(i)
    i=i+1
    
    #reverse 
i=10
while i>=1:
    print(i)
    i=i-1

#break(to stop)continue(to skip)
#(ctrl+z=undo)
 #(ctrl+c=for stopping finite loop)

#function 
def myfunction():  
    print("my function called")
    
#call the function by name
myfunction()

def Area(x,y):
    a=x*y
    print(a)
    
x=int(input("enter x"))
y=int(input("enter y"))
Area(x,y)

def area(x,y):
    a=x*y
    return a
area =area(2,3)
print(area)


