# Author: Paul Quaife
# Date: 2/23/2021
# Description: Takes a string and returns a dictionary that tabulates how many of each letter is in that string.


def count_letters(string):
    letter_dic = {}
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in string.upper():
        if c in alphabets:
            if c in letter_dic:
                letter_dic[c] += 1
            else:
                letter_dic[c] = 1
    return letter_dic
