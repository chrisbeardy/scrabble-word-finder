#!/usr/bin/python3

import twl  # scrabble dictionary
import PySimpleGUI as sg  # UI


LETTER_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2,
                 "e": 1, "f": 4, "g": 2, "h": 4,
                 "i": 1, "j": 8, "k": 5, "l": 1,
                 "m": 3, "n": 1, "o": 1, "p": 3,
                 "q": 10, "r": 1, "s": 1, "t": 1,
                 "u": 1, "v": 4, "w": 4, "x": 8,
                 "y": 4, "z": 10}
starting_text = "X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0 \n X : 0"

# UI
layout = [
            [sg.Text('Enter Letters:', font=("Helvetica", 30))],
            [sg.InputText(default_text='Scrabble')],
            [sg.Text('Top Word Scores:', justification='center', font=("Helvetica", 30))],
            [sg.Multiline(starting_text, size=(40, 10), key='words', font=("Helvetica", 15))],
            [sg.Button('Close', size=(8, 4))]
          ]
window = sg.Window('Scrabble Word Finder', layout, size=(820, 480), resizable=True)


def check_valid_words(current_tile_letters, scrabble_words):
    temp_word_array = []

    for word in scrabble_words:
        for letter in word:
            if letter not in current_tile_letters:
                break
            elif word.count(letter) > current_tile_letters.count(letter):
                break
        else:
            temp_word_array.append(word)
            continue
    temp_word_array.sort()
    return temp_word_array


def get_top_scoring_words(valid_words):
    word_and_score = dict()

    for word in valid_words:
        score = 0
        for letter in word:
            score += LETTER_SCORES.get(letter)
        word_and_score[word] = score

    return dict(sorted(word_and_score.items(), key=lambda x: x[1], reverse=True)[:10])


def start_scrabble():
    scrabble_words = set(twl.iterator())  # scrabble dictionary

    while True:
        event, values = window.read(timeout=100)

        current_tile_letters = values[0]
        valid_words = check_valid_words(current_tile_letters, scrabble_words)
        top_word_scores = get_top_scoring_words(valid_words)

        window['words'].update("\n".join("{}: {}".format(k, v) for k, v in top_word_scores.items()))
        window.refresh()

        if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
            break

    window.close()


if __name__ == '__main__':
    start_scrabble()
