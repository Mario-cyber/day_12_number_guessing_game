number = int(input("what number do you want to check: "))

def is_prime(number):
    if number < 2 :
        return False
    if number == 2: 
        return True
    if number % 2 == 0:
        return False

    for i in range(3,int(number ** 0.5 +1) ,2):
        if number % 1 == 0:
            return False
    return True
print(is_prime(number))

# for number in range(0,17,1):
#     print(f"the number i is prime is: {is_prime(number=number)}")

# if is_prime(number):
#     print(f"the number {number} is prime")
# else: 
#     print(f"the number {number} is not prime")

