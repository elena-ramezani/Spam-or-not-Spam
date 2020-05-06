import sys
import os
import pdb
#from sklearn.metrics import precision_recall_fscore_support
true_positive = 0
false_negative = 0
false_positive = 0
true_negative = 0




model_source_file = open("nboutput.txt", "r", encoding="latin1")
data = model_source_file.read().splitlines()
y_pre = []
y_act = []
for saved_data in data:


    if saved_data[0] =="s":
        y_pre.append(1)

        if saved_data.lower().find("spam.txt") != -1:
            true_positive += 1
            y_act.append(1)
        elif saved_data.lower().find("ham.txt") != -1:
            false_positive += 1
            y_act.append(0)

    if saved_data[0] =="h":
        y_pre.append(0)
        if saved_data.lower().find("ham.txt") != -1:
            true_negative += 1
            y_act.append(0)
        elif saved_data.lower().find("spam.txt") != -1:
            false_negative +=1
            y_act.append(1)


#average_precision = precision_recall_fscore_support(y_act, y_pre)
#pdb.set_trace()


model_source_file.close()




spam_precision = true_positive/(true_positive + false_positive)
spam_recal = true_positive / (true_positive + false_negative)
f1_score_spam = 2 * ((spam_precision * spam_recal)/(spam_precision + spam_recal))

ham_precision = true_negative/(true_negative + false_negative)
ham_recal = true_negative / (true_negative + false_positive)
f1_score_ham = 2 * ((ham_precision * ham_recal) / (ham_precision + ham_recal))



print("ham precision:",ham_precision,"spam precision:",spam_precision)
print("ham ham_recal:",ham_recal,"spam_recal:",spam_recal)
print("f1_ham:",f1_score_ham)
print("f1_spam:",f1_score_spam)
