#we can read, write, update,delete a file 

f=open("preeti.txt","w")  #(open-create file)   #w for write   (can create any type of file but you need reader for that)
f.write("my name is preeti,i'm a mca student")
f.close()

f=open("preeti.txt","r")  
print(f.read())
#notepad type application

#create a file and enter your name,collegename and email
name=input("enter your name")
email=input("enter your email")
collegename=input("enter your collegename")
data=name+email+collegename

f=open("preetidetails.txt","w")
f.write(data)
f.close()

f=open("preetidetails.txt","r")
print(f.read(4))  #(it will read 4 letters from the start)

