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

words = '''intro-two-cool-four-skool we-are-bulletproof-pt-two skit-circle-room-talk no-more-dream interlude like outro-circle-room-cypher skit: on the start line path intro-o-rul-eight-two no we-on skit-r-u-happy-now if-i-ruled-the-world coffee cypher-pt-1 attack-on-bangtan satoori-rap outro-luv-in-skool miss-right i-like-it intro-skool-luv-affair boy-in-luv skit-soulmate where-did-you-come-from just-one-day tomorrow cypher-pt-two-triptych spine-breaker jump outro-propose intro-what-am-i-to-you danger war-of-hormone hip-hop-phile let-me-know rain cypher-pt-three-killer interlude-what-are-you-doing-now can-you-turn-off-your-cellphone embarrased twenty-four-seven-heaven look-here so-four-more outro-does-that-make-sense intro-blooming-youth i-need-u hold-me-tight skit-expectation dope fun-boys converse-high moving-on outro-love-is-not-over for-you intro-never-mind run butterfly whalien-fifty-two ma-city silver-spoon skit-one-night-in-a-strange-city autumn-leaves outro-house-of-cards intro-the-most-beautiful-moment-in-life save-me epilogue-young-forever intro-boy-meets-evil blood-sweat-and-tears begin lie stigma first-love reflection mama awake lost cypher-pt-four am-i-wrong twenty-first-century-girls two-three interlude-wings spring-day not-today a-supplementary-story-you-never-walk-alone intro-serendipity dna best-of-me dimple pied-piper mic-drop go-go outro-her skit-hesitation-and-fear sea intro-ringwanderung dont-leave-me crystal-snow let-go outro-crack intro-singularity fake-love the-truth-untold one-hundred-thirty-four-thousand-three-hundred-forty paradise love-maze magic-shop airplane-pt-two anpanman so-what outro-tear euphoria trivia-just-dance serendipity singularity the-truth-untold trivia-seesaw epiphany im-fine idol answer-love-myself intro-persona boy-with-luv mikrokosmos make-it-right home jamais-vu dionysus heartbeat dream-glow a-brand-new-day all-night captain cake-waltz shine not-alone friends wish flying lalala you-are-here lights interlude-shadow black-swan filter my-time louder-than-bombs on ugh zero-zero-zero-zero inner-child friends moon respect we-are-bulletproof-the-eternal outro-ego stay-gold dynamite life-goes-on fly-to-my-room blue-and-grey skit telepathy dis-ease stay butter permission-to-dance my-universe born-singer yet-to-come run-bts bad-decisions the-planet take-two'''.split()

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
