#Find the number in a range of number

a = int(input("Input a Upper Limit in number: ")) #input the upper limit 

for num in range(0,a):
    for i in range(2,num):
        if num%i == 0:
            j = num/i
            print('%d can not be a prime number because %d is %d*%d' %(num,num,i,j))
            break
    else:
        print(num, ' is prime number')
