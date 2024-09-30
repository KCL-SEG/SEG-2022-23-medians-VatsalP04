"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

if len(numbers)%2 == 0:
    median = (numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1]) / 2
else:
    median = numbers[len(numbers)//2]

print(f"The median of the list is {median}.")