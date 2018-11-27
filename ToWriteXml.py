# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:59:31 2018

@author: PC
"""

import pickle
import xlsxwriter

#Code block no 1: importing Class info I'm finnish with class info
def writingDataInExcel(workSheet):
    row = 1
    col = 0
    for g in ClassInfo:
        workSheet.write(row,col,g)
        row+=1

def ImportingToExcel():
    location = r"C:\Users\PC\Desktop\CS foundation\ClassInfo.xlsx"
    worbook = xlsxwriter.Workbook(location)
    workSheet = worbook.add_worksheet('ClassesAndModules')
    workSheet.write(0,0,"Class")
    writingDataInExcel(workSheet)
    worbook.close()
#Code block no 1; Don't run code Within this comment block, it'll delete all your info

#Code block no 2:
    
def teacherClassConnection(workSheet):
    row = 1
    col = 0
    teaching = 5
    for x in TeacherProfile.keys():
        if (len(TeacherProfile[x]) <= 5):
            pass
        else:
            for y in range(len(TeacherProfile[x])-5):
                workSheet.write(row,col,TeacherProfile[x][0])
                col +=1
                workSheet.write(row,col,TeacherProfile[x][1])
                col +=1
                workSheet.write(row,col,TeacherProfile[x][2])
                col +=1
                workSheet.write(row,col,TeacherProfile[x][teaching])
                col = 0
                row +=1
                teaching+=1
            teaching=5
            
    
    
def importingTeacherAndClassConnection():
    location = r"C:\Users\PC\Desktop\CS foundation\TeacherClassConnection.xlsx"
    worbook = xlsxwriter.Workbook(location)
    workSheet = worbook.add_worksheet('TeacherInfo')
    workSheet.write(0,0,"Teacher ID")
    workSheet.write(0,1,"Name")
    workSheet.write(0,2,"Email")
    workSheet.write(0,3,"Module code")

    teacherClassConnection(workSheet)
    worbook.close()
#Code block no 2;

##Code block no 3:
def imporintTeacherDetail(workSheet):
    row = 1
    col = 0
    for x in TeacherProfile.keys():
        counter = 0
        for y in TeacherProfile[x]:
            if(counter>4):
                break
            print (y)
            workSheet.write(row,col,y)
            col += 1
            counter+=1
        col=0
        row += 1
   
def importingTeacherInfo():
    location = r"C:\Users\PC\Desktop\CS foundation\TeacherInfo.xlsx"
    worbook = xlsxwriter.Workbook(location)
    workSheet = worbook.add_worksheet('TeacherInfo')
    workSheet.write(0,0,"ID")
    workSheet.write(0,1,"Name")
    workSheet.write(0,2,"E-mail")
    workSheet.write(0,3,"Office")
    workSheet.write(0,4,"Phone")
    imporintTeacherDetail(workSheet)
    worbook.close()
##Code block no 3;

pickleInDic = open(r"C:\Users\PC\Desktop\CS foundation\teacherProfile.pickle","rb")
pickleInClass = open(r"C:\Users\PC\Desktop\CS foundation\ClassProfile.pickle","rb")

TeacherProfile = pickle.load(pickleInDic)
ClassInfo = pickle.load(pickleInClass)

print(len(TeacherProfile))
#settingUpID()
importingTeacherInfo()
importingTeacherAndClassConnection()
for x in TeacherProfile.keys():
    print(TeacherProfile[x])


"""
for x in TeacherProfile.keys():
    for i in TeacherProfile[x]:
        print(i)
    print()
    print()
"""



 