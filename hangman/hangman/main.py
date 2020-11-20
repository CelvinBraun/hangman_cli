import random
import hangman_art as art
import hangman_words as words
end_of_game=0

#Random chose of word out of hangman_word.py
while end_of_game!="1":
    chosen_word = random.choice(words.word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    print(art.logo)

    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        #Input letter
        guess = input("Guess a letter: ").lower()
    
        if guess in display:
            print(f"You already used the letter: {guess}")

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            print(f"{guess} isn´t in the word!")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(art.stages[0])
                print("You lose.")
                end_of_game=int(input("'1' for another round, '2' for exit."))

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")
            end_of_game=int(input("'1' for another round, '2' for exit."))
        print(art.stages[lives])