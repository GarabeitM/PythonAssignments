#Task 1:
def last_word(str_list):
    A = sorted(str_list)
    return print(f"""The string that starts with the latest letter of the alphabet is: "{A[-1]}" """)


list_of_words = ["redi", "school", "is", "nice"]
print("Task 1:")
A = last_word(list_of_words)

#Task 2:
def print_file(file_path):
    opened_file = open(file_path)
    read_file = opened_file.read()
    print(f"Your file reads: {read_file}")


print("Task 2:")
A = print_file(
    "C:\\Users\\PC\\Desktop\\Rest\\-ReDI\\Repositries\\PythonAssignments\\Lesson 14\\randomtext.txt")

#Task 3:
import random

def dice():
    return print(f"Your lucky number is: {random.randrange(1, 6)}")

print("Task 3:")
A = dice()
#Task 4:
import datetime
import calendar


def weekday_by_date(day, month, year):
    return calendar.day_name[
        datetime.date(day=day, month=month, year=year).weekday()]


A = weekday_by_date(24, 12, 2022)
print("Task 4:")
print(A)
#Task 5:
#There were multiple ways to complete this task, and the documentation stated that the ".perf_counter_ns" method is the highest available resolution to measure a short duration. However, the results varried as I ran this multiple times!
#So I also tried the ".time" method for comparison purposes, the results still varried so I couldn't tell which function is faster.
import time

# creating a million empty lists via list():
def time_list1(n):
    lists = [list() for _ in range(n)]
    
first_method = time_list1(1_000_000) 

# creating a million empty lists via []:  
def time_list2(n):
    lists = [[] for _ in range(n)]
    
second_method = time_list2(1_000_000) 
   
 #first_possible_solution: 
def timing_1(function, name_of_method):
    start_time = time.perf_counter_ns()
    
    time.sleep(1) #time is a package and sleep is a function inside that package
    function
    end_time = time.perf_counter_ns()
    duration = end_time - start_time
    duration_1= end_time - start_time
    print(f"Duration_1_{name_of_method} {duration_1}")
    return duration-1

print("Task 5:")      
A = timing_1(first_method, "list()")
B = timing_1(second_method, "[]")


if A > B:
    print("[] is faster")
else:
    print ("list () is faster")
    
#second_poosible_solution:
def timing_2(function, name_of_method):
    start_time = time.time()
    time.sleep(1)
    function
    end_time = time.time()
    duration_2 = end_time-start_time
    print(f"Duration_2_{name_of_method} {duration_2}") 
    return duration_2

C = timing_2(first_method, "list()")
D = timing_2(second_method, "[]")

if C > D:
    print("[] is faster")
else:
    print ("list () is faster")
    
#Task 6:
#I was able to get the general idea. However, I couldn't really figure out what this sentence means! "- Ignore the name of the input directory path itself for the search string"
#I decided on all files containing "sunrise" as a search pattern, btw just searching for "sunrise" resulted in an empty list!

import os
import fnmatch


def find_in_filenames(directory_path, search_pattern):
    result = []
    for root, dirs, files in os.walk(directory_path):
        for name in files:
            if fnmatch.fnmatch(name, search_pattern):
                result.append(os.path.join(root, name))
    return result
  
A = find_in_filenames(
    "C:\\Users\\PC\\Desktop\\Rest\\-ReDI\\Repositries\\L7-Portfolio", "*sunrise*.*")
print ("Task 6:")
print (A)




#import package.file 
#package.file.class
#from package.file import class or function or variable 
#package and llibraries are interchangeable 
#help(what ever you are having a problem with/ you can search )