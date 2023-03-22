import random

def open_letter(letter):
    if letter not in correct_letters:
        correct_letters.add(letter)

def check_letter(letter):
    if letter not in correct_letters and letter not in wrong_letters:
        if letter in word:
            open_letter(letter)
        else:
            make_mistake(letter)

def make_mistake(letter):
    hearts -= 1
    wrong_letters.add(letter)

def win():
    pass

def lose():
    pass

if __name__ == "__main__":
    words = ['апельсин', "яблоко", "учебник", "кинескоп"]
    correct_letters = set()
    wrong_letters = set()
    hearts = 11
    word = random.choice(words).lower()
    while hearts > 0:
        user_letter = input("Введите букву")
        letter = user_letter.lower()
        check_letter(letter)

        if correct_letters == set(word):
            win()
    else:
        lose()