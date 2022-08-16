#find a prime number in a range of number

for num in range(0,10):
#a range of number start from 0 and end with 10
    for i in range(2,num):
            if num % i == 0:
            j = num/i 
            print('%d is %d * %d'%(num,i,j))
            break
    else:
        print(num,' is prime number')
