#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# Predefined list of 5 words
word_list = ['apple', 'banana', 'cherry', 'grape', 'lemon']

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Initialize game state
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Create a display version of the word with underscores
display_word = ['_' for _ in secret_word]

print("🎯 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 chances to make a mistake.\n")

# Game loop
while wrong_guesses < max_wrong_guesses and '_' in display_word:
    print("Word: ", ' '.join(display_word))
    print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter. Try a new one.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!\n")
        wrong_guesses += 1

# Game end
if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)


# In[ ]:




