import random
import hangman_words as mundos
import hangman_art as art
from replit import clear


chosen_word = random.choice(mundos.word_list).lower()
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(art.logo)
print(art.stages[6])

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Escolha uma letra: ").lower()
        
    clear()

    if guess in display:
        print(f"Voce ja escolheu a letra {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Voce digitou {guess}, e errou, voce perdeu uma vida")
        if lives == 0:
            end_of_game = True
            print("*PARABENS, VOCE PERDEU!!.*")
            print(f"A palavra certa era {chosen_word}")
            
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Impressionante para um macaco q nem vc.")

    print(art.stages[lives])