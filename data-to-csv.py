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
with open("wiki_prep_sents.SENTS","r") as full_sent_list:
    line =  full_sent_list.readline()
    while line:
        sent_list.append(line)
        line =  full_sent_list.readline()


#Turn text file into lists: read text file; reading line by line of text files, split line by tabs;
#add the column contents to the appropriate lists; repeat.
at_list = [ [],[],[],[],[],[], []]
in_list = [ [],[],[],[],[],[], []]
on_list = [ [],[],[],[],[],[], []]
during_list = [ [],[],[],[],[],[], []]
out_list = [ [],[],[],[],[],[], []]

lineCounter = 0
with open("wiki_prep_corrections.CORRECTIONS","r") as full_corr_list:
    line =  full_corr_list.readline()
    while line:
        split_line = line.split('\t')
        #1 = preposition mistake column; 3 = preposition correction column. if either preposition 
        #is one of the five mentioned before, add it to it's list.
        if re.match(r"[aA]t", split_line[1]) or re.match(r"[aA]t", split_line[3]):
            add_list_info(at_list,split_line)
            at_list[5].append(find_context(sent_list[lineCounter], int(split_line[0])))
            at_list[6].append(sent_list[lineCounter])
            # #plus context.
        if re.match(r"[oO]n", split_line[1]) or re.match(r"[oO]n", split_line[3]):
            add_list_info(on_list,split_line)
            on_list[5].append(find_context(sent_list[lineCounter], int(split_line[0])))
            on_list[6].append(sent_list[lineCounter])
        if re.match(r"[iI]n", split_line[1]) or re.match(r"[iI]n", split_line[3]):
            add_list_info(in_list,split_line)
            in_list[5].append(find_context(sent_list[lineCounter], int(split_line[0])))
            in_list[6].append(sent_list[lineCounter])
        if re.match(r"[dD]uring", split_line[1]) or re.match(r"[dD]uring", split_line[3]):
            add_list_info(during_list,split_line)
            during_list[5].append(find_context(sent_list[lineCounter], int(split_line[0])))
            during_list[6].append(sent_list[lineCounter])
        if re.match(r"[oO]ut", split_line[1]) or re.match(r"[oO]ut", split_line[3]):
            add_list_info(out_list,split_line)
            out_list[5].append(find_context(sent_list[lineCounter], int(split_line[0])))
            out_list[6].append(sent_list[lineCounter])

        # corrections_list[index].append(split_line[index])
        lineCounter = lineCounter + 1
        line =  full_corr_list.readline()

#Transpose the dataframes so we have the columns on top.
df_at = pd.DataFrame(at_list).transpose()
df_in = pd.DataFrame(in_list).transpose()
df_on = pd.DataFrame(on_list).transpose()
df_during = pd.DataFrame(during_list).transpose()
df_out = pd.DataFrame(out_list).transpose()

#add column names.
df_list = [df_at, df_in, df_on, df_during, df_out]
for df in df_list :
    df.columns = ['token_value', 'wrong_prep', 'W_POS_tag', 'right_prep', 'R_POS_Tag','context', 'sentence']

#Write these to CSV files and done.
df_at.to_csv('at.csv')
df_in.to_csv('in.csv')
df_on.to_csv('on.csv')
df_during.to_csv('during.csv')
df_out.to_csv('out.csv')

