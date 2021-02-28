import pandas as pd
import re
import string
import datetime

def get_details(comment):
    try:
        comment_id = comment.id
        parent_id = comment.parent_id
        submission_id = comment.link_id
        comm_author = comment.author
        comm_body = comment.body
        vote_score = comment.score
        time = convert_date_time(comment.created_utc)

        return [comment_id, parent_id, submission_id, comm_author, comm_body, time, vote_score]
    except:
        return

def convert_date_time(unix_time):
	return str(datetime.datetime.fromtimestamp(unix_time))

def clean_submissions(func_df):
    #merge title and submission text
    func_df['full_text'] = func_df.title + ' ' + func_df.self_text

    #set media to video if the submission is tagged as video
    func_df.loc[(func_df['video'] == True), 'media'] = 'video'

    #set media to image if the url ends with jpg or png
    mask = (func_df['url'].str.slice(start=-3) == 'jpg') | (func_df['url'].str.slice(start=-3) == 'png')
    func_df.loc[mask, 'media'] = 'image'
    func_df.loc[(func_df['thumbnail'] == 'self'), 'media'] = 'none'

    #drop unneeded columns
    func_df.drop(columns=['title', 'self_text', 'video', 'thumbnail'], inplace=True)

    #remove duplicates
    func_df.sort_values(['full_text'], inplace=True, ascending=False)
    func_df.drop_duplicates(subset=['full_text'], inplace=True)

    #cast time to datetime and sort in order of post datetime
    func_df['time'] = pd.to_datetime(func_df['time'])
    func_df = func_df.sort_values(by='time')

    #filter out NAs
    func_df = func_df[func_df.full_text.notnull()]
    return func_df

def clean_praw_input(func_df):
    #rename columns
    func_df.rename(columns={'selftext': 'self_text', 'is_video': 'video'}, inplace=True)
    #convert time from utc to date_time
    func_df['time'] = func_df.created.map(lambda x: convert_date_time(x))
    func_df.drop(columns='created_utc', inplace=True)

    mask = (func_df.self_text == '[removed]') | (func_df.self_text == '[deleted]')
    func_df = func_df[~mask]
    return func_df

def text_processing(func_df):
    #remove http/https links
    links = lambda x: re.sub(r'^https?:\/\/.*[\r\n]*', ' ', x, flags=re.MULTILINE)
    #embedded links
    links2 = lambda x: re.sub(r'`&.*link rel=.*”.*;', ' ', x, flags=re.MULTILINE)
    #&amp*
    amps = lambda x: re.sub(r'&amp;.*;', ' ', x, flags=re.MULTILINE)
    #remove links in () or []
    links3 = lambda x: re.sub(r'[\(\[]https?:\/\/.*[\)\]]', ' ', x, flags=re.MULTILINE)

    #remove slashes
    slashes = lambda x: re.sub(r'\/', ' ', x, flags=re.MULTILINE)

    alphanumeric = lambda x: re.sub('\w*\d\w*', ' ', x)
    punc_lower = lambda x: re.sub('[%s]' % re.escape(string.punctuation), '', x.lower())
    new_line = lambda x: x.replace('\n', ' ')
    emojis = lambda x: x.encode('ascii', 'ignore').decode('ascii')

    func_df['full_text'] = func_df.full_text.map(links).map(links2).map(amps).map(links3).map(slashes)
    func_df['full_text'] = func_df.full_text.map(alphanumeric).map(punc_lower).map(new_line).map(emojis)
    return

def de_dup(func_df):
    func_df.sort_values(['full_text'], inplace=True, ascending=False)
    func_df.drop_duplicates(subset=['full_text'], inplace=True)

    func_df.sort_values(by='time', inplace=True)
    return

#lemmatization code from here:
#https://gaurav5430.medium.com/using-nltk-for-lemmatizing-sentences-c1bfff963258
import nltk
from nltk.corpus import wordnet
lemma=nltk.stem.WordNetLemmatizer()

# function to convert nltk tag to wordnet tag
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def lemmatize_sentence(sentence):
    global lemma
    #tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    #tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            #if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            #else use the tag to lemmatize the token
            lemmatized_sentence.append(lemma.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)

import spacy
nlp = spacy.load('en_core_web_sm')

def lemmatize_spacy(sentence):
    global nlp
    doc = nlp(sentence)
    return ' '.join([token.lemma_ for token in doc])
