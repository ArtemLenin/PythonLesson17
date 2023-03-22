import random
import os

def clear_screen():
    os.system('cls')

def show_word():
    for letter in word:
        print(letter if letter in correct_letters else '_', end="")
    print()

def show_gallow():
    with open(f'gallow_text/gallow_{max_hearts - hearts}.txt', encoding='utf-8') as file:
        text = file.read()
    print(text)

def show_wrong_letters():
    print("Использованные буквы: ", end=" ")
    for letter in wrong_letters:
        print(letter, end=" ")
    print()

def show_user_interface():
    show_gallow()
    show_word()
    show_wrong_letters()


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
    global hearts
    hearts -= 1
    wrong_letters.add(letter)

def win():
    clear_screen()
    show_user_interface()
    print("Win")

def lose():
    clear_screen()
    show_user_interface()
    print("Lose!")

if __name__ == "__main__":
    words = ['апельсин', "яблоко", "учебник", "кинескоп"]
    correct_letters = set()
    wrong_letters = set()
    max_hearts = 11
    hearts = max_hearts
    word = random.choice(words).lower()
    while hearts > 0:
        clear_screen()
        show_user_interface()
        user_letter = input("Введите букву: ")
        letter = user_letter.lower()
        check_letter(letter)

        if correct_letters == set(word):
            win()
            break
    else:
        lose()