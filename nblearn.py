import math
import sys
import os
import pdb

directory = ''

path = sys.argv[1]

for input in path:

    directory += input

dictionary_of_words = {}

problity_spam = 0

problity_ham = 0

total_number_of_word_in_ham = 0

total_number_of_word_in_spam = 0

number_of_ham_file = 0

number_of_spam_file = 0

simbol1= "/"
simbol2 = "\\"
spam = "spam"
ham = "ham"

for directory_name, dir_name, file_name in os.walk(directory):

    if simbol1 in directory_name:

        dir = directory_name.split(simbol1)

    elif simbol2 in directory_name:

        dir = directory_name.split(simbol2)

    dir = dir[-1]

    if dir.lower() == spam:

        for  each_file in file_name:

            number_of_spam_file = number_of_spam_file+ 1

            if  each_file.endswith(".txt"):

                input_file = open(os.path.join(directory_name,  each_file), "r", encoding="latin1")

                all_token = input_file.read().split()


                for each_token in all_token:
                    each_token.lower()
                    #if each_token == "/":


                    if each_token not in dictionary_of_words.keys():

                        dictionary_of_words[each_token] = [0, 1, 0, 0]

                        total_number_of_word_in_spam = total_number_of_word_in_spam + 1

                    else:

                        dictionary_of_words[each_token][1] = dictionary_of_words[each_token][1] +1


                        total_number_of_word_in_spam = total_number_of_word_in_spam + 1


                input_file.close()


    if dir.lower() == ham:

        for each_file in file_name:

            number_of_ham_file = number_of_ham_file + 1

            if each_file.endswith(".txt"):

                path_each_file = open(os.path.join(directory_name,  each_file), "r", encoding="latin1")

                all_token_inside_file = path_each_file.read().split()

                for each_token in all_token_inside_file:
                    each_token.lower()


                    if each_token not in dictionary_of_words.keys():

                        dictionary_of_words[each_token] = [1, 0, 0, 0]

                        total_number_of_word_in_ham = total_number_of_word_in_ham + 1

                    else:

                        dictionary_of_words[each_token][0] = dictionary_of_words[each_token][0] + 1

                        total_number_of_word_in_ham = total_number_of_word_in_ham + 1

                path_each_file.close()




smoothing = 1

total_number_file = 0

for word in dictionary_of_words:

    dictionary_of_words[word][2] = (dictionary_of_words[word][0] + smoothing ) / (total_number_of_word_in_ham + len(dictionary_of_words))

    if dictionary_of_words[word][2] > 0:

        dictionary_of_words[word][2] = math.log(dictionary_of_words[word][2])




for word in dictionary_of_words:

    dictionary_of_words[word][3] = (dictionary_of_words[word][1] + smoothing) / (total_number_of_word_in_spam + len(dictionary_of_words))

    if dictionary_of_words[word][3] > 0:

        dictionary_of_words[word][3] = math.log(dictionary_of_words[word][3])

total_number_file = number_of_spam_file + number_of_ham_file

if total_number_file > 0:

    problity_of_ham = math.log(number_of_ham_file / total_number_file)



if total_number_file > 0:

    problity_of_spam = math.log(number_of_spam_file / total_number_file)


output = open('nbmodel.txt', "w", encoding="latin1")

output.write("number_of_words"+"\t" + str(len(dictionary_of_words)) + "\n")

output.write(spam+"\t" + str(problity_of_spam) + "\n")

output.write(ham+"\t" + str(problity_of_ham) + "\n")

for word in dictionary_of_words:

    string = ''
    string += str(word)
    string +="\t"

    string += str(dictionary_of_words[word][2])
    string += "\t"

    string += str(dictionary_of_words[word][3])
    output.write(string + '\n')

output.close()
#pdb.set_trace()