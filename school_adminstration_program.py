# -*- coding: utf-8 -*-
"""school_adminstration_program.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17kENZaefdyBpiO_jd2T1XKJwZDC7IzB6
"""

import csv

def write_into_csv(info_list):
  with open('student_info.csv','a',newline='')as csv_file:
    write=csv.writer(csv_file)

    if csv_file.tell()==0:
       write.writerow(["Nmae","Age","Contact Number","E-mail Id"])

    write.writerow(info_list)


if __name__=='__main__':
  condition=True
  student_num=1

  while(condition):
    student_info=input("Enter student information for student #{} in the following format (Name Age Contact_Number E-mail_Id):".format(student_num))
    print("Entered information:",student_info)
    
    student_info_list=student_info.split(' ')
    print("Enter split up information is:"+ str(student_info_list))

    print("\nThe entered info is-\nName: {}\nAge: {}\nContact_Number: {}\nE-mail_Id: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    
    choice_check=input("Is the entered information correct? (y/n):")
    if choice_check=="y":
      write_into_csv(student_info_list)
      condition_check=input("Enter (y/n) if you want to enter information for another student: ")
      if condition_check=="y":
        condition=True
        student_num=student_num+1
      elif condition_check=="n":
        condition=False
    elif choice_check=='n':
      print("\nPlease re-enter the values!")