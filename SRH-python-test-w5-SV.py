# Big Data Programming: Pyhton Module Test
# Instructions ...
# Please consider good style & naming while developing the code when necessary,
#  such as Docstring, linting, etc. it is considered in the grading process!
# Use this file for the solution only. Jupyter notebook(.ipynb) not acceptable!
# Push the solution to a remote repo of name "SRH-Python-Test", and send me the link of the repo as DM
#  on Ms Teams for assessment.
# The duration of this test is 1 hour.

# Q1: What is the main difference between the list and Tuple?
"""
    Lists are mutable, which means they can be changed after they are created.
    Tuples, on the other hand, are immutable, meaning they cannot be changed after they are created.
"""


# Q2: why should list indexing be used Python?
"""
    List indexing are important in Python cause problems with
"""


# Q3: You have two lists (string_list, values_list) below. Write a function of
#  a name count_car. The function returns a dictionary.
#  The expected return of the function should print out this dictionary:
#  {'Audi_Q5': 2, 'Honda_civic': 4, 'Mercedes_200E': 5, 'BMW_720': 7, 'VW_passat': 2}
# string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
#                'BMW_720', 'VW_passat']

# value_list = [2, 4, 5, 7, 2]

# def count_car(string_list, value_list):
    
#     car_dict = {}
#     string_list = list(set(string_list))  

#     for i in range(len(string_list)):
#         if string_list[i] not in car_dict:
#             car_dict[string_list[i]] = value_list[i]
#         else:
#             pass
#     return car_dict


# print(count_car(string_list, value_list))


# Q4: Write a function of a name double_even_numbers. The function squares the
#  even numbers only. Also, the function leaves the first element of the input
#  as is without getting squared regardless being even or odd number.
#  The function has one argument which is a numpy array of 100 elements of
#  integer type between 0-10.
#  The function returns an array. Use list comprehension in your answer.

# import numpy as np

# def double_even_numbers(np_arr):
#     # print(np_arr[0], np_arr[1:10])
#     return [i ** 2 for i in np_arr[1:] if i % 2 == 0]

# print(double_even_numbers(np.random.randint(0, 10, 100))[:10])


# Q5: Read "movies.csv" file, a file is provided. Create a function
#  returns only table of elements before 2000 with score 7 and above, then save
#  the elements in a new csv file with a name "dest_csv". 
import csv

def filter_movies(input_file, output_file):
    with open(input_file, 'r', newline='') as in_file:
        reader = csv.DictReader(in_file)
        
        filtered_rows = [row for row in reader if int(row['year']) < 2000 and float(row['score']) >= 7.0]
        
        if not filtered_rows:
            print("No movies found matching the criteria.")
            return
        
        # Write the filtered rows to the output file
        with open(output_file, 'w', newline='') as out_file:
            writer = csv.DictWriter(out_file, fieldnames=filtered_rows[0].keys())
            writer.writeheader()  # Write the column headers
            writer.writerows(filtered_rows)  # Write the filtered rows

    print(f"Filtered movies have been saved to {output_file}.")

# Input and output file paths
input_file = 'movies.csv'
output_file = 'movie_output.csv'

# Function call
filter_movies(input_file, output_file)




# Q6: Write a function of a name div_func. It returns the divsion of elements
#  in a list in reversed order. The function should pass the two lists below
#  without errors.

# import random
# random.seed(42)
# short_list = [1, 0, 2, 2, 20]
# long_list = [random.randrange(0, 10, 1) for i in range(15)]

# def div_func(short_list, long_list):
#     try:
#         return [short_list[i] / long_list[len(long_list) - 1 - i] for i in range(len(short_list))].reverse()
#     except ZeroDivisionError:
#         return "Error: Division by zero occurred"
    

# print(div_func(short_list, long_list))
