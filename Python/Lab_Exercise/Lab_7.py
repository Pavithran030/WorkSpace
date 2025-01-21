#1
def show_employee(name, salary=9000):
    print("Name:", name)
    print("Salary:", salary)

# Example usage:
show_employee("John", 10000)  # Passing both name and salary
show_employee("Alice")         # Passing only name, default salary used

#2
def func1(*args):
    for arg in args:
        print(arg)

# Example usage:
func1(1, 2, 3, "Hello", [4, 5])

#3
def print_name_and_age(name, age):
    print("Name:", name)
    print("Age:", age)

# Example usage:
print_name_and_age("Alice", 30)

#4
def get_unique_elements(input_list):
    return list(set(input_list))

# Example usage:
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = get_unique_elements(sample_list)
print("Unique List:", unique_list)

#5
def reverse_list(input_list):
    return input_list[::-1]

# Example usage:
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Original List:", original_list)
print("Reversed List:", reversed_list)

#6
def compute(num1, num2):
    """
    Compute the sum, difference, product, and quotient of two numbers.

    Parameters:
        num1 (float or int): First number.
        num2 (float or int): Second number.

    Returns:
        tuple: A tuple containing the sum, difference, product, and quotient.
    """
    # Compute sum
    total_sum = num1 + num2
    # Compute difference
    difference = num1 - num2
    # Compute product
    product = num1 * num2
    # Compute quotient
    # Check if num2 is not zero to avoid division by zero error
    if num2 != 0:
        quotient = num1 / num2
    else:
        # If num2 is zero, assign None to the quotient
        quotient = None
        print("Cannot divide by zero.")

    return total_sum, difference, product, quotient

# Example usage:
result = compute(10, 5)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Quotient:", result[3])

#7
def student_info(name, **kwargs):
    """
    Print student's information including name, age, grade, and school.

    Parameters:
        name (str): Student's name.
        **kwargs: Keyword arguments for age, grade, and school.
    """
    print("Student Information:")
    print("Name:", name)
    if 'age' in kwargs:
        print("Age:", kwargs['age'])
    if 'grade' in kwargs:
        print("Grade:", kwargs['grade'])
    if 'school' in kwargs:
        print("School:", kwargs['school'])

# Example usage:
student_info("Alice", age=15, grade=10, school="ABC High School")

#8
def generate_primes(limit):
    """
    Generate prime numbers up to the specified limit using the Sieve of Eratosthenes algorithm.

    Parameters:
        limit (int): Upper limit for generating prime numbers.

    Yields:
        int: Prime numbers up to the specified limit.
    """
    # Create a boolean array "is_prime" to mark numbers as prime or composite
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime

    # Mark multiples of each prime number as composite
    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    # Yield prime numbers
    for num in range(2, limit + 1):
        if is_prime[num]:
            yield num

# Example usage:
limit = 20
print("Prime numbers up to", limit, ":")
for prime in generate_primes(limit):
    print(prime, end=" ")
#9
def apply_function_to_list(func, values):
    """
    Apply the given function to each value in the list and return the results.

    Parameters:
        func (function): The function to apply to each value.
        values (list): List of values.

    Returns:
        list: List containing the results of applying the function to each value.
    """
    return [func(value) for value in values]

# Example usage:

# Define a function to square a number
def square(x):
    return x ** 2

# List of values
numbers = [1, 2, 3, 4, 5]

# Apply the square function to each value in the list
result = apply_function_to_list(square, numbers)
print("Original List:", numbers)
print("Squared List:", result)

#10
def generate_fibonacci():
    """
    Generate Fibonacci numbers indefinitely.

    Yields:
        int: Fibonacci numbers.
    """
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Yield the first Fibonacci number
    yield a
    # Yield the second Fibonacci number
    yield b
    # Generate subsequent Fibonacci numbers indefinitely
    while True:
        # Calculate the next Fibonacci number
        a, b = b, a + b
        yield b

# Example usage:
fibonacci_generator = generate_fibonacci()
for _ in range(10):  # Print the first 10 Fibonacci numbers
    print(next(fibonacci_generator), end=" ")


#11
def factorial(n):
    """
    Calculate the factorial of a given positive integer using recursion.

    Parameters:
        n (int): Positive integer.

    Returns:
        int: Factorial of the given integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = 5
print("Factorial of", number, "is:", factorial(number))


#12
def count_departments(org_chart):
    """
    Recursively count the total number of departments, including sub-departments.

    Parameters:
        org_chart (dict): Nested dictionary representing the organizational chart.

    Returns:
        int: Total number of departments.
    """
    # Base case: if the organization chart is empty, return 0
    if not org_chart:
        return 0
    
    # Initialize the count with the number of direct departments
    count = len(org_chart)
    
    # Recursively count the sub-departments
    for sub_dept in org_chart.values():
        count += count_departments(sub_dept)
    
    return count

# Example usage:
org_chart = {
    'HR': {
        'Recruitment': {},
        'Training': {},
        'Benefits': {
            'Healthcare': {},
            'Insurance': {}
        }
    },
    'IT': {
        'Development': {
            'Frontend': {},
            'Backend': {}
        },
        'QA': {},
        'DevOps': {}
    },
    'Finance': {}
}

total_departments = count_departments(org_chart)
print("Total number of departments:", total_departments)


























