#Write a program to find the factors of given number.

print("**Count Factors**")
x = int(input("Enter number: "))
   
def factors(num):
   print(f"Factors of {num} are...")
   print("1",end=' ')

   while num % 2 == 0:
       print(2,end=' '),
       num = num // 2
       
   for i in range(3,num+1):
        
        while num % i == 0:
            print(i,end=' '),
            num = num // i
factors(x)