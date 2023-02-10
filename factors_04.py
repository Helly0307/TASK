print("**Count Fctors**")
x = int(input("Enter number: "))
   
def factors(num):
   print(f"Factors of {num} are...")
   for i in range(1, num+1):
        if num % i == 0:
            print(i)   
factors(x)


            











