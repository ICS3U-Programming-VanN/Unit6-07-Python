#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: December 31, 2022
# This program asks the user for a string and
# then displays each word of the string on a new line


# This function takes a sentence as a string and returns a list of the words in the sentence
def string_parser(string_sentence):
    # Turns the string into a list of words
    list_of_words = string_sentence.split()

    # Returns the list of words
    return list_of_words


def main():
    # Displays what the program does
    print(
        "This program will take in a sentence as input and display each word separately on a new line, without spaces."
    )

    # Asks user for a string
    user_sentence = input("Enter a string: ")

    # Calls function to turn the string into a list of words
    user_words_list = string_parser(user_sentence)

    # Displays the words in the list
    print("\nThe words in your sentence: ")
    for word in user_words_list:
        print(word)


if __name__ == "__main__":
    main()
