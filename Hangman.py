import random

words  = ["Apple", "Ball", "Cat", "Double", "Elephant", "Ferrarie"]

random_word = random.choice(words).upper()
random_word_letters_list = list(random_word)
length_of_word = len(random_word)

print(random_word)
print(random_word_letters_list)

display = []
for _ in range(length_of_word):
    display.append("_")
print(display)

count = 0
while count < length_of_word:
    guessed_letter = input("Guess the letter: ").upper()
    print(guessed_letter)
    if guessed_letter in random_word_letters_list:
        index = random_word_letters_list.index(guessed_letter)
        print(index)
        display[index] = guessed_letter
        random_word_letters_list[index] = " "
        print(display)
    count += 1

if "_" not in display:
    print("you Win!")
else:
    print("Game Over!!")
