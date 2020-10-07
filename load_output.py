import numpy as np
from collections import Counter
import argparse
import sys, os
# from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score

np.set_printoptions(threshold=np.inf)


def score(key, prediction, verbose=True, NO_RELATION=0):
    correct_by_relation = Counter()
    guessed_by_relation = Counter()
    gold_by_relation = Counter()

    # Loop over the data to compute a score
    for row in range(len(key)):
        gold = key[row]
        guess = prediction[row]

        if gold == NO_RELATION and guess == NO_RELATION:
            pass
        elif gold == NO_RELATION and guess != NO_RELATION:
            guessed_by_relation[guess] += 1
        elif gold != NO_RELATION and guess == NO_RELATION:
            gold_by_relation[gold] += 1
        elif gold != NO_RELATION and guess != NO_RELATION:
            guessed_by_relation[guess] += 1
            gold_by_relation[gold] += 1
            if gold == guess:
                correct_by_relation[guess] += 1

    # Print verbose information
    # if verbose:
    #     print("Per-relation statistics:")
    #     relations = gold_by_relation.keys()
    #     longest_relation = 0
    #     for relation in sorted(relations):
    #         longest_relation = max(relation, longest_relation)
    #     for relation in sorted(relations):
    #         # (compute the score)
    #         correct = correct_by_relation[relation]
    #         guessed = guessed_by_relation[relation]
    #         gold = gold_by_relation[relation]
    #         prec = 1.0
    #         if guessed > 0:
    #             prec = float(correct) / float(guessed)
    #         recall = 0.0
    #         if gold > 0:
    #             recall = float(correct) / float(gold)
    #         f1 = 0.0
    #         if prec + recall > 0:
    #             f1 = 2.0 * prec * recall / (prec + recall)
    #         # (print the score)
    #         sys.stdout.write(("{:<" + str(longest_relation) + "}").format(relation))
    #         sys.stdout.write("  P: ")
    #         if prec < 0.1:
    #             sys.stdout.write(' ')
    #         if prec < 1.0:
    #             sys.stdout.write(' ')
    #         sys.stdout.write("{:.2%}".format(prec))
    #         sys.stdout.write("  R: ")
    #         if recall < 0.1:
    #             sys.stdout.write(' ')
    #         if recall < 1.0:
    #             sys.stdout.write(' ')
    #         sys.stdout.write("{:.2%}".format(recall))
    #         sys.stdout.write("  F1: ")
    #         if f1 < 0.1:
    #             sys.stdout.write(' ')
    #         if f1 < 1.0:
    #             sys.stdout.write(' ')
    #         sys.stdout.write("{:.2%}".format(f1))
    #         sys.stdout.write("  #: %d" % gold)
    #         sys.stdout.write("\n")
    #     print("")

    # Print the aggregate score
    if verbose:
        print("Final Score:")
    prec_micro = 1.0
    if sum(guessed_by_relation.values()) > 0:
        prec_micro = float(sum(correct_by_relation.values())) / float(
            sum(guessed_by_relation.values()))
    recall_micro = 0.0
    if sum(gold_by_relation.values()) > 0:
        recall_micro = float(sum(correct_by_relation.values())) / float(
            sum(gold_by_relation.values()))
    f1_micro = 0.0
    if prec_micro + recall_micro > 0.0:
        f1_micro = 2.0 * prec_micro * recall_micro / (prec_micro + recall_micro)
    print("SET NO_RELATION ID: ", NO_RELATION)
    print("Precision (micro): {:.3%}".format(prec_micro))
    print("   Recall (micro): {:.3%}".format(recall_micro))
    print("       F1 (micro): {:.3%}".format(f1_micro))
    return prec_micro, recall_micro, f1_micro



for cnt in range(3):
    prediction = np.load("prediction{}".format(cnt)+".npy")
    label = np.load("label{}".format(cnt)+".npy")
    # nonzero_prediction = np.load("nonzero_prediction"+"0"*cnt+".npy")
    # nonzero_label = np.load("nonzero_label"+"0"*cnt+".npy")
    # print("prediction",prediction[25:50])
    # print("label",label[25:50])

    score(list(label), list(prediction))
    # print("nonzero_prediction",nonzero_prediction[:20])
    # print("nonzero_label",nonzero_label[:20])

    # print("accuracy: ",accuracy_score(nonzero_label, nonzero_prediction))
    # print("precision: ", precision_score(nonzero_label,nonzero_prediction,average='micro'))
    # print("recall: ", recall_score(nonzero_label,nonzero_prediction,average='micro'))
    # print("f1: ", f1_score(list(nonzero_label), nonzero_prediction,average='micro'))
    print("---------------------")


