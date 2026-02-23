print("Factor Finder")
number = int(input("Enter number: "))
i = 1
count = 0
total_sum = 0

while i <= number:
    if number % i == 0:
        print("Factor:", i)
        count = count + 1
        total_sum = total_sum + i
    i = i + 1

print("Total factors:", count)

# Subtract the number itself to get proper factor sum
proper_sum = total_sum - number

print("Sum of proper factors:", proper_sum)

if proper_sum > number:
    print("Abundant number")
elif proper_sum == number:
    print("Perfect number")
else:
    print("Deficient number")