student_list = []
totalScore = 300
​
print("Student Grade Calculator")
print("-------------------------")
numberOfStudent = int(input("Total number of students: ")) 
print("-------------------------")
​
def studentRecord():
    
    for count in range(0, numberOfStudent):
        studentName = str(input("Enter the name of student: "))
        englishScore = int(input("Enter {studentName}'s score in English: ".format(studentName = studentName)))
        scienceScore = int(input("Enter {studentName}'s score in Science: ".format(studentName = studentName)))
        mathScore = int(input("Enter {studentName}'s score in Mathematics: ".format(studentName = studentName)))
        studentTotalScore = englishScore + scienceScore + mathScore
        studentPercentage = (studentTotalScore/ totalScore)*100
        passFailStatus = ""
        
        if englishScore < 40 or scienceScore < 40 or mathScore < 40:
            passFailStatus = "Fail"
            
        elif englishScore >= 40 and scienceScore >= 40 and mathScore >= 40:
            passFailStatus = "Pass"
        
            
​
        student_list.append({
            'name': studentName,
            'englishScore': englishScore,
            'scienceScore': scienceScore,
            'mathScore': mathScore,
            'percentage': round(studentPercentage,2),
            'totalScore': studentTotalScore,
            'passFailStatus': passFailStatus
        })
        print("-------------------------")
    
def overall_calculation(student_list):
    totalMarks = 0
    englishAverage = 0
    scienceTotal = 0
    mathematicsTotal = 0
    percentageTotal = 0
    englishTotal = 0
​
    for index, eachStudentItem in enumerate(student_list):
        englishTotal = englishTotal + eachStudentItem['englishScore']
        scienceTotal = scienceTotal + eachStudentItem['scienceScore']
        mathematicsTotal = mathematicsTotal + eachStudentItem['mathScore']
        totalMarks = totalMarks + eachStudentItem['totalScore']
        percentageTotal = percentageTotal + eachStudentItem['percentage']
        percentageAverageRound = round(percentageTotal,2) # Rounding to 2 decimal place of float number
    
    print("----------Overall Record--------")
    print("English Average Mark: ", englishTotal/numberOfStudent)
    print("Science Average Mark: ", scienceTotal/numberOfStudent)
    print("Mathematics Average Mark: ", mathematicsTotal/numberOfStudent)
    print("Percentage Average: ", percentageAverageRound/numberOfStudent)
    print("Total Score Average: ", totalMarks/numberOfStudent)
   
​
def printStudentRecord():
    print("----------Student Record--------")
    for eachStudent in student_list:
        print(eachStudent)
    
​
​
# Calling Function
​
studentRecord()
printStudentRecord()
overall_calculation(student_list)
