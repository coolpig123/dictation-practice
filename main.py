import collections
import time
import os


def print_grade(correct_answers,number_of_items):
    grade = ((correct_answers / number_of_items) * 100)
    print("grade = "+str(grade)+"%")


# a function the make a test from hebrew to english
def test_from_heb_to_eng(dictionary):
    correct_answers = 0
    user_input = ""
    for key, value in dictionary.items():
        user_input = input(value[::-1]+"\n")
        if key == user_input:
            correct_answers += 1
            print("correct\n")
            input("press enter to continue...")
        else:
            print("false\n correct answer is "+key)
            input("press enter to continue...")
        os.system("cls")
    print_grade(correct_answers,len(dictionary))


# a function the make a test from english to hebrew
def test_from_eng_to_heb(dictionary):
    correct_answers = 0
    user_input = ""
    for key, value in dictionary.items():
        user_input = input(key+"\n")
        if value == user_input:
            correct_answers += 1
            print("correct \n")
            input("press enter to continue...")
        else:
            print("false \n answer is "+ value[::-1])
            input("press enter to continue...")
        os.system('cls')
    print_grade(correct_answers,len(dictionary))


words_2 = {'will':'רצון',
           'input':'תשומה',
           'respond':'תגובה',
           'particulary':'במיוחד',
           'crisis':'משבר',
           'expectations':'ציפיות',
           'percent':'אחוז',
           'approach':'לגשת',
           'incident':'תקרית',
           'in contrast':'בניגוד ל',
           'variety':'מבחר',
           'background':'רקע',
           'phenomenon':'תופעה',
           'wicked':'מרושע',
           'policy':'מדיניות',
           'objective':'אוביקטיבי',
           'subjective':'סוביקטיבי',
           'to back up':'לגבות',
           'media':'תקשורת',
           'obvious':'ברור'}

while True:
    print(" a - test from english to hebrew \n b - test from hebrew to english \n c - quit the program")
    user_input = input()
    while user_input != 'a' and user_input != 'b' and user_input != 'c':
        user_input = input()
    
    if user_input == 'a':
        os.system('cls')
        test_from_eng_to_heb(words_2)
    elif user_input == 'b':
        os.system('cls')
        test_from_heb_to_eng(words_2)
    else:
        break