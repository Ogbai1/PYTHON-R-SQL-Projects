def read_test_scores() :
   print("Enter all test scores: ")
Score1=int(input())
Score2=int(input())
Score3 = int(input())
Score4=int(input())
Score5=int(input())

def mark_grade():
    if 90 <= final_score <= 100:
        grade = 'A'
    elif 80 <= final_score <= 89:
        grade = 'B'
    elif 70 <= final_score <= 79:
        grade = 'C'
    elif 60 <= final_score <= 69:
        grade = 'D'
    else:
       grade = 'F'
    
    
