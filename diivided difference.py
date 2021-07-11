#Newtons Divided difference formula

n = int(input("Enter the number of data in dataset : "))


li = [[0 for i in range(n)]for i in range(n+1)]

for i in range(n):
    li[0][i] = int(input("enter the value of x{}  : ".format(i)))
    li[1][i] = int(input("enter the value of y{}  : ".format(i)))

x = int(input("enter the unknown value of x : "))


c = 1
for i in range(n-1):
    for j in range(n-1-i):
        li[i+2][j] = (-li[i+1][j]+li[i+1][j+1]) / (li[0][j+c]-li[0][j])
        
    c = c+1

y = li[1][0]

for i in range(n-1):
    temp_add = 1 
    
    for j in range(i+1):
        temp_add = temp_add * (x-li[0][j])
    
    y = y + ( temp_add * li[i+2][0] )

print("The value of y for {} is {}".format(x,y))
    
#print(li)