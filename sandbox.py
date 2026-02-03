number = int(input("what number do you want to check: "))

def is_prime(number):
    if number == 1 :
        return False
    elif number == 2: 
        return True
    elif number.prime() :
        return True    


if is_prime(number):
    print(f"the number {number} is prime")
else: 
    print(f"the number {number} is not prime")