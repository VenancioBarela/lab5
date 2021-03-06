
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

"""
main():
set sentence = input()
set dictionary = create dictionary()
translate(sentence, dictionary)

translate(sentence, dictionary):
words = for each word in the sentence
for each words, translate the word
print translated sentence to user

create dictionary():
read in textese.txt
create list = each line from file
close the file
create a dict off of the list
return dict

main()
"""
#This method kickstarts  the app
# it creates a dictionary and fires off the translate method
def main():
    sentence = input("Enter a sentence:")
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

# this method create a dictionary based off of a text file given in the parameter
def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])

# This method translate the user input based off of the dictionary
def translate(sentence, dictionary):
    words = sentence.split() 
    for word in words:
        print(dictionary.get(word, word), " ", end="")


main()

