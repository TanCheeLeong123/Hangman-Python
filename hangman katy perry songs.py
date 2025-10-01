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

words = '''unconditionally last-friday-night california-gurls firework hot-n-cold dark-horse wide-awake teenage-dream harleys-in-hawaii this-is-how-we-do the-one-that-got-away i-kissed-a-girl never-really-over waking-up-in-vegas thinking-of-you bon-appetit swish-swish cozy-little-christmas part-of-me chained-to-the-rhythm mannequin ur-so-gay if-you-can-afford-me lost im-still-breathing fingerprints peacock circle-the-drain hummingbird-heartbeat et not-like-the-movies roar walking-on-air legendary-lovers this-moment love-me witness hey-hey-hey double-rainbow roulette ghost deja-vu power mind-maze miss-you-more pendulum tsunami into-me-you-see by-the-grace-of-god spiritual daisies smile cry-about-it-later teary-eyes resilient not-the-end-of-the-world what-makes-a-woman only-love electric rise when-im-gone three-six-five if-we-ever-meet-again starstrukk feels trust-in-me piercing search-me last-call growing-pains my-own-monster spit faith-wont-fail naturally when-theres-nothing-left box diamonds hook-up long-shot its-okay-to-believe simple takes-one-to-know-one wish-you-the-worst weigh-me-down one-of-the-boys self-inflicted who-am-i-living-for pearl birthday international-smile dressin-up it-takes-two choose-your-battles bigger-than-me dance-with-the-devil act-my-age save-as-draft champagne-problems tucked womans-world gimme-gimme gorgeous im-his-hes-mine crush lifetimes all-the-love nirvana artificial truth wonder i-woke-up has-a-heart no-tears-for-new-years ok black-and-gold breakout brick-by-brick broken bullet con-calma damn did-somebody-say electric-feel every-day-is-a-holiday girl-next-door hackensack head-over-heels immortal-flame in-between look-but-dont-touch method-to-my-madness milk-milk-lemonade nothing-like-the-first-time passenger playing-house psycho-love rise speed-dialin spend-the-night t-shirt thats-more-like-it the-better-half-of-me the-driveway times-up use-your-love waving-through-a-window whatever-you-say'''.split()

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


print('H A N G M A N   K A T Y   P E R R Y   S O N G S')
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

