# 1. Write a function that takes a phrase and a text file as inputs. The function returns True if the phrase is found
# in the document and returns False otherwise. Note: Newline characters will not be included in the phrase.

def searchfor(phrase):
    file = open("random.txt","r")
    text = file.readlines()

    for line in text:
        if phrase in line:
            return True

    return False

phrase = input(str('enter the phrase to be searched: '))
print (searchfor(phrase))

