#Challenge 1: Sum of Two Numbers

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

sum_result = num1 + num2

print("Sum = ", sum_result)

#Subtraction
print("Subtraction =",num1-num2)

#multiplication
print("Multiplication =", num1*num2)

#Division
print("Division =", num1/num2)


#Challenge 2: Odd or Even Checker

num = int(input("Enter Number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Challenge 3: Factorial Calculation

num = int(input("Enter a Number: "))

factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print("Factorial =", factorial)


# Challenge 4: Fibonacci Sequence

n = int(input("How many terms?"))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    next_num = a + b
    a = b
    b = next_num


# Challenge 5: String Reverse

print("\n")
text = input("Enter a string: ")

reverse_text = text[::-1]

print("Reversed String =", reverse_text)


# Challenge 6: Palindrome Check

print("\n")

word = input("Enter a word: ")

reverse_word = word[::-1]

if word == reverse_word:
    print("Palindrome")
else:
    print("Not Palindrome")


# Challenge 7: Leap Year Check

print("\n")

year = int(input("Enter the Year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")


# Challenge 8: Armstrong Number

num = int(input("Enter Number: "))

order = len(str(num))

sum_val = 0

for digit in str(num):
    sum_val = sum_val + int(digit) ** order

if num == sum_val:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


