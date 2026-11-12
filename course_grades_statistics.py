"""
Course Grade Statistics

Reads a tab-separated file of student grades and prints:
- the full table sorted by Final score (highest first)
- the maximum, median, average, and standard deviation
  of each assignment

Usage: run the program and enter the file name when prompted,

"""

import pandas as pd

file_name = input()
grades = pd.read_csv(file_name, sep='\t')

sorted_grades = grades.sort_values(by='Final', ascending=False)
print(sorted_grades.to_string())

print()
print('Max Scores:')
print(grades.max(numeric_only=True).to_string())

print()
print('Median Scores:')
print(grades.median(numeric_only=True).to_string())

print()
print('Average Scores:')
print(grades.mean(numeric_only=True).to_string())

print()
print('Standard Deviation:')
print(grades.std(numeric_only=True).to_string())
