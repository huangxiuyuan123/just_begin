# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:10:11 2019

@author: Suzumiya.Haruhi
"""

class Student(object):
    def __init__(self, StudentNo, StudentName):
        self.StudentNo = StudentNo
        self.StudentName = StudentName
    def show():
        print("学号：",Student.StudentNo,"姓名：",Student.StudentName)
    
def main():
    student.show()
    
if __name__ == '__main__':
    student = Student
    student.StudentNo = input("输入你的学号：")
    student.StudentName = input("输入你的姓名：")
    main()
