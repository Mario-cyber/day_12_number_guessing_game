number = int(input("what number do you want to check: "))

def is_prime(number):
    if number < 2 :
        return False
    elif number == 2: 
        return True
    elif number > 2:
        for i in range(3, int(number ** 0.5 + 1)):
            if number % i == 0 : 
                return False 


for number in range(0,17,1):
    print(f"the number i is prime is: {is_prime(number=number)}")

# if is_prime(number):
#     print(f"the number {number} is prime")
# else: 
#     print(f"the number {number} is not prime")

