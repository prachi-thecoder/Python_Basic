def get_grade(marks):
    if(marks>=89):
        return 'A GRADE'
    elif(marks>=79):
        return 'B GRADE'
    elif(marks>=69):
        return 'C GRADE'
    elif(marks>=59):
        return 'D GRADE'
    elif(marks>=49):
        return 'E GRADE'

def is_pass(marks):
    if(marks>=35):
        return 'student is pass'
    else:
       return 'student is fail'
