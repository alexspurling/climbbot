import re

yos={
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

french={
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

v={
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

font={
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

yos_grade = re.compile('(5\.[1-9]([0-5][abcd]?)?)')
french_grade = re.compile('([1-3]|[4-5][abcABC]?[+]?|[6-9]([abcABC][+]?)?)')
font_grade = re.compile('([4-5][abcABC]?[+]?|[6-8]([abcABC][+]?)?)')
v_grade = re.compile('([vV][bB0-9][0-9]?[+]?)')

def get_yos_grade(grade):
    match = yos_grade.match(grade)
    if match:
        return match.group(1)
    return None

def get_french_grade(grade):
    match = french_grade.match(grade)
    if match:
        return match.group(1)
    return None

def get_font_grade(grade):
    match = font_grade.match(grade)
    if match:
        return match.group(1)
    return None

def get_v_grade(grade):
    match = v_grade.match(grade)
    if match:
        return match.group(1)
    return None

def contains_grade(grade):
    return get_yos_grade(grade) or\
           get_french_grade(grade)  or\
           get_font_grade(grade)  or\
           get_v_grade(grade)

def convert(grade_text):
    conv_grade = None
    v_grade = None

    ygrade = get_yos_grade(grade_text)
    ygrade = get_french_grade(grade_text)
    ygrade = get_font_grade(grade_text)
    ygrade = get_v_grade(grade_text)
    if ygrade:
        conv_grade = "F" + yos[ygrade]
        #Clean up the input - yosemite grade should always be lower case
        input_grade = ygrade.lower()
    elif upper_case_grade in v:
        conv_grade = "font " + v[upper_case_grade]
    else:
        if lower_case_grade in french:
            conv_grade = french[lower_case_grade]
        if upper_case_grade in font:
            v_grade = font[upper_case_grade]

    if conv_grade:
        response = input_grade + " is " + conv_grade
        if v_grade:
            response += " or " + v_grade
        return response
    raise ValueError('Invalid grade: ' + grade)