# -*- coding: utf-8 -*-
"""Fibonacci_series.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w_NjtWF0479UXc1RZ-qQZe8gH6S1X4M6
"""

number=int(input("Enter the no. of terms for series:"))

first=0 #Initializing 1st term
second=1 #Initializing 2nd term
for i in range(number):
  if number<0:
    print("Series input value is smaller than 0")
  else:
    print(first) #We are printing the 1st term
    temp=first #Creating a temperary variable that stores the first value
    first=second #Here the second value will be stored in 1st variable 
    second=temp+second #Here the second variable will store the addition value