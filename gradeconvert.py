import re

yos_grade = re.compile('5\.[1-9]([0-5][abcd]?)?$')
french_grade = re.compile('([1-3]|[4-5][abcABC]?[+]?|[6-9]([abcABC][+]?)?)$')
v_grade = re.compile('[vV][bB0-9][0-9]?$')

def convert_grade(grade):
    if is_yos(grade):
        return "The yosemite grade " + grade + " is " + convert_from_yos(grade)
    elif is_french(grade):
        return "The french grade " + grade + " is " + convert_from_french(grade)
    else:
        return "I don't understand: " + grade

def is_yos(grade):
    return bool(yos_grade.match(grade))

def is_french(grade):
    return bool(french_grade.match(grade))

def convert_from_yos(us_grade):
    return us_grade

def convert_from_french(french_grade):
    return french_grade