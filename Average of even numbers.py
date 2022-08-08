#ID: 10953758
#I hereby state that this work was done soely by me and by me alone.
#signed
#Fancis Atinga

#This is a Python programe to calculate for the sum of all even numbers between 1 and 1000. As well as finding the average of these even numbers.

a=0
b=0
number=range(1, 1000)
for i in number:
    if i%2==0:
        a+=i
        b+=1
print('The total is: ' + str(a))

print('The number of even numbers are: ' + str(b))

print('the average is: ' + str(int(a) / int(b)))
