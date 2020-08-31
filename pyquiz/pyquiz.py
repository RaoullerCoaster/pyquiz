def check(question, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if question.lower() == answer.lower():
            print('Correct answer!')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                raad = input('Wrong answer, try again!')
            attempt = attempt + 1

        if attempt == 3:
            print('Wrong answer, the right answer was: ' + answer)

score = 0

def score_reset():
    score = 0

def score_set(data):
    score = data

def end():
    print('This is the end of the quiz! Your score is: ' + str(score))

def mid():
    print('We are entering a new catagory! Your score is: ' + str(score))
