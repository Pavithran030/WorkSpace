# import numpy as np
# lt=[1,2,3,4,5,6,7,8,9]
# k=np.array(lt)
# print(k)
# m=k.reshape(3,3)
# print(m)
# print(m[::-1,::-1])

# 12
# import numpy as np 
# k=np.array([0,1,2,3,4,5])
# m=k.reshape(2,3)
# print(m)
# print("Mean",np.mean(m,axis=1))
# print("Variance",np.var(m,axis=1))
# print("Standard Deviation",np.std(m,axis=1))

# #13

# import turtle as hk
# #hk=turtle.Turtle()
# hk.speed(20)
# hk.begin_fill()
# hk.color("red")
# hk.circle(100)
# hk.end_fill()
# hk.hideturtle()
# hk.done()

#14

# import turtle as tt

# sc=tt.Screen().bgcolor("white")

# p=tt.Turtle()

# p.penup()
# p.goto(-100,-100)
# p.pendown()

# for i in range(4):
#     p.fd(200)
#     p.left(90)

# p.penup()
# p.goto(-50,-50)
# p.pendown()

# for i in range(4):
#     p.fd(100)
#     p.left(90)

# #15
# import tkinter as tk
# from tkinter import messagebox

# def submit_login():
#     username = username_entry.get()
#     password = password_entry.get()

#     messagebox.showinfo("Login Result", f"Username: {username}\nPassword: {password}")

# root = tk.Tk()
# root.title("Login Form")


# username_label = tk.Label(root, text="Username:")
# password_label = tk.Label(root, text="Password:")

# username_entry = tk.Entry(root)
# password_entry = tk.Entry(root, show="*")  #
# submit_button = tk.Button(root, text="Submit", command=submit_login)

# username_label.grid(row=0, column=0, padx=10, pady=5)
# username_entry.grid(row=0, column=1, padx=10, pady=5)
# password_label.grid(row=1, column=0, padx=10, pady=5)
# password_entry.grid(row=1, column=1, padx=10, pady=5)
# submit_button.grid(row=2, columnspan=2, padx=10, pady=10)

# root.mainloop()

# 17 (b)

# n=int(input("Enter a number : "))
# for i in range(n):
#     c=[1]
#     for j in range(1,i+1):
#         p=c[-1]
#         n=p*(i-j+1)//j
#         c.append(n)
#     print(*c)




# n=216
# to=0
# while n>0:
#     i=n%10
#     to+=i**3
#     print(i)
#     n=n//10
# print(to)
# if n==to:
#     print(to)
    


# def highest_score(students):
#     # Find the student with the highest score
#     max_student = sorted(students, key=lambda student: student[1],reverse=True)
#     # Return the name of the student with the highest score
#     k,y=max_student[0]
#     print(f"{k}={y}")

# # Example usage
# students = [("Alice", 85), ("Bob", 95), ("Charlie", 90)]
# highest_score(students)


# x=int(input("Enter the start : "))
# y=int(input("Enter the end : "))

# def arm(n):
#     s=str(n)
#     l=len(s)
    
#     armstrong=sum(int(i)**l for i in s)
#     return armstrong == n

# for i in range(x,y+1):
#     if arm(i):
#         print(i)


Write a Python program to combine two dictionaries by adding values for common keys.
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 30, 'c': 40, 'd': 50}
combined_dict ={}
for key in dict1:
    if key in dict2:
        combined_dict[key] = dict1[key] + dict2[key]
    else:
        combined_dict[key] = dict1[key]
for key in dict2dict2:
    if key not in combined_dict:
        combined_dict[key] = dict2[key]
print("Combined dictionary:", combined_dict)
Sample Output :
Combined dictionary: {'a': 10, 'b': 50, 'c': 70, 'd': 50}
Write a Python program to convert a dictionary of lists into a list of dictionaries.
dict_of_lists = {'Name': ['John', 'Alice', 'Bob'],
                 'Age': [25, 30, 35],
                 'City': ['New York', 'Paris', 'London']}
list_length =len(next(iter(dict_of_lists.values())))
list_of_dicts =[]
for i in range(list_length):
    new_dict = {]
    for key, values in dict_of_lists.items():
        new_dict[key] = values[i]
for dictionary in list_of_dicts:
    print(dictionary)
Sample Output:
{'Name': 'John', 'Age': 25, 'City': 'New York'}
{'Name': 'Alice', 'Age': 30, 'City': 'Paris'}
{'Name': 'Bob', 'Age': 35, 'City': 'London'}
Write a Python program to create a dictionary from two lists, where one list contains keys and the other contains values.
keys = ['Name', 'Age', 'City']
values = ['John', 25, 'New York']
result_dict = dict(zip(keys, values))
print("Dictionary from two lists:", result_dict)
Sample Output :
Dictionary from two lists: {'Name': 'John', 'Age': 25, 'City': 'New York'}
Write a Python program to create a dictionary of dictionaries.
inner_dict1 = {'a': 1, 'b': 2, 'c': 3}
inner_dict2 = {'x': 10, 'y': 20, 'z': 30}
outer_dict = {'dict1': inner_dict1, 'dict2': inner_dict2}
print("Dictionary of dictionaries:", outer_dict)
Sample Output :
Dictionary of dictionaries: {'dict1': {'a': 1, 'b': 2, 'c': 3}, 'dict2': {'x': 10, 'y': 20, 'z': 30}}
Write a Python program to create a dictionary where the keys are numbers from 1 to 5 and the values are their squares.
square_dict = {}
for num in range(1, 6):
    square_dict[num] = num ** 2
print(square_dict)
Sample Output :
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Write a Python program to find the second largest value in a dictionary.
data = {'a': 10, 'b': 20, 'c': 30, 'd': 15, 'e': 25}
unique_values = sorted(set(data.values()), reverse=True)
if len(unique_values) >= 2:
    second_largest = unique_values[1]
    keys = [key for key, value in data.items() if value == second_largest]
    print(f"The second largest value in the dictionary is {second_largest}.")
    print(f"It appears with key(s): {keys}")
else:
    print("There is no second largest value in the dictionary.")
Sample Output :
The second largest value in the dictionary is 25.
It appears with key(s): ['e']
Write a Python program to multiply all the values in a dictionary.
data = {'a': 2, 'b': 3, 'c': 4}
product = 1
for value in data.values():
    product *= value
print("Product of all values in the dictionary:", product)
Sample Output 
Product of all values in the dictionary: 24
Write a Python program to print a dictionary in table format.
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'London']}
max_lengths = {key: max(len(str(key)), max(len(str(x)) for x in values)) for key, values in data.items()}
print("|", end="")
for key, max_length in max_lengths.items():
    print(f" {key.ljust(max_length)} |", end="")
print()
print("+", end="")
for _, max_length in max_lengths.items():
    print(f"-{'-' * max_length}-+", end="")
print()
for i in range(len(data['Name'])):
    print("|", end="")
    for key, values in data.items():
        print(f" {str(values[i]).ljust(max_lengths[key])} |", end="")
    print()
print("+", end="")
for _, max_length in max_lengths.items():
    print(f"-{'-' * max_length}-+", end="")
print()
Sample Output :
| Name   | Age | City    |
+--------+-----+---------+
| John   | 25  | New York|
| Alice  | 30  | Paris   |
| Bob    | 35  | London  |
+--------+-----+---------+
  Write a Python program to sort a dictionary by its keys.
  data = {'b': 2, 'a': 1, 'c': 3}
sorted_data = dict(sorted(data.items()))
print("Sorted dictionary by keys:", sorted_data)
Sample Output :
Sorted dictionary by keys: {'a': 1, 'b': 2, 'c': 3}
Write a Python program to update the values of a specific key in a dictionary.
data = {'a': 1, 'b': 2, 'c': 3}
data['b'] = 20
print("Updated dictionary:", data)
Sample Output :
Updated dictionary: {'a': 1, 'b': 20, 'c': 3}
You are developing a dictionary-based spelling checker. Write a Python program to check the spelling of words in a document using a dictionary of valid words.
You are developing a dictionary-based spelling checker. Write a Python program to check the spelling of words in a document using a dictionary of valid words.
Sample Dictionary: valid_words = {'apple', 'banana', 'orange', 'grape'}
Sample Output: Misspelled words: ['aple', 'bannana']
valid_words = {'apple', 'banana', 'orange', 'grape'}
document = input("Enter the document: ")
words = document.split()
misspelled_words = []
for word in words:
    if word.lower() not in valid_words:
        misspelled_words.append(word)
print("Misspelled words:", misspelled_words)
Sample output :
Enter the document: apple banana grape strawberry
Misspelled words: ['strawberry']
You are developing a movie recommendation system. Write a Python program to recommend movies to a user based on their preferences stored in a dictionary.
You are developing a movie recommendation system. Write a Python program to recommend movies to a user based on their preferences stored in a dictionary.
Sample Dictionary: preferences = {'Action': ['The Dark Knight', 'Inception'], 'Comedy': ['The Hangover', 'Superbad']}
Sample Output: Recommendations: ['The Dark Knight', 'Inception']
preferences = {}
num_genres = int(input("Enter the number of genres: "))
for _ in range(num_genres):
    genre = input("Enter the genre: ")
    movies = input(f"Enter the movies for {genre} (comma-separated): ").split(',')
    preferences[genre] = [movie.strip() for movie in movies]
user_preferences = input("Enter your movie preferences (comma-separated): ").split(',')
recommendations = []
for genre, movies in preferences.items():
    recommended_movies = [movie for movie in movies if movie not in user_preferences]
    recommendations.extend(recommended_movies)
print("Recommendations:", recommendations)
Sample Output :
Enter the number of genres: 2
Enter the genre: Action
Enter the movies for Action (comma-separated): The Dark Knight, Inception
Enter the genre: Comedy
Enter the movies for Comedy (comma-separated): The Hangover, Superbad
Enter your movie preferences (comma-separated): Inception, The Hangover
Recommendations: ['The Dark Knight', 'Superbad']
You are developing a voting system for a school election. Write a Python program to count the number of votes each candidate receives and store the results in a dictionary. Sample Dictionary: votes = {'Candidate1': 150, 'Candidate2': 200, 'Candidate3': 180} Sample Output: Candidate1: 150, Candidate2: 200, Candidate3: 180 Note : input from the user
You are developing a voting system for a school election. Write a Python program to count the number of votes each candidate receives and store the results in a dictionary.
Sample Dictionary: votes = {'Candidate1': 150, 'Candidate2': 200, 'Candidate3': 180}
Sample Output: Candidate1: 150, Candidate2: 200, Candidate3: 180
Note : input from the user
votes = {}
num_candidates = int(input("Enter the number of candidates: "))
for i in range(1, num_candidates + 1):
    candidate_name = input(f"Enter the name of candidate {i}: ")
    vote_count = int(input(f"Enter the number of votes for {candidate_name}: "))
    votes[candidate_name] = vote_count
print("Dictionary of votes:", votes)
print("Output:")
for candidate, count in votes.items():
    print(f"{candidate}: {count}")
Sample Output :
Enter the number of candidates: 3
Enter the name of candidate 1: Candidate1
Enter the number of votes for Candidate1: 150
Enter the name of candidate 2: Candidate2
Enter the number of votes for Candidate2: 200
Enter the name of candidate 3: Candidate3
Enter the number of votes for Candidate3: 180
Dictionary of votes: {'Candidate1': 150, 'Candidate2': 200, 'Candidate3': 180}
Output:
Candidate1: 150
Candidate2: 200
Candidate3: 180
# You are implementing a word frequency counter for a text processing application. Write a Python program to count the frequency of each word in a given text and store the results in a dictionary.
Sample Text: "This is a sample text. This text contains sample words."
Sample Output: {'This': 2, 'is': 1, 'a': 1, 'sample': 2, 'text.': 1, 'contains': 1, 'words.': 1}
text = input("Enter the text: ")
words = text.split()
word_freq = {}
for word in words:
    word = word.strip('.,?!')
    word = word.lower()
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word frequency count:")
print(word_freq)
sample output :
Enter the text: This is a sample text. This text contains sample words.
Word frequency count:
{'this': 2, 'is': 1, 'a': 1, 'sample': 2, 'text': 1, 'contains': 1, 'words': 1}
# You have a dictionary representing student grades in various subjects. Write a Python program to calculate the average grade for each student.
  You have a dictionary representing student grades in various subjects. Write a Python program to calculate the average grade for each student.
Sample Dictionary: grades = {'John': [85, 90, 88], 'Alice': [75, 80, 82], 'Bob': [92, 88, 90]}
Sample Output: John: 87.67, Alice: 79.00, Bob: 90.00
grades = {}
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    student_name = input(f"Enter the name of student {i+1}: ")
    student_grades = input(f"Enter the grades for {student_name} (comma-separated): ").split(',')
    student_grades = [int(grade.strip()) for grade in student_grades]  # Convert grades to integers
    grades[student_name] = student_grades
average_grades = {student: sum(grades) / len(grades) for student, grades in grades.items()}
print("Average grades:")
for student, avg_grade in average_grades.items():
    print(f"{student}: {avg_grade:.2f}")
Sample Output :
Enter the number of students: 3
Enter the name of student 1: John
Enter the grades for John (comma-separated): 85, 90, 88
Enter the name of student 2: Alice
Enter the grades for Alice (comma-separated): 75, 80, 82
Enter the name of student 3: Bob
Enter the grades for Bob (comma-separated): 92, 88, 90
Average grades:
John: 87.67
Alice: 79.00
Bob: 90.00
                                                                                                                              
# You have a list of strings representing names of students in a class. Write a Python program to Remove any duplicate names from the list and print the updated list.
  student_names = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve"]
unique_names = []
for name in student_names:
    if name not in unique_names:
        unique_names.append(name)
print("Updated list of unique names:", unique_names)
Sample Output :
Updated list of unique names: ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
#You have a list of strings representing words. Develop a Python program to Count the number of vowels (a, e, i, o, u) in each word and print the word along with its vowel count.
words = ["hello", "world", "python", "programming", "example"]
for word in words:
    vowel_count = 0
    for char in word:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
    print(f"Word: {word}, Vowel Count: {vowel_count}")
Sample Output :
Word: hello, Vowel Count: 2
Word: world, Vowel Count: 1
Word: python, Vowel Count: 1
Word: programming, Vowel Count: 3
Word: example, Vowel Count: 3
# You have a list of temperatures measured in Celsius. Write a Python program to Convert each temperature to Fahrenheit and print the resulting list.
temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = []
for celsius in temperatures_celsius:
    fahrenheit = (celsius * 9/5) + 32
    temperatures_fahrenheit.append(fahrenheit)
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
Sample Output :
Temperatures in Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]
# You have a list of tuples representing (name, age) pairs of people. Write a Python program to convert this list of tuples into a dictionary where the names are keys and the ages are values
people = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
people_dict = {}
for name, age in people:
    people_dict[name] = age
print("Dictionary with names as keys and ages as values:", people_dict)
Sample Output: 
Dictionary with names as keys and ages as values: {'Alice': 25, 'Bob': 30, 'Charlie': 35}
# You have a list of tuples, each containing a student's name and their corresponding scores in three subjects (Math, Physics, Chemistry). Write a Python program to sort the list of tuples based on the total score (sum of scores in all subjects) in descending order.
You have a list of tuples, each representing a person's name and their corresponding age (e.g., [("Alice", 25), ("Bob", 30), ...]). Write a Python program to Calculate the average age of all the people in the list and print it.students_scores = [("Alice", 90, 85, 95), ("Bob", 80, 75, 85), ("Charlie", 95, 90, 100)]
sorted_students = sorted(students_scores, key=lambda x: sum(x[1:]), reverse=True
print("Sorted list of tuples based on total score (in descending order):")
for student in sorted_students:
    print(student)
Sample Output :
Sorted list of tuples based on total score (in descending order):
('Charlie', 95, 90, 100)
('Alice', 90, 85, 95)
('Bob', 80, 75, 85)
# You have a list of tuples, each representing a person's name and their corresponding age (e.g., [("Alice", 25), ("Bob", 30), ...]). Write a Python program to Calculate the average age of all the people in the list and print it.
people = [("Alice", 25), ("Bob", 30), ("Charlie", 40), ("David", 35)]
total_age = 0
count = 0
for person in people:
    age = person[1]
    total_age += age
    
    count += 1
average_age = total_age / count
print("Average age:", average_age)

Sample Output : Average age: 32.5


# You have a tuple containing the names of months in a year. Write a Python program to slice the tuple and create a new tuple containing only the names of the first half of the months.


months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
first_half_months = months[:len(months)//2]
print("Names of the first half of the months:", first_half_months)
Sample Output :
Names of the first half of the months: ('January', 'February', 'March', 'April', 'May', 'June')

# You have two lists of integers. Develop a Python program to create a new list that contains the common elements present in both lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)
print("Common elements:", common_elements)
Sample Output :
Common elements: [4, 5]

# You have two tuples containing integers. Write a Python program to concatenate the two tuples and create a new tuple with the elements from both tuples.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print("Concatenated tuple:", new_tuple)
Sample output:
Concatenated tuple: (1, 2, 3, 4, 5, 6)

# You have two tuples representing dates in the format (year, month, day). Write a Python program to compare the two dates and print whether the first date is earlier, later, or the same as the second date.

date1 = (2022, 10, 15)
date2 = (2023, 5, 20)
if date1 < date2:
    print("The first date is earlier than the second date.")
elif date1 > date2:
    print("The first date is later than the second date.")
else:
    print("The first date is the same as the second date.")
Sample Output:
Sample tuples
date1 = (2022, 10, 15)
date2 = (2023, 5, 20)
Expected output
The first date is earlier than the second date.

# You're creating a budget tracking application. Write a Python program to calculate the total expenses for each category stored in a dictionary.

You're creating a budget tracking application. Write a Python program to calculate the total expenses for each category stored in a dictionary.
Sample Dictionary: expenses = {'Food': [100, 150], 'Transportation': [50, 75], 'Entertainment': [75, 100]}
Sample Test Case: expenses
Sample Output: {'Food': 250, 'Transportation': 125, 'Entertainment': 175}

expenses = {}

num_categories = int(input("Enter the number of categories: "))

for _ in range(num_categories):
    category = input("Enter the category: ")
    amounts = input(f"Enter the expenses for {category} (comma-separated): ").split(',')
    expenses[category] = [int(amount.strip()) for amount in amounts]

total_expenses = {category: sum(amounts) for category, amounts in expenses.items()}

print("Total expenses:")
print(total_expenses)
Sample output :
Enter the number of categories: 3
Enter the category: Food
Enter the expenses for Food (comma-separated): 100, 150
Enter the category: Transportation
Enter the expenses for Transportation (comma-separated): 50, 75
Enter the category: Entertainment
Enter the expenses for Entertainment (comma-separated): 75, 100
Total expenses:
{'Food': 250, 'Transportation': 125, 'Entertainment': 175}

# You're developing a hotel reservation system. Write a Python program to check the availability of rooms for a given date stored in a dictionary.

You're developing a hotel reservation system. Write a Python program to check the availability of rooms for a given date stored in a dictionary.
Sample Dictionary: room_availability = {'Standard': {'2024-04-12': 10, '2024-04-13': 5}, 'Deluxe': {'2024-04-12': 5, '2024-04-13': 2}}
Sample Test Case: '2024-04-13'
Sample Output: {'Standard': 5, 'Deluxe': 2}

room_availability = {
    'Standard': {'2024-04-12': 10, '2024-04-13': 5},
    'Deluxe': {'2024-04-12': 5, '2024-04-13': 2}
}

date = input("Enter the date (YYYY-MM-DD): ")

availability = {room_type: availability.get(date, 0) for room_type, availability in room_availability.items()}

print("Room availability for", date + ":", availability)
Sample Output:
Enter the date (YYYY-MM-DD): 2024-04-13
Room availability for 2024-04-13: {'Standard': 5, 'Deluxe': 2}

# You work for a finance company that manages investment portfolios for clients. Your team is tasked with analyzing the performance of various investment instruments over time. Each instrument's performance is represented as a list of tuples, where each tuple contains the date and the corresponding value of the investment. Your task is to identify the investment instrument that has shown the highest growth rate over a specified period.
# Design a Python program to analyze the performance of investment instruments. Create lists to represent the performance data of three investment instruments over time. Then, prompt the user to enter a start and end date for the analysis period. Calculate the growth rate for each instrument over the specified period and determine which instrument has shown the highest growth rate. Display the name of the instrument along with its growth rate.

instrument1 = [("2023-01-01", 1000), ("2023-03-01", 1200), ("2023-06-01", 1400)]
instrument2 = [("2023-01-01", 2000), ("2023-03-01", 1800), ("2023-06-01", 2500)]
instrument3 = [("2023-01-01", 1500), ("2023-03-01", 1700), ("2023-06-01", 1800)]

start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

max_growth_rate = -1
best_instrument = None

def date_to_int(date):
    year, month, day = map(int, date.split('-'))
    return year * 10000 + month * 100 + day

for instrument, data in [("Instrument 1", instrument1), ("Instrument 2", instrument2), ("Instrument 3", instrument3)]:
    start_value = None
    end_value = None

    for date, value in data:
        if date_to_int(date) == date_to_int(start_date):
            start_value = value
        elif date_to_int(date) == date_to_int(end_date):
            end_value = value

    if start_value is not None and end_value is not None:
        growth_rate = ((end_value - start_value) / start_value) * 100
        print(f"{instrument}: Growth rate = {growth_rate:.2f}%")

        if growth_rate > max_growth_rate:
            max_growth_rate = growth_rate

print(f"The instrument with the highest growth rate is {best_instrument} with a growth rate of {max_growth_rate:.2f}%.")


Sample Output :
Instrument 1: Growth rate = 40.00%
Instrument 2: Growth rate = 25.00%
Instrument 3: Growth rate = 20.00%
The instrument with the highest growth rate is Instrument 1 with a growth rate of 40.00%.

# You are part of a team developing an inventory management system for a retail company. The system needs to track product availability across multiple warehouses. Each warehouse is represented as a list of tuples, where each tuple contains the product identifier and the quantity available. Your task is to implement a feature that checks if a given product is available in any of the warehouses and returns the total quantity available.
# Design a Python program to implement the inventory management system. Create lists to represent three warehouses, each containing tuples of product identifiers and quantities available. Then, prompt the user to enter a product identifier and check if the product is available in any of the warehouses. If available, display the total quantity available across all warehouses; otherwise, display a message indicating that the product is out of stock.

warehouse1 = [("product1", 50), ("product2", 30), ("product3", 20)]
warehouse2 = [("product4", 40), ("product2", 20), ("product5", 60)]
warehouse3 = [("product6", 70), ("product3", 10), ("product7", 25)]

product_id = input("Enter product identifier: ")

total_quantity = 0
found = False

for warehouse in [warehouse1, warehouse2, warehouse3]:
    for item in warehouse:
        if item[0] == product_id:
            total_quantity += item[1]
            found = True
            break  

if found:
    print(f"Total quantity of product {product_id}: {total_quantity}")
else:
    print("Product is out of stock.")

Sample Output :
Total quantity of product product3: 30

'''You are working for a social media analytics company. Your team is responsible for analyzing user engagement metrics to provide insights to clients. One of your tasks involves identifying trending topics based on user comments. Each comment is represented as a tuple containing the comment text and the number of likes it received. Your goal is to develop a function to identify the top trending topics based on the frequency of specific keywords mentioned in the comments.
Design a Python function identify_trending_topics (comments: List[Tuple[str, int]], keywords: List[str]) -> List[str] that takes a list of comment tuples and a list of keywords as input. Each comment tuple consists of the comment text and the number of likes it received. The function should identify the top trending topics by counting the frequency of each keyword mentioned in the comments and return a list of keywords sorted in descending order of their frequency.
Ensure your implementation efficiently handles cases where multiple keywords have the same frequency. Provide explanations for your design choices and any assumptions made.'''

comments = [
    ("Great product, love the features!", 50),
    ("The customer service was terrible, won't recommend.", 20),
    ("Best purchase ever, highly recommended.", 100),
    ("The delivery was delayed, very disappointed.", 10),
    ("Amazing quality, exceeded my expectations.", 80)
]


keywords = ["product", "customer service", "recommend", "delivery", "quality"]


keyword_freq = {keyword: 0 for keyword in keywords}

for comment, likes in comments:
    for keyword in keywords:
        if keyword in comment.lower():
            keyword_freq[keyword] += 1


sorted_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)

top_trending_topics = [keyword for keyword, freq in sorted_keywords]

print("Top Trending Topics:")
for topic in top_trending_topics:
    print(topic)
Sample Output :
Top Trending Topics:
product
quality
recommend
delivery
customer service