import utils

DATA_3 = utils.read_data('testdata3.csv')
DATA_4 = utils.read_data('testdata4.csv')
DATA_5 = utils.read_data('testdata5.csv')

INDEX_FIRST = 0
INDEX_LAST = 1
INDEX_PRONOUNS = 2
INDEX_DESCRIPTION = 3
INDEX_YEAR = 4
INDEX_MAJOR = 5
INDEX_IDEAL_MAJOR = 6
INDEX_BEVERAGE = 7
INDEX_EMOJI_FAV = 8
INDEX_LIVE_WHERE = 9
INDEX_LIVE_WITH = 10
INDEX_BIRTHDAY = 11
INDEX_FOOD = 12
INDEX_FUN_THING = 13
INDEX_LAT_NORTH = 14
INDEX_LAT_SOUTH = 15
INDEX_COOL_THING = 16
INDEX_THING_TO_MAKE = 17
INDEX_STUDY_TIME = 18
INDEX_STUDY_GOOD_AT = 19
INDEX_STUDY_HELP_WITH = 20

def first_last(data):
    """Returns the first and last name of each student as a list

    Each string in this list has the format '{first_name} {last_name}'

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        list[str]: a list of the first and last names of each student
    """
    # Hint: consider trying out f-strings!

    # TODO: Implement me!
    List_of_names = []
    for student in data:
        name = f'{student[INDEX_FIRST]} {student[INDEX_LAST]}'
        List_of_names.append(name)
    return List_of_names



def tea_enjoyers(data):
    """Returns the names of all students who prefer tea

    Concretely, returns a list of strings of the form:
      "{first_name} {last_name}"
    For all students include "tea" or "chai" in their preferred beverages

    NOTE: this must include any capitalization of tea and chai

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        list[string]: a list of names of tea-enjoying students
    """
    # Hint: as with the ramen function, consider using .lower and the in expression
    
    # TODO: Implement me!
    names = []
    for student in data:
        bev = student[INDEX_BEVERAGE].lower().strip()
        if (('chai' in bev) | ('tea' in bev)):
            names.append(f'{student[INDEX_FIRST]} {student[INDEX_LAST]}')
    return names




def coffee_enjoyers(data):
    """Returns the names of all students who prefer coffee

    Concretely, returns a list of strings of the form:
      "{first_name} {last_name}"
    For all students include any of the following in their preferred beverages:
      "coffee" or "espresso" or "brew" or "mocha" or "americano"

    NOTE: this must include any capitalization of these coffee variations

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        list[string]: a list of names of coffee-enjoying students
    """
    
    # TODO: Implement me!
    names = []
    for student in data:
        bev = student[INDEX_BEVERAGE].lower().strip()
        if (('coffee' in bev) | ('espresso' in bev) | ('brew' in bev) | ('mocha' in bev) | ('americano' in bev)):
            names.append(f'{student[INDEX_FIRST]} {student[INDEX_LAST]}')
    return names


def travelled_south(data):
    """Returns a list of all students who have travelled south of Key West

    Concretely, returns a list of strings of the form:
      f"{first_name} {last_name} ({student_lat}°)"
    For all students who have travelled SOUTH of the Key West  (24.555059 degrees N)
    (Based on their response to the question on southern latitude)

    Note the use of the special character ° in the output string
    
    Any student with an empty value for their southernmost latitude is not included

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        list[string]: a list of names of students who travelled south of Key West
    """
    # Hint: recall that you can convert (valid) strings to floats using float(string)
    # Hint: you can't convert an empty string to a float, so beware of errors!
    KEYWEST_LAT = 24.555059
    
    # TODO: Implement me!
    lst = []
    for student in data:
        if (student[INDEX_LAT_SOUTH] != ''):
            if (float(student[INDEX_LAT_SOUTH]) < KEYWEST_LAT):
                lst .append(f'{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_LAT_SOUTH]}°)')
    return lst

# ------------------------------------------
# Part 3

def list_majors(data):
    """Returns the full name, major, and ideal major for each student as a list

    Each string should have the format:
       "{first_name} {last_name} ({real_major}): {ideal_major}"

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        list[str]: a list of the major information of each student
    """
    # Hint: consider using f-strings to match the given formatting

    # TODO: Implement me! 
    lst = []

    for student in data:
        lst.append(f'{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_MAJOR]}): {student[INDEX_IDEAL_MAJOR]}')
    
    return lst

def cool_things(data):
    """Returns some "cool information" about each student as a list
    
    Specifically, for each student in data, this returns a list
      where each element is a list containing three string values:
        1. the first/last name of the student
        2. the cool thing a student has seen made with code
        3. a thing the student would like to make
    
    These strings have the following format, respectively:
    "{first_name} {last_name}"
    "\t{cool_thing}"
    "\t{thing_to_make}"

    (Note that '\t' is the tab character)

    NOTE: This only includes "cool thing" in the list the if the student has an answer to "cool thing"
      Similarly, this only includes "thing to make" in the list the if the student has an answer to "thing to make"
    NOTE: the second two strings (i.e. "cool thing" and "thing to make") must have 
      whitespace removed on either end

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        list[list[str]]: cool information about each student
    """
    # Hint: Use strip() to remove whitespace from either end of a string
    
    # TODO: Implement me!
    lst = []

    for student in data:
        value = []
        value.append(f'{student[INDEX_FIRST]} {student[INDEX_LAST]}')
        if (student[INDEX_COOL_THING] != ''):
            value.append(f'\t{student[INDEX_COOL_THING].strip()}')
        if (student[INDEX_THING_TO_MAKE] != ''):
            value.append(f'\t{student[INDEX_THING_TO_MAKE].strip()}')
        lst.append(value)

    return lst

def emojis(data):
    """Returns a list of the emojis preferred for each student

    Any emoji is permitted, including plain-text emoji such as :-)

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        list[str]: A list of student's favorite emojis
    """
    
    # TODO: Implement me!
    lst = []

    for student in data:
        if (student[INDEX_EMOJI_FAV] != ''):
            lst.append(student[INDEX_EMOJI_FAV])

    return lst

def study_partners(data):
    """Returns name and study-group information for interested students in data

    Specifically, for each student in data, this returns a list
      where each element is a list containing three string values:
        1. "{first_name} {last_name} {study_time}"
        2. "\t{good_at}"
        3. "\t{help_with}"
    
    Where good_at refers to the column where the student described their strengths
      and help_with refers to the column where the student described
      what they most need help with 

    NOTE: If a student doesn't include study_time, good_at, *and* help_with,
      The student is not considered to be "interested" and is not added to the list
    NOTE: You _may_ remove whitespace on either end (with strip) of each string
      but are not required to do so

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        list[list[str]]: study group information for each student
    """
    
    # TODO: Implement me!
    lst = []

    for student in data:
        if ((student[INDEX_STUDY_TIME] != '') & (student[INDEX_STUDY_HELP_WITH] != '') & (student[INDEX_STUDY_GOOD_AT] != '')):
            value = []
            value.append(f'{student[INDEX_FIRST]} {student[INDEX_LAST]} {student[INDEX_STUDY_TIME]}')
            value.append(f'\t{student[INDEX_STUDY_GOOD_AT].strip()}')
            value.append(f'\t{student[INDEX_STUDY_HELP_WITH].strip()}')
            lst.append(value)

    return lst

# ------------------------------------------
# Part 4

def graduation_years(data):
    """Returns a dictionary mapping graduation years to the number of students graduating in that year

    Graduation years and number of students are both given as integers

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        dict[int, int]: Dictionary mapping graduation years to number of students
    """
    # Hint: you can use int(s) to convert a string to an integer
    #   Note that, as with floats, empty strings cannot be converted to an integer
    # Note: it's bad style (and unnecessary) to hard-code specific 
    #   years for this problem (e.g. explicitly including 2026 and 2027)
    # Instead, how can you build your dictionary with each year as you encounter it?
    d = {}

    for student in data:
        if student[INDEX_YEAR] != '':
            if int(student[INDEX_YEAR]) not in d:
                d[int(student[INDEX_YEAR])] = 1
            else:
                d[int(student[INDEX_YEAR])] += 1
    return d

def birthday_buddies(data):
    """Returns a dictionary mapping birthdays to all birthday buddies on that date
        
    Birthday buddies are a list of students that all share a birthday
    Birthday buddies are included only if there is more than one student in the list
    Students are represented as strings in the format f'{first_name} {last_name}'

    Args:
        data (list[list[str]]): Dataset of students
    
    Returns:
        dict[str, list[str]]: Dictionary mapping birthdays to lists of students
    """
    # Hint: Create the dictionary up-front and add to it
    # After finding all birthday buddies, make a _second_ dictionary
    #  and only add keys/values from the first dictionary 
    #  if the value list has more than one element
    # Hint: remember, you can loop over the keys of a dictionary using a for loop!
    d1 = {}
    d2 = {}

    for student in data:
        if student[INDEX_BIRTHDAY] != '':
            if student[INDEX_BIRTHDAY] not in d1:
                d1[student[INDEX_BIRTHDAY]] = [f'{student[INDEX_FIRST]} {student[INDEX_LAST]}']
            else:
                d1[student[INDEX_BIRTHDAY]].append(f'{student[INDEX_FIRST]} {student[INDEX_LAST]}')

    for key in d1:
        if len(d1[key]) > 1:
            d2[key] = d1[key]
    return d2

print(birthday_buddies(DATA_3))
print(birthday_buddies(DATA_4))
print(birthday_buddies(DATA_5))