#concatention of string
string1 = "Hello "
string2 = "World"
print(string1+string2)

#replace part of string
string = "Coding"
string = string.replace('ing','ers')
print(string)

#palindrome string
string = input("Enter a string: ")
mid = (len(string)-1)//2
start =0
last = (len(string)-1)
flag=0
while(start<=mid):
    if string[start]==string[last]:
        start+=1
        last-=1
    else:
        flag=1
        break

if(flag==1):
    print("String is not palindrome")
else:
    print("String is palindrome")    

#reverse a string
string =input("enter a string")
print(string[::-1])
