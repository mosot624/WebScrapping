
import csv
import urllib.request
import xlsxwriter
import pickle
from bs4 import BeautifulSoup

URLarray = [
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/bpt",
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/cjp",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/rrz",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/dit5",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/afc",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/hmd1",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/thj10",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/ffl",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/fwl",		
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/nwh",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/dah56",
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/rkj",
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/cwl",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/cul",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/htp",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/ais",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/eds",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/rcs",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/nns",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/aos",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/nst",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/lgt",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/mxw",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/chz8",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/hem23",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/man27",
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/waa2",
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/alg25",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/cns",
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/phs",	
"http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/qqs"]

TeacherEmail =[]

def URLtoEmail(arraytoChange):
    for i in range(0,len(arraytoChange)):
        charArray = []
        for z in reversed(range(0,len(arraytoChange[i]))):
            if "/" in arraytoChange[i][z]:
                break
            else:
                charArray.append(arraytoChange[i][z])
        charArray.reverse()
        email = "".join(charArray)
        email += "@aber.ac.uk"
        TeacherEmail.append(email)
        
URLtoEmail(URLarray)

arrayOfClasses = []
arryOfClassesWithoutrepeating = []

pickleDic = open(r"C:\Users\PC\Desktop\CS foundation\teacherProfile.pickle","wb")
pickleClass = open(r"C:\Users\PC\Desktop\CS foundation\ClassProfile.pickle","wb")

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def checkingForRepeatingData(ele):
    for x in teacherProfile:
        if ele in x:
            return False
    return True

def writingDataInExcel(workSheet):
    row = 1
    col = 0
    for g in arrayOfClassesNotRep:
        workSheet.write(row,col,g)
        row+=1
    
       
    

def ImportingToExcel():
    location = r"C:\Users\PC\Desktop\CS foundation\ClassInfo.xlsx"
    worbook = xlsxwriter.Workbook(location)
    workSheet = worbook.add_worksheet('ClassesAndModules')
    workSheet.write(0,0,"Class")
    writingDataInExcel(workSheet)
    
    worbook.close()


def chackingCharacter(ele):
    if("Personal Website" in ele):
        z=0
    elif("ORCID" in ele):
        z=0
    elif("Twitter" in ele):
        z=0
    elif("Google Scholar" in ele):
        z=0
    elif("Research Portal Profile" in ele):
        z=0
    elif("Senior fellowship of the HEA (SFHEA), 2018" in ele):
        z=0
    elif("Student led teaching awards (SLTA), highly commended, technology enhanced learning category, 2016" in ele):
        z=0
    elif("Exemplary Course Awards (ECA), highly commended for Computer Vision, 2015" in ele):
        z=0
    elif("Exemplary Course Awards (ECA), highly commended for Client Side Graphics module, 2014" in ele):
        z=0
    elif("Student led teaching awards (SLTA), highly commended, teaching through technology category, 2013" in ele):
        z=0
    elif("Aberystwyth University Learning and Teaching Fellowship (AULTF), 2012" in ele):
        z=0
    elif("coordinator" in ele):
        z=0
    elif("Moderator" in ele):
        z=0
    elif("Monday" in ele):
        z=0
    elif("CS37420: E-Commerce: Implementation, Management and Security;" in ele):
        z=0
    elif("Computer Science Employability Coordinator (2016-18)" in ele):
        z=0
    elif("CS39430: Major Project: supervising projects;" in ele):
        z=0
    elif("CS39220: Minor Project: supervising projects." in ele):
        z=0
    elif("Computer Science Head of Admissions and Recruitment (2017+)" in ele):
        z=0
    elif("Computer Science Head of Admissions and Recruitment (2017+)" in ele):
        z=0
    elif("Email:" in ele):
        z=0
    elif(hasNumbers(ele) == False):
        if("Group" in ele):
            z=0
    elif(len(ele) == 9):
        z=0
    else:
        if(checkingForRepeatingData(ele)):
            teacherProfile.append(ele)
        return True

def checkingForRepeat(ele):
    for x in arrayOfClassesNotRep:
        if ele in x:
            return False
    return True

def AddingEmail():
    for x,j in zip(UserProfile.keys(),TeacherEmail):
        arrayOf = UserProfile[x]
        arrayOf.insert(1,j)
        UserProfile[x] = arrayOf

def settingUpID():
    for x in UserProfile.keys():
        teacherId = ""
        for i in UserProfile[x][1]:
            if (i == "@"):
                break
            else:
                teacherId = teacherId + str(i)
        UserProfile[x].insert(0,teacherId)            

###Main###   
URLtoUse = "http://www.aber.ac.uk/en/cs/staff-profiles/listing/profile/dit5/"

text_file = open(r"C:\Users\PC\Desktop\CS foundation\TeacherProfile.txt", "w")
text_file2 = open(r"C:\Users\PC\Desktop\CS foundation\ClassesProfile.txt", "w")
text_file3 = open(r"C:\Users\PC\Desktop\CS foundation\ClassesProfileVr2.txt", "w")


UserProfile = {}

bigestNo = 0
arrayOfClasses = []
arrayOfClassesNotRep = []
forAccessingStaffArray = 0


#Make multidimensional list, array or dic to call it later 
for ll in URLarray:
    teacherProfile = []
    FoundPhone = False
    soup = BeautifulSoup(urllib.request.urlopen(ll).read(), 'lxml')
    
    #dateExtract = soup('div',{"class":"grey-box-fe clearfix"})[0].find_all('li')
    dateExtract = soup.find_all('div',{"class":"content"})[0].find_all('li')
    
    
    personName = soup('nav',{"class":"breadcrumbs"})[0].find_all('li')
    
    """
    Remove "Research Portal Profile" in array
    Also remove value that ends with "group" but doesn't contain number
    Remove "twitter"
    Remove "personal website"
    "Google scholar"
    """
    
    personEle = personName[3].findChildren(recursive=False)
    personEle = personName[3].text.strip()
    teacherProfile.append(personEle)
    
    for x in dateExtract:
        ele = x.findChildren(recursive=False)
        ele = x.text.strip()
        if(chackingCharacter(ele)):
            z = 0
    z = 0
    
    
    UserProfile[forAccessingStaffArray] = teacherProfile
    
    forAccessingStaffArray = forAccessingStaffArray + 1
    #print()
    #print()
    i=0
    g=1
    #Makes class modue array
    qwer = 0
    for x in teacherProfile:
        #print(i)
        if("Office: E42, Llandinam Building" in personEle):
            arrayOfClasses.append(x)
            text_file2.write(x)
            text_file.write("\n")
        if("Phone:" in x):
            FoundPhone = True
        if(FoundPhone):
            if("Phone" in x):
                z = 0
            elif("Monday" in x):
                z = 0
            else:
                arrayOfClasses.append(x)
            g+=1
        
        i+=1
        
    #print(teacherProfile)
    forAccessingStaffArray+=1
    if(g > bigestNo):
        bigestNo = g
        
    
#This remove any repeating data
for g in arrayOfClasses:
    text_file3.write(g)
    text_file3.write("\n")
    if(checkingForRepeat(g)):
        arrayOfClassesNotRep.append(g)
        
for g in arrayOfClassesNotRep:
    text_file2.write(g)
    text_file2.write("\n")
    z=0
"""
for g in range(0,len(URLarray)):
    for q in range(0,len(UserProfile[g])):
        print(UserProfile[g][q])
    print(" ")
    """
AddingEmail()
settingUpID()
for x in UserProfile.keys():
    for z in UserProfile[x]:
        text_file.write(z)
        text_file.write("\n")
    text_file.write("\n")
    text_file.write("\n")
    



pickle.dump(UserProfile,pickleDic)
pickle.dump(arrayOfClassesNotRep,pickleClass)
pickleClass.close()
pickleDic.close()



print(arrayOfClassesNotRep)
    
print(bigestNo-2) 


text_file3.close()
text_file2.close()
text_file.close()

    
    
