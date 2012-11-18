import re

yos_map={
    '5.1':'1',
    '5.2':'2',
    '5.3':'3',
    '5.4':'4a',
    '5.5':'4b',
    '5.6':'4c',
    '5.7':'5a',
    '5.8':'5b',
    '5.9':'5c',
    '5.10':'6a-6b+',
    '5.10a':'6a',
    '5.10b':'6a+',
    '5.10c':'6b',
    '5.10d':'6b+',
    '5.11':'6c-7a',
    '5.11a':'6c',
    '5.11b':'6c',
    '5.11c':'6c+',
    '5.11d':'7a',
    '5.12':'7a+-7c',
    '5.12a':'7a+',
    '5.12b':'7b',
    '5.12c':'7b+',
    '5.12d':'7c',
    '5.13':'7c+-8b',
    '5.13a':'7c+',
    '5.13b':'8a',
    '5.13c':'8a+',
    '5.13d':'8b',
    '5.14':'8b+-9a',
    '5.14a':'8b+',
    '5.14b':'8c',
    '5.14c':'8c+',
    '5.14d':'9a',
    '5.15':'9a+-9c',
    '5.15a':'9a+',
    '5.15b':'9b',
    '5.15c':'9b+',
    '5.15d':'9c'
}

french_map={
    '1':'5.1',
    '2':'5.2',
    '3':'5.3',
    '4':'5.4',
    '4a':'5.4',
    '4b':'5.5',
    '4+':'5.6',
    '4c':'5.6',
    '5':'5.7',
    '5a':'5.7',
    '5b':'5.8',
    '5+':'5.9',
    '5c':'5.9',
    '6a':'5.10a',
    '6a+':'5.10b',
    '6b':'5.10c',
    '6b+':'5.10d',
    '6c':'5.11a/b',
    '6c+':'5.11c',
    '7a':'5.11d',
    '7a+':'5.12a',
    '7b':'5.12b',
    '7b+':'5.12c',
    '7c':'5.12d',
    '7c+':'5.13a',
    '8a':'5.13b',
    '8a+':'5.13c',
    '8b':'5.13d',
    '8b+':'5.14a',
    '8c':'5.14b',
    '8c+':'5.14c',
    '9a':'5.14d',
    '9a+':'5.15a',
    '9b':'5.15b',
    '9b+':'5.15c',
    '9c':'5.15d'
}

v_map={
    'V0':'4',
    'V0+':'4+',
    'V1':'5',
    'V2':'5+',
    'V3':'6A',
    'V3+':'6A+',
    'V4':'6B',
    'V4+':'6B+',
    'V5':'6C',
    'V5+':'6C+',
    'V6':'7A',
    'V7':'7A+',
    'V8':'7B',
    'V8+':'7B+',
    'V9':'7C',
    'V10':'7C+',
    'V11':'8A',
    'V12':'8A+',
    'V13':'8B',
    'V14':'8B+',
    'V15':'8C',
    'V16':'8C+'
}

font_map={
    '4':'V0',
    '4+':'V0+',
    '5':'V1',
    '5+':'V2',
    '6A':'V3',
    '6A+':'V3+',
    '6B':'V4',
    '6B+':'V4+',
    '6C':'V5',
    '6C+':'V5+',
    '7A':'V6',
    '7A+':'V7',
    '7B':'V8',
    '7B+':'V8+',
    '7C':'V9',
    '7C+':'V10',
    '8A':'V11',
    '8A+':'V12',
    '8B':'V13',
    '8B+':'V14',
    '8C':'V15',
    '8C+':'V16'
}


yos_grade_pattern = '5\.[1-9]([0-5][abcd]?)?'
french_grade_pattern = 'F?([1-3]|[4-5][abcABC]?[+]?|[6-9]([abcABC][+]?)?)'
font_grade_pattern = '(font )?([4-5][abcABC]?[+]?|[6-8]([abcABC][+]?)?)'
v_grade_pattern = '[vV][0-9][0-9]?[+]?'
all_grades_pattern = '((' + yos_grade_pattern + \
                     ')|(' + french_grade_pattern + \
                     ')|(' + font_grade_pattern + \
                     ')|(' + v_grade_pattern + '))'

yos_grade_regex = re.compile(yos_grade_pattern)
french_grade_regex = re.compile(french_grade_pattern)
font_grade_regex = re.compile(font_grade_pattern)
v_grade_regex = re.compile(v_grade_pattern)
all_grades_regex = re.compile(all_grades_pattern)

def contains_grade(grade):
    return all_grades_regex.search(grade)

def get_all_grades(grade_text):
    return [x[0] for x in all_grades_regex.findall(grade_text)]

def convert_grade(grade, grade_map):
    if grade.lower() in grade_map:
        return grade_map[grade.lower()]
    elif grade.upper() in grade_map:
        return grade_map[grade.upper()]
    return None

def convert_all_grades(all_grades):
    converted_grades = []
    for grade in all_grades:
        print "Got grade: " + str(grade)
        #print "Got grade: " + str(grade)
        grade_tuple = ()
        ygrade = convert_grade(grade.replace('F', ''), french_map)
        frenchgrade = convert_grade(grade, yos_map)
        fontgrade = convert_grade(grade, v_map)
        vgrade = convert_grade(grade.replace('font ', ''), font_map)

        if ygrade:
            grade_tuple += ygrade,
        if frenchgrade:
            grade_tuple += frenchgrade,
        if fontgrade:
            grade_tuple += fontgrade,
        if vgrade:
            grade_tuple += vgrade,

        converted_grades.append(grade_tuple)

    return converted_grades


def convert(grade_text):
    print "Converting all grades in text: " + grade_text
    all_grades = get_all_grades(grade_text)
    print "Filtered out grades: " + str(all_grades)
    converted_grades = convert_all_grades(all_grades)

    for i, grade_tuple in enumerate(converted_grades):
        for grade in grade_tuple:
            print all_grades[i] + " is " + grade

    return converted_grades