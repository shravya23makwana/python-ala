print("Factor Finder")
number = int(input("Enter number: "))
i = 1
count = 0
sum = 0
while i <= number:
if number % i == 0:
print("Factor:", i)
count = count + 1
sum = sum + i
i = i + 1
print("Total factors:", count)
print("Sum of factors:", sum)
if sum > number:
print("Abundant number")
else if sum == number:
print("Perfect number")
else:
print("Deficient number")