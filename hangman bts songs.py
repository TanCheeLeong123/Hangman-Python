import random

HANGMAN_PICS = [r'''
  +---+
      |
      |
      |
     ===''', r'''
  +---+
  O   |
      |
      |
     ===''', r'''
  +---+
  O   |
  |   |
      |
     ===''', r'''
  +---+
  O   |
 /|   |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
 /    |
     ===''', r'''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = '''intro-two-cool-four-Skool we-are-Bulletproof-pt-two skit-circle-room-talk No-More-Dream Interlude Like Outro-Circle-Room-Cypher Skit: On the Start Line path Intro-o-Rul-eight-two no we-on skit-r-u-happy-now if-i-ruled-the-world coffee cypher-pt-1 attack-on-bangtan satoori-rap Outro-luv-in-skool Miss-Right I-Like-It Intro-Skool-Luv-Affair Boy-In-Luv Skit-Soulmate Where-Did-You-Come-From Just-One-Day Tomorrow Cypher-Pt-two-Triptych Spine-Breaker Jump Outro-Propose Intro-What-Am-I-To-You Danger War-of-Hormone Hip-Hop-Phile Let-Me-Know Rain Cypher-Pt-three-KILLER Interlude-What-Are-You-Doing-Now Can-You-Turn-Off-Your-Cellphone Embarrased twenty-four-seven-Heaven Look-Here So-four-More Outro-Does-That-Make-Sense intro-Blooming-Youth I-NEED-U Hold-Me-Tight Skit-Expectation DOPE fun-boys Converse-High Moving-On Outro-Love-is-Not-Over for-you Intro-Never-Mind RUN Butterfly Whalien-fifty-two Ma-City Silver-Spoon Skit-One-Night-In-A-Strange-City Autumn-Leaves Outro-House-of-Cards intro-the-most-beautiful-moment-in-life save-me epilogue-young-forever Intro-Boy-Meets-Evil Blood-Sweat-and-Tears Begin Lie Stigma First-Love Reflection MAMA Awake Lost Cypher-pt-four Am-i-Wrong twenty-first-Century-Girls two-three Interlude-Wings spring-day not-today a-supplementary-story-you-never-walk-alone Intro-Serendipity DNA Best-of-Me Dimple Pied-Piper MIC-Drop Go-Go Outro-Her Skit-Hesitation-and-Fear Sea intro-ringwanderung dont-leave-me crystal-snow let-go outro-crack intro-singularity fake-love the-truth-untold one-hundred-thirty-four-thousand-three-hundred-forty paradise love-maze magic-shop airplane-pt-two Anpanman so-what outro-tear euphoria trivia-just-dance serendipity singularity the-truth-untold trivia-seesaw epiphany im-fine idol answer-love-myself Intro-Persona Boy-With-Luv Mikrokosmos Make-It-Right HOME Jamais-Vu Dionysus heartbeat dream-glow a-brand-new-day all-night captain cake-waltz shine not-alone friends wish flying lalala you-are-here lights interlude-shadow black-swan filter my-time louder-than-bombs on ugh zero-zero-zero-zero inner-child friends moon respect we-are-bulletproof-the-eternal outro-ego stay-gold dynamite life-goes-on fly-to-my-room blue-and-grey skit telepathy dis-ease stay butter permission-to-dance my-universe born-singer yet-to-come run-bts bad-decisions the-planet take-two'''.split()
def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter or -.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter or -.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz-':
            print('Please enter a LETTER or -.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N   B T S   S O N G S')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Yes! The secret word is "{secretWord}"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(f'You have run out of guesses!\nAfter {len(missedLetters)} missed guesses and {len(correctLetters)} correct guesses, the word was "{secretWord}"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
