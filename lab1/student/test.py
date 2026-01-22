"""
Author: Declan Reed
Starting Date: Jan 20, 2026

Initial creation by Dietrich Geisler on 10/12/2025
Edits by Anastasia Kurdia on 1/14/2026

Test cases for the "getting to know you" analysis functions
"""

import utils
import analysis

# Constant data file information
# We use smaller data files than the "whole thing" to help us with testing
# Reminder: these are for you to use when testing also!

DATA_1 = utils.read_data('testdata1.csv')
DATA_2 = utils.read_data('testdata2.csv')

# TODO: add new data files here!
DATA_3 = utils.read_data('testdata3.csv')
DATA_4 = utils.read_data('testdata4.csv')
DATA_5 = utils.read_data('testdata5.csv')
# ---------------------------------------------------------
# Provided example functions
# You do not need to extend these tests

def test_first_name():
    """
    Test cases for first_name
    """
    expected = ['anonymous', 'test']
    result = analysis.first_name(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['test', 'anonymous', 'first', 'anonymous', 'ABCD', 'anonymous', 'anonymous']
    result = analysis.first_name(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('First name tests passed')

def test_introduction():
    """
    Test cases for introduction
    """
    expected = [
        ['Hi, this is anonymous!\n\tHello!'], 
        ['Hi, this is test!\n\tThis is a test!']
    ]
    result = analysis.introduction(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['Hi, this is test!\n\tthis is an introduction!'], 
        ['Hi, this is anonymous!\n\ta'], 
        ['Hi, this is ABCD!\n\t12345'], 
        ['Hi, this is anonymous!\n\thello world!']
    ]
    result = analysis.introduction(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('Introduction tests passed')

def test_cs_count():
    """
    Test cases for cs count
    """
    expected = 2 # note that economics has "cs" at the end, so we count it!
    result = analysis.cs_count(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 2
    result = analysis.cs_count(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('CS count tests passed')

# ---------------------------------------------------------
# Part 1 tests

def test_number_of_students():
    """
    Test cases for student count
    """
    expected = 2
    result = analysis.number_of_students(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 7
    result = analysis.number_of_students(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = 8
    result = analysis.number_of_students(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 9
    result = analysis.number_of_students(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 16
    result = analysis.number_of_students(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message


    print('Number of students tests passed')

def test_number_of_anonymous():
    """
    Test cases for anonymous count
    """
    expected = 1
    result = analysis.number_of_anonymous(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 4
    result = analysis.number_of_anonymous(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = 0
    result = analysis.number_of_anonymous(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 0
    result = analysis.number_of_anonymous(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 1
    result = analysis.number_of_anonymous(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    
    print('Number of anonymous tests passed')

def test_number_of_ramen_recommends():
    """
    Test cases for ramen recommends
    """
    expected = 0
    result = analysis.number_of_ramen_recommends(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 2
    result = analysis.number_of_ramen_recommends(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = 1
    result = analysis.number_of_ramen_recommends(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    expected = 1
    result = analysis.number_of_ramen_recommends(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 1
    result = analysis.number_of_ramen_recommends(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('Number of ramen recommends tests passed')

# ------------------------------------------------
# Part 2 Tests

def test_first_last():
    """
    Test cases for first last
    """
    expected = ['anonymous anonymous', 'test student']
    result = analysis.first_last(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        'test student', 
        'anonymous anonymous', 
        'first last',
        'anonymous anonymous', 
        'ABCD EFGH', 
        'anonymous anonymous', 
        'anonymous anonymous'
    ]
    result = analysis.first_last(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = ['Angela Zhou', 'Brandon anonymous', 'Kevin Huang', 'Graham  Gilbert-Schroeer ', 'Vaunshika Bagalwadi', 'Brooke Luce', 'Victor Martinez', 'Joaquin Noguera']
    result = analysis.first_last(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Aarav Prakash', 'Nicholas Tumelty', 'Hassan Almutkassi', 'Shakur Adewale', 'Cavin Becker', 'Gael Torres', 'Larson Jones', 'Declan Reed', 'Alvis  Peralta Mercado ']
    result = analysis.first_last(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Damian Arias', 'Rachel Yang', 'Aggie Kalinska', 'Nisema Dikeni', 'anonymous anonymous', 'Franco Arnaiz', 'Gin Tuang', 'Adanna Chikwendu', 'Suditi Challa', 'Isabella Vilches', 'Matthew Silveyra', 'Linden Berte', 'Charlotte Morton', 'Paguiyendou Sandrine Douti', 'Stephen Heller', 'Kane Kiep']
    result = analysis.first_last(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    print('First last tests passed')

def test_tea_enjoyers():
    """
    Test cases for tea enjoyers
    """
    expected = ['anonymous anonymous']
    result = analysis.tea_enjoyers(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['anonymous anonymous']
    result = analysis.tea_enjoyers(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = ['Angela Zhou', 'Vaunshika Bagalwadi', 'Brooke Luce']
    result = analysis.tea_enjoyers(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Hassan Almutkassi', 'Alvis  Peralta Mercado ']
    result = analysis.tea_enjoyers(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Rachel Yang', 'Nisema Dikeni', 'Paguiyendou Sandrine Douti', 'Kane Kiep']
    result = analysis.tea_enjoyers(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    print('Tea enjoyer tests passed')

def test_coffee_enjoyers():
    """
    Test cases for coffee enjoyers
    """
    expected = ['test student']
    result = analysis.coffee_enjoyers(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['anonymous anonymous', 'first last']
    result = analysis.coffee_enjoyers(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = ['Graham  Gilbert-Schroeer ']
    result = analysis.coffee_enjoyers(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = []
    result = analysis.coffee_enjoyers(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Aggie Kalinska', 'Matthew Silveyra']
    result = analysis.coffee_enjoyers(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('Coffee enjoyer tests passed')

def test_travelled_south():
    """
    Test cases for travelled_south
    """
    expected = ['test student (-12.123°)']
    result = analysis.travelled_south(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        'test student (9.940512411°)', 
        'anonymous anonymous (-37.81249621°)', 
        'anonymous anonymous (18.912096°)', 
        'anonymous anonymous (21.03557°)'
    ]
    result = analysis.travelled_south(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = ['Graham  Gilbert-Schroeer  (-55.97666°)', 'Vaunshika Bagalwadi (-34.6026°)', 'Brooke Luce (18.7357°)', 'Victor Martinez (20.643181°)', 'Joaquin Noguera (-2.89932°)']
    result = analysis.travelled_south(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    expected = ['Hassan Almutkassi (15.37782552°)', 'Larson Jones (20.916492°)']
    result = analysis.travelled_south(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Rachel Yang (19.07257114°)', 'Nisema Dikeni (-34.35630344°)', 'Franco Arnaiz (21.14°)', 'Suditi Challa (17.4065°)', 'Isabella Vilches (-33.44371°)', 'Linden Berte (-13.53771691°)', 'Charlotte Morton (-91°)', 'Paguiyendou Sandrine Douti (8.990269781°)', 'Stephen Heller (18°)']
    result = analysis.travelled_south(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    print('Travelled south tests passed')

# ------------------------------------------------
# Part 3 Tests

def test_list_majors():
    """
    Test cases for majors
    """
    expected = ['anonymous anonymous (Computer Science): Teleportation', 'test student (Economics): Underwater Basket Weaving']
    result = analysis.list_majors(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        'test student (biomedical engineering): kniitting', 
        'anonymous anonymous (Data Science): Pilates', 
        'first last (Materials Science and Engineering): wine design', 
        'anonymous anonymous (Industrial Engineering): travelling for fun', 
        'ABCD EFGH (CS): egyptian mythology', 
        'anonymous anonymous (Comp Sci): fire wizard', 
        'anonymous anonymous (Biomedical Engineering): Racecar driver'
    ]
    result = analysis.list_majors(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = ['Angela Zhou (Data Science): Transportation', 'Brandon anonymous (MechE): ', 'Kevin Huang (): ', 'Graham  Gilbert-Schroeer  (Mechanical Engineering): Sleeponomics', 'Vaunshika Bagalwadi (Chemistry): magic', 'Brooke Luce (MechE): MechE', 'Victor Martinez (MechE): Mechatronics', 'Joaquin Noguera (Mechanical Engineering): ']
    result = analysis.list_majors(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Aarav Prakash (Mechanical Engineering): ', 'Nicholas Tumelty (Materials Engineering): ', 'Hassan Almutkassi (Computer Science (Weinberg)): Voice acting', 'Shakur Adewale (Mechanical Engineering): mind reading', 'Cavin Becker (Applied math): ', 'Gael Torres (Biomedical Engineering): Movie watching', 'Larson Jones (Mechanical Engineering): pyrotechnics', 'Declan Reed (Mechanical Engineering): Aerospace Engineering', 'Alvis  Peralta Mercado  (Commputer Science): N/A']
    result = analysis.list_majors(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Damian Arias (Electrical Engineering): ', 'Rachel Yang (Biology ): interior design', 'Aggie Kalinska (Biomedical Engineering): social systems debugging ', 'Nisema Dikeni (Computer Science): Enigmatology - The science of puzzles', 'anonymous anonymous (): ', 'Franco Arnaiz (Mechanical Engineering): Internet Rabbit Hole Studies', 'Gin Tuang (MechE): ', 'Adanna Chikwendu (Computer Science): Concept Art', 'Suditi Challa (Industrial Engineering): People-watching', 'Isabella Vilches (Biomedical Engineering): ', 'Matthew Silveyra (Mechanical Engineering): napping', 'Linden Berte (Mechanical Engineers ): ', 'Charlotte Morton (Cognitive science): Cafe Studies', 'Paguiyendou Sandrine Douti (Mechanical Engineering): Acting', 'Stephen Heller (Mechanical Engineering): pedantic technically correct ranting', 'Kane Kiep (data science): soccer match analysis']
    result = analysis.list_majors(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    print('List Major tests passed')

def test_cool_things():
    """
    Test cases for cool things
    """
    expected = [
        ['anonymous anonymous', '\twebsite', '\tvideo games'], 
        ['test student']
    ]
    result = analysis.cool_things(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['test student', '\tinternet', '\ta website'], 
        ['anonymous anonymous', '\tgame', '\tgame'], 
        ['first last'], 
        ['anonymous anonymous', '\tcat videos'], 
        ['ABCD EFGH', '\tgoogle earth', '\tmedical software'], 
        ['anonymous anonymous', '\tdoom', '\tprosthetics'], 
        ['anonymous anonymous']
    ]
    result = analysis.cool_things(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = [['Angela Zhou', '\tData Scientist'], ['Brandon anonymous'], ['Kevin Huang'], ['Graham  Gilbert-Schroeer ', '\tPersonal website', '\tFun side projects'], ['Vaunshika Bagalwadi', '\tvideo games: dispatch', '\ta game!'], ['Brooke Luce', '\tgames', '\tgames'], ['Victor Martinez', '\tCoded Snake from scratch with Python', '\tCode Snake with Python'], ['Joaquin Noguera']]
    result = analysis.cool_things(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [['Aarav Prakash'], ['Nicholas Tumelty'], ['Hassan Almutkassi', '\tThe internet', '\tAn algorithm that figures out the absolute fastest way to get to places on campus (Shortcuts included)'], ['Shakur Adewale', '\tI would like to make my a flight tracking app that would look for cheap flights for me.'], ['Cavin Becker', '\tPuzzle robot'], ['Gael Torres', '\tCreating a video game', '\tCreating a programmed physical health assessment'], ['Larson Jones', '\tchat gpt', '\ta program'], ['Declan Reed', '\tan animated dragon that follows the mouse around on the screen', '\tMy above anwser'], ['Alvis  Peralta Mercado ', '\tN/A']]
    result = analysis.cool_things(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [['Damian Arias'], ['Rachel Yang'], ['Aggie Kalinska', '\tan algorithm analyzing social media ‘For You’ pages to determine the effect of social media use on the progression of individuals’ mental disorders', '\tanalyze different data (blood pressure, EEG signals, facial expressions) to quantify feelings and emotions'], ['Nisema Dikeni', '\tThe Harry Potter house sorting website', '\tAn application that improves accountability to the transportation system back home.'], ['anonymous anonymous'], ['Franco Arnaiz', "\tA 'useless' website selector website", '\tA videogame'], ['Gin Tuang', '\ta trash can that catches trash', '\ta personal app or device for Christians'], ['Adanna Chikwendu', '\tA game!! or a visual novel'], ['Suditi Challa', '\tA site that visualizes music as moving shapes and colors that react live to the song.', '\tI’d like to build a tool that includes task and deadline tracking, progress tracking over time, a centralized dashboard, and basic reminders or notifications.'], ['Isabella Vilches'], ['Matthew Silveyra', '\tvideo games', '\trobot'], ['Linden Berte', '\tThe Climate READi tool for electric grid risk assessment; found during internship search', '\tSomething sustainability related-- putting in data to get out the viability for underground carbon sequestration for example'], ['Charlotte Morton', '\tMusic visualizer', '\tsomething that can choose which Spotify playlist I want to listen to based on my moo'], ['Paguiyendou Sandrine Douti', '\tGames', '\tAn app'], ['Stephen Heller'], ['Kane Kiep', "\tA program that you can't beat in tic tac toe", '\tpersonal website']]
    result = analysis.cool_things(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    print('Cool things tests passed')

def test_emojis():
    """
    Test cases for emojis
    """
    expected = ['😟', '🍅']
    result = analysis.emojis(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['😟', '🐋', '😳', 'crying', '😛', '🌚', '🤯']
    result = analysis.emojis(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = [':)', '😐', '🌸', ':)', '🥀']
    result = analysis.emojis(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    expected = ['🤔', '🤑', '🦑', '🔥', 'Dominican Flag ']
    result = analysis.emojis(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['🐛', '🌟', '🪽', '🕺', '😁', '🥳', '🔥', '🤩', '💌', '🙂\u200d↔️', '🤓', '🫦']
    result = analysis.emojis(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    print('Emojis tests passed')

def test_study_partners():
    """
    Test cases for study partners
    """
    expected = [
        ['test student Tuesdays/Thursdays', '\torganization', '\tComplicated code']
    ]
    result = analysis.study_partners(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['test student after 5pm', '\tcommunication', '\tdetails of code'], 
        ['ABCD EFGH anytime', '\tmotivation', '\tintuition'], 
        ['anonymous anonymous whenever', '\tpatience', "\tI'll need some support getting going"], 
        ['anonymous anonymous 11:00-12:00', '\torganization', '\tgeneral background']
    ]
    result = analysis.study_partners(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = [['Angela Zhou Tuesday afternoons', '\tActive Communication', '\tUnderstanding coding rules'], ['Graham  Gilbert-Schroeer  After two any weekday but Wednesday ', '\tExperience, I’ve been coding for 6 years', '\tLarge project organization'], ['Vaunshika Bagalwadi thursdays afternoons!', '\tI love talking to people and collaborating', '\tpair coding!']]
    result = analysis.study_partners(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [['Hassan Almutkassi Tuesday mornings or weekends', '\tProblem solving and problem mapping (finding a way to the solution using what we know)', '\tGeneral coding skills and help me simplify my code'], ['Shakur Adewale anytime past 5', '\tI have very basic coding knowledge so I am not particularly good at anything', '\tmaking my code organized and sharper.'], ['Larson Jones wednesday afternoons', '\texplaining stuff', '\tcoding'], ['Declan Reed Monday or Wednesday from 10-12', '\tWriting the actual code', '\tfiguring out where to start']]
    result = analysis.study_partners(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [['Aggie Kalinska mon 2-5 pm + after 6pm; tue and thu after 11am; wed after 3pm; fri after 2 pm; weekends anytime but 4-6pm', '\tplanning, organization, research, reflections & goals, task division, and project management', '\thow to translate ideas into code - how to break them down into codable steps; how to learn syntax effectively'], ['Nisema Dikeni Monday to Friday 8pm to 10pm or between 2pm and 10pm on a Thursday', '\tI am good at keeping the group focused, great with breaking down programming problems and overall I am good with organisation', '\tI need help writing more efficient, clean code because I have a tendency to overcomplicate code.'], ['Franco Arnaiz Tuesday mornings, Wednesday evenings, Thursday afternoons, or the weekend', '\tI am good at breaking down big problems into smaller parts', '\tFinding concise solutions and optimizing code'], ['Gin Tuang usually after 6pm', '\torganization and quality checks', '\tunderstanding coding language and to code from scratch'], ['Suditi Challa Tuesday/Thursday all day, Monday/Wednesday/Friday after 2', '\tI’m good at figuring things out by working through them carefully. I don’t usually get things instantly, but once I understand something, I can explain it clearly and help others who are stuck.', '\tI struggle with writing clean, efficient solutions on my first try. I often know a way to solve a problem, but not the best way.'], ['Linden Berte mornings, first class at 11', '\ttime management and organization', "\tI'm new to Python, so I will probably need syntax help initially"], ['Charlotte Morton Tuesdays and Thursdays, afternoons/evenings', '\tI am attentive to detail and love helping others with their problems', '\tHow to think through/approach large coding projects'], ['Paguiyendou Sandrine Douti Monday/Tuesday Evenings', "\tI am a beginner in Python coding so I don't know much yet", '\tCoding']]
    result = analysis.study_partners(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    print('Study partners tests passed')

# ------------------------------------------------
# Part 4 Tests

def test_graduation_years():
    """
    Test cases for graduation years
    """
    # Note for these cases, the order of the dictionary keys doesn't matter!
    expected = {2026: 1, 2027: 1}
    result = analysis.graduation_years(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {2028: 5, 2027: 1, 2029: 1}
    result = analysis.graduation_years(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = {2029: 3, 2028: 4}
    result = analysis.graduation_years(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {2028: 1, 2029: 8}
    result = analysis.graduation_years(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {2029: 8, 2028: 7}
    result = analysis.graduation_years(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    print('Graduation years tests passed')

def test_birthday_buddies():
    """
    Test cases for birthday buddies
    """
    expected = {'1-Jan': ['anonymous anonymous', 'test student']}
    result = analysis.birthday_buddies(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {'7-May': ['test student', 'ABCD EFGH'], '10-Mar': ['anonymous anonymous', 'anonymous anonymous', 'anonymous anonymous']}
    result = analysis.birthday_buddies(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    # TODO: Add 2 or more new tests here
    expected = {'24-Jan': ['Victor Martinez', 'Joaquin Noguera']}
    result = analysis.birthday_buddies(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {}
    result = analysis.birthday_buddies(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {}
    result = analysis.birthday_buddies(DATA_5)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    print('Birthday buddies tests passed')

def test_all():
    test_first_name()
    test_introduction()
    test_cs_count()
    test_number_of_students()
    test_number_of_anonymous()
    test_number_of_ramen_recommends()
    test_first_last()
    test_tea_enjoyers()
    test_coffee_enjoyers()
    test_travelled_south()
    test_list_majors()
    test_cool_things()
    test_emojis()
    test_study_partners()
    test_graduation_years()
    test_birthday_buddies()
    print('Hooray, all tests passed!')

if __name__ == "__main__":
    test_all()