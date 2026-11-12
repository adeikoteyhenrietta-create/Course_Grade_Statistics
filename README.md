# Course_Grade_Statistics

This activity analyzes student course grades from a tab-separated file using Python and Pandas. It sorts students by final exam score and reports the maximum, median, mean, and standard deviation for each assignment.

## Requirements

- Python 3
- pandas ("pip install pandas")

## How to run

From this folder run:

```
python course_grades_statistics.py
```

The program waits for an input. Type the name of a data file and press Enter. For example:

```
StudentInfo.tsv
```

## Datasets

I tested the program with two data files. StudentInfo.tsv is the example from the activity instructions and has 5 students with 3 assignments. grades.tsv is a second file I made with 6 students and 4 assignments to check that the program works with different columns.

Each file is tab-separated with a header row. The first two columns are "Lname" and "Fname". The other columns are assignment scores and one of them must be "Final". The program does not assume any other column names so it works with any number of assignments.

## Understanding the output

1. Sorted table shows all students from the highest to the lowest "Final" score. The number on the left of each row is the student's original row position in the file. Pandas keeps it after sorting.
2. Max Scores: shows the highest score in each assignment.
3. Median Scores: shows the middle score in each assignment.
4. Average Scores: shows the mean score in each assignment.
5. Standard Deviation: shows the sample standard deviation of each assignment. 

The name columns are left out of the statistics with "numeric_only=True".