
"""
The program is trying to attempt to translate a sentence captured as users input
We first must read in the text file testese.txt.
Then from the texr file, we create a list of strings from each lines in the text file.
Then, we create the dictionary from the list
Once the text file has been read into memory, we cloes the file.


We then define a function for translating which envolves splitting the user input (sentence) into an
array of strings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

once we have the array of strings representing the user's input sentence, we
loop through each words, find the key matching word and returns back the value tied to the word
in our dictionary.


after each word is translated, we then
print out the translated sentence to the user.

"""

