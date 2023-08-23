"""
list = [10, 20, 30, 40]
largest_number = 0

for number in list:
    if largest_number is ' 0' or largest_number < number:
        largest_number = number

print(largest_number)

"""

"""
ch = 'r'
n = "raman"

if not any(ch == i for i in n):
    print("")
"""
"""
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example list of numbers
num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

prime_numbers = find_prime_numbers(num_list)
print("Prime numbers in the list:", prime_numbers)

"""
# write a python program to count the number of strings feom a given list of strings . the
# of strings . The string length is 2 or more and the first and last characters are the same .

# sample list : ['abc','xyz','aba','1221']
# Expected Result:2



