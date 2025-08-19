score = int(input("Enter the Score: "))

def grading_1():
    
    if score >= 90 and score <=100:
        print("Grade: A")
    elif score >=80 and score < 90:
        print("Grade: B")
    elif score >=70 and score < 80:
        print("Grade: C")
    elif score >=60 and score < 70:
        print("Grade: D")
    else:
        print("Grade: F")

#grading_1()


def grading_2():
    
    #creating a limit
    if 90 <= score <=100:
        print("Grade: A")
    elif 80 <= score < 90:
        print("Grade: B")
    elif 70 <= score < 80:
        print("Grade: C")
    elif 60 <= score < 70:
        print("Grade: D")
    else:
        print("Grade: F")
    
#grading_2()

def grading_3():
    
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
        
grading_3()

    