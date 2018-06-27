def Scoresgrades(grade):

    print "Scores and Grades"

    if grade >=60 and grade<=69:
        print "score: {}; Your grade is D".format(grade)
    elif grade >=70 and grade<=79:
        print "score: {}; Your grade is C".format(grade)
    elif grade >=80 and grade<=89:
        print "score: {}; Your grade is B".format(grade)
    elif grade >=90 and grade<=100:
        print "score: {}; Your grade is A".format(grade)

import random
grade = random.randint(60, 100)
Scoresgrades(grade)