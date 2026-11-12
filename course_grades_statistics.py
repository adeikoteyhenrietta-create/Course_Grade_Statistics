"""
Course Grade Statistics

Reads a tab-separated file of student grades and prints:
- the full table sorted by Final score (highest first)
- the maximum, median, average, and standard deviation
  of each assignment
- the number of missing scores, if any are missing

Missing or non-numeric scores are left out of the statistics.
The program stops with a message if the file cannot be read
or has no Final column.

Usage: run the program and enter the file name when prompted,
e.g. StudentInfo.tsv or grades.tsv
"""

import sys
import pandas as pd

file_name = input()

try:
    grades = pd.read_csv(file_name, sep='\t')
except FileNotFoundError:
    print(f'Error: the file "{file_name}" was not found.')
    sys.exit(1)
except pd.errors.EmptyDataError:
    print(f'Error: the file "{file_name}" is empty.')
    sys.exit(1)

if 'Final' not in grades.columns:
    print('Error: the file must have a column named "Final".')
    sys.exit(1)

score_columns = grades.columns.drop(['Lname', 'Fname'], errors='ignore')
grades[score_columns] = grades[score_columns].apply(pd.to_numeric, errors='coerce')

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

missing = grades[score_columns].isna().sum()
if missing.sum() > 0:
    print()
    print('Missing Scores:')
    print(missing.to_string())
