'''
This code takes our text data file containing the preposition errors and corrections and creates CSV files
for the prepositions ("at, in, on, during, out").
'''

import re
import pandas as pd
from pandas.core.frame import DataFrame

#Define helper methods:
def add_list_info(list_to_add, list_to_copy, ):
    for index in range(5):
        list_to_add[index].append(list_to_copy[index])

#take token_value, go to that index - 1 in sentence list, get the n-gram 4 before and 4 indexes 
#after the preposition, return that n-gram.
def find_context(sentence, token):
    #reduce token by one to get it on the right index. Split sentence. 
    sentence = sentence.split()
    token = token - 1   
    start, end = token, token
    start -= 4
    if (start < 0):
        start = 0
    end += 5
    if(end >= len(sentence) ):
        end = len(sentence) - 1
    return sentence[start:end]
    
# def get_corrections_list():
#     with open("wiki_prep_corrections.CORRECTIONS","r") as full_corr_list:
#         line =  full_corr_list.readline()
#         while line:
#             split_line = line.split('\t')
#             for index in range(len(split_line)):
#             corrections_list[index].append(split_line[index])
#             lineCounter = lineCounter + 1
#             line =  full_corr_list.readline()
# df_full_corrections = pd.DataFrame(corrections_list,)
# df_full_corrections = df_full_corrections.transpose()
# df_full_corrections.columns = ['token_value', 'wrong_prep', 'W_POS_tag', 'right_prep', 'R_POS_Tag', 'wiki_ID', 'article_id_wrong', 'article_ID_right', 'edit_chain', 'clean?']
#We now have a full dataframe of the correction information we can manipulate.


#Declare necessary lists. Preps is currently unusued.
preps = ["at","in", "on","during","out"]
corrections_list = [ [], [], [], [], [], [], [], [], [], [] ]
sent_list = []

#Read wiki sentence files into a list. This is so we can iterate through all 2 million sentences 
#more quickly
with open("processed_sents.txt", "w") as output:
    with open("wiki_sents.txt","r") as full_sent_list:
        line =  full_sent_list.readline()

        while line:
            # line.replace('_[A-Z,.!?;:\']*', '')
            line = re.sub(r'_[A-Z,.!?;:\'\`]*', '', line)
            output.write(line)
            # sent_list.append(line)
            line =  full_sent_list.readline()

# print(sent_list)

print(len(sent_list))
#Write back into text file




