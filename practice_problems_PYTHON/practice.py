# PYTHON PRACTICE PROBLEMS

print("\n-------------------------ANSWERS-------------------------\n")

# 1) Create a function that calculates the area of a rectangle.
def rectangle_area(width, length):
    """Function to calculate the area of a rectangle."""

    return float(width*length)

result = rectangle_area(11.4, 6)
print(f"1) Rectangle Area: {result} inches")

print("\n")

# 2) Create a function that provides the sum and average of a list of numbers.
def sum_average(numbers):
    """Function to return the sum and average of a list of numbers."""

    list_sum = sum(numbers)

    average = list_sum / len(numbers)

    return f"Sum: {list_sum}, Average: {average}"

result = sum_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"2) {result}")

print("\n")

# 3) Create a function that returns the number of vowels in a string.
def vowel_counts(phrase):
    """Function to count the number of vowels in a phrase."""

    vowels= ['a', 'e', 'i', 'o', 'u']

    phrase_listed = list(phrase)

    count = 0

    for vowel in vowels:
        for letter in phrase_listed:
            if vowel == letter.lower():
                count+=1

    return count

result = vowel_counts("Happy Birthday!")
print(f"3) Number of Vowels: {result}")

print("\n")

# 4) Create a function that calculates the median of a list of ages.
def median_age(ages):
    """Function to calculate the median of a list of ages."""

    sorted_list = sorted(ages)

    if len(ages) % 2 == 0:
        m1 = len(ages) // 2 - 1
        m2 = len(ages) // 2
        index_of_answer = (m1+m2) // 2
    else:
        index_of_answer = len(ages) // 2
      
    
    return ages[index_of_answer]

result = median_age([20, 22, 19, 20, 26, 28, 30])
print(f"4) {result}")

print("\n")

# 5) Create a function that checks if a number is even or odd.
def even_or_odd(number):
    """Function to check if a number is even or odd."""

    if number % 2 == 0:
        answer = f'{number} is even.'
    else:
        answer = f'{number} is odd.'

    return answer

result = even_or_odd(19)
print(f"5) {result}")

print("\n")

# 6) Create a function that provides the first 5 multiples of a given number.
def multiples(number):
    """Function to print the first 5 multiples of a given number."""

    multiples = [1, 2, 3, 4, 5]
    multiple_list = []

    for multiple in multiples:
        multiple_list.append(number*multiple)

    return multiple_list
        
result = multiples(5)
print(f"6) The first five multiples are: {result}")

print("\n")

# 7) Create a function to find the highest grade in a gradebook.
def highest_grade(gradebook):
    """Function to find the highest grade in a gradebook(dictionary)."""

    grade = max(gradebook.values())

    for person in gradebook.keys():
        if gradebook[person] == grade:
            return person


student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 98,
    'David': 95,
    'Eva': 89
}

result = highest_grade(student_scores)
print(f"7) The highest grade in class is: {result}.")

print("\n")

# 8) Read in a string from a separate file.
with open('/Users/Brendan Smith/Desktop/practice_problems_PYTHON/text_file.txt', 'r') as file:
    string = file.read()
print(f"8) {string}")

