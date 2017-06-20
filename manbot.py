# IPND Stage 3 Final Project
# This is the hard question presented to the user to fill in the blanks.
avengers_hard = '''My favorite Marvel Avengers team members are __1__, __2__,
__3___, and __4__. I grew up playing with their action figures as a kid. Possible
choices include Hulk, Ironman, Thor or Captain America.'''
# These are the answer choices to fill in the blanks.
answers_hard = ['Hulk', 'Thor', 'Captain America', 'Ironman']
# This is the harder question presented to the user to fill in the blanks.
gijoe_harder = '''My favorite G.I.Joe action figures when I was a kid were
__1__ because he was awesome, __2__ because he was the enemy of my first choice,
__3__ because he was super strong, and __4__ bcause she was the only lady ninja. Possible choices are StormShadow, SnakeEyes, Jynx, or RoadBlock.'''
# These are the answers to the gijoe_harder question
answers_harder = ['SnakeEyes', 'StormShadow', 'RoadBlock', 'Jynx']
# This is the hardest question presented to the user to fill in the blanks.
hardest_one = '''Today, I have kept safely __1__ G.I.JOES's, __2__ Avengers,
__3__ G.I.JOE vehicles, and __4__ G.I.JOE planes. Possible choices are 0,
3, 2, or 153.'''
# These are the answers to the gijoe_hardest question
answers_hardest = ['153', '0', '3', '2']
# place savers as blanks below
blanks = ['__1__', '__2__', '__3__', '__4__']
# This marks the begining of the quiz with a greeting to the user.
print "Hello, this is a fun quiz to learn a little about me. I hope you enjoy it! Below this is a set of game level choices."
def level():
    '''
    Level function = input is the level desired by the user.
    The output is their chosen level.
    Args:
        level_choice: the choices to pick
        level_chosen: allows user to type in their selection
    Behavior:
        it displays to the user what to do and what the levels are while
        indenting the next line properly.
    '''
    level_choice = ['hard', 'harder', 'hardest']
    #this specify the user what choices are available.
    print level_choice
    level_chosen = raw_input('Select game level by typing it in.')
    phrase = ''
        # I declared the variable phrase here with an empty string so that it
        # will notify that the value phrase will be assigned with a string value
    answers = []
        # I declared answers with an empty list because later you'll
        # re-assign answers with a list variable.
    print "Great, you have chosen " + level_chosen + "." + '\n'
        # lets the user know what they have chosen and indents the line.
    if level_chosen == 'hard':
        phrase = avengers_hard
        answers = answers_hard
        # if they choose hard, then show the hard phrase
        return phrase, answers, level_chosen
    elif level_chosen == 'harder':
        phrase = gijoe_harder
        answers = answers_harder
        # if they choose harder, then show the hard phrase
        return phrase, answers, level_chosen
    elif level_chosen == 'hardest':
        phrase = hardest_one
        answers = answers_hardest
        # if they choose hardest, then show the hard phrase
        return phrase, answers, level_chosen
    else:
        # if they did not choose a said selection, this will remind them to.
        print "Something happened unexpected. I'm sorry, that option is not a choice"
        level()
        # calling the defined function so user can input again.
#print level() #used for testing

def word_in_pos(guess, answers, n):
    '''
    word_in_pos is looking at a blank. Users guess is input, the list of
    answers and then a number to understand which answer in that list should be
    the guess of the user.
    '''
    if guess == answers[n]:
        # taking the guess of user and checking if in the answers.
        return guess
    else:
        return None
#Playgame function defining local variables
def replacementFunction(phrase, current_blank, guess):
    phrase = phrase.split()
    replaced = []
    for word in phrase:#looping through phrase
        if current_blank in word:
            word = word.replace(current_blank, guess)
            replaced.append(word)
        else:
            replaced.append(word)
    phrase = " ".join(replaced)
    return phrase

def play_game():
    phrase, answers, level_chosen = level()
    replaced = []
    blanks = ['__1__', '__2__', '__3__', '__4__']
    index = 0#takes the current position
    forward_index = 1#references moving forwrad a position. Redundent I've been
    #told
    # blanks_total = 4#states the amount of blanks there are.
    while index < len(blanks):#while the current position is less than the total
        current_blank = blanks[index]#blanks left, to print the phrase.
        print "Your present phrase is this:" + "\n"
        print phrase + "\n"#some indentation
        guess = raw_input("So what should you put here" + current_blank + "?")
        if word_in_pos(guess, answers, index):#checks users input from the list.
            print "Awesome, Great job!" + "\n"
            phrase = replacementFunction(phrase, current_blank, guess)
            index += forward_index#moves forward a blank or position
            if index == len(blanks):# shows the user they have completed the quiz.
                print "You have completed the quiz. Great work!"
        else:#is this over too far?
              print "Sorry, that is not correct."#tells the user they have not quessed right.


play_game()