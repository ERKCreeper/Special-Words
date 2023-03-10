#You will need to delete an extra line at the end of the output txt file.
allWords = open("word_list.txt", "r").readlines() #Open the main word file as a string. This also splits each line into a seperate item in a list. You will need to download this from the Github repository and put it in the same folder as the python file.
outputFile = open("Z-A Sorted.txt", "w") #You will need to make this file under the same folder the python script is under.

allWords.sort(reverse = True) #Sorts all of the words in reverse.

outputFile.writelines(allWords) #Writes each item in the list of words on an seperate line.
outputFile.close() #Close output file to save changes.
