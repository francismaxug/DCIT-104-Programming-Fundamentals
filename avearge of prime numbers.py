#ID: 10953758
#I hereby state that this work was done soely by me and by me alone.
#signed
#Fancis Atinga



#This is a Python program to calculate the sum of all pime numbers in a given range.
#The user will just input a number and the programe will tell him or her the number of pime numbers from 2 to that given number by the user. As well as summing those numbers and then calculate for the average of those prime numbers.
#Thank you. Lets begin.

print('Input a Number:')
nums=int(input())
sumPrime=0
numberofPrime=0
for i in range(2, nums +1):
    for j in range(2, i):
        if i%j==0:
            break
    else:
        print(i, 'Is a prim number')
        sumPrime+=i
        numberofPrime+=1
print('The sum of these prime numbers are:' , sumPrime)

print('The Number of prime numbers are: ', numberofPrime)

print('The average is :' + str(int(sumPrime) / int(numberofPrime)))
