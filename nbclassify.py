import sys
import os
import pdb

problity_ham_file = 0
problity_spam_file = 0
directory_name_dir = ''
argument = sys.argv[1]
dictionary = {}
number_ham_file_name = 0
number_spam_file_name = 0
number_ham_file_predicted = 0
number_spam_file_predicted = 0




for entry in argument:
    directory_name_dir += entry

model_source_file = open("nbmodel.txt", "r", encoding="latin1")

data = model_source_file.read().splitlines()

for index, saved_data in enumerate(data):

    input = saved_data.split()
    if index > 2:
        dictionary[input[0]] = [float(input[1]), float(input[2])]

    elif index == 0:
        number_of_words = int(input[1])

    elif index == 1:
        give_problity_of_spam = float(input[1])

    elif index == 2:
        give_problity_of_ham = float(input[1])

model_source_file.close()
simbol1= "/"
simbol2 = "\\"
spam = "spam"
ham = "ham"
with open("nboutput.txt", "w", encoding="latin1") as output_file:
    for directory_name, dir_name, file_name in os.walk(directory_name_dir):

        if simbol1 in directory_name:
            dir = directory_name.split(simbol1)

        elif simbol2 in directory_name:
            dir = directory_name.split(simbol2)
        dir = dir[-1]


        for file in file_name:

            if file.endswith(".txt"):



                path_of_file = open(os.path.join(directory_name, file), "r", encoding="latin1")

                token_list = path_of_file.read().split()

                problity_ham_file = 0
                problity_spam_file = 0

                for each_token in token_list:
                    each_token.lower()

                    if each_token in dictionary.keys() :

                        problity_ham_file += dictionary[each_token][0]
                        problity_spam_file += dictionary[each_token][1]


                path_of_file.close()

                pr_ham_file = give_problity_of_ham + problity_ham_file

                pr_spam_file = give_problity_of_spam + problity_spam_file

                if pr_ham_file < pr_spam_file:
                    #pdb.set_trace()
                    string = spam+"\t" + str(os.path.join(directory_name, file))

                    output_file.write(string + "\n")

                elif pr_ham_file > pr_spam_file:
                    #pdb.set_trace()
                    string = ham+"\t" + str(os.path.join(directory_name, file))

                    output_file.write(string + "\n")

                else:
                    string = spam+"\t" + str(os.path.join(directory_name, file))

                    output_file.write(string + "\n")
    output_file.close()
#pdb.set_trace()
