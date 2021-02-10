from sklearn.svm import LinearSVC
import joblib
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords, wordnet
import string
import contractions
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Replace all days of week by string "dayofweek"
weekstring =['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday']

# Replace all month names by string "month"
months = ['january','february', 'march','april','may','june','july','august', 'september', 'october','november','december']

# Replace all month names by string "month"
nums=['one','two','three','four','five','six','seven','eight','nine','ten']

# Replace all family relations with string "famrel"
famrel=['dad','mum','daughter','son','aunt','uncle','husband','wife', 'brother','sister', 'father','mother']

# Replace all friendship (non-family) relations with string "friend"
friendrel=['boyfriend','girlfriend','colleague']

def remove_punctuations(text):
    punc = string.punctuation 
    for punctuation in punc:
        text = text.replace(punctuation, '')
    return text

def replace_string(text,remove_arr, replace_str):
    for rem in remove_arr:
        text = text.replace(rem, replace_str)
    return text

def remove_stopwords(text, filename):
    stop_words=[]
    with open(filename,'r') as f:
        for line in f:
            for word in line.split():
                stop_words.append(word.lower()) 
    result =  [word for word in text if word not in stop_words]
    return result

def remove_contractions(text):
  return " ".join([contractions.fix(word) for word in text.split()])

def replace_strings(text, new_string , remove_arr ):
    for r in remove_arr:
        text = text.replace(r, new_string)
    return text

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def Lemmatize(text):
    #Make Lower Case
    text=text.lower()

    #Remove Word contractions
    text = remove_contractions(text)

    #Remove Punctuation
    text = remove_punctuations(text)

    print(text)
    #Replace Strings

    #Replace all days of week by string "dayofweek"
    weekstring =['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday']
    text = replace_strings(text,'dayofweek', weekstring)

    #Replace all month names by string "month"
    months = ['january','february', 'march','april','may','june','july','august', 'september', 'october','november','december']
    text = replace_strings(text,'month', months)

    #Replace all Numbers by String 'number'
    nums=['one','two','three','four','five','six','seven','eight','nine','ten']
    text = replace_strings(text, 'number',nums)

    #Replace all family relations with string "famrel"
    famrel=['dad','mum','daughter','son','aunt','uncle','husband','wife', 'brother','sister', 'father','mother']
    text = replace_strings(text, 'famrel',famrel)
    
    #Replace all friendship (non-family) relations with string "friend"
    friendrel=['boyfriend','girlfriend','colleague'] 
    text = replace_strings(text, 'friend',friendrel)

    #Tokenize
    tokens= word_tokenize(text)

    #Remove StopWords
    tokens = remove_stopwords(tokens, 'stopwords.txt')
    #print(tokens)

    #Tagging Parts of Speech in the tokenized 
    pos = nltk.tag.pos_tag(tokens)
    #print(pos)

    #Tag Wordnet position
    wn_pos = [(word, get_wordnet_pos(pos_tag)) for (word, pos_tag) in pos]

    #Get Lemmatized String
    wnl = WordNetLemmatizer()
    lemmatized=" ".join([wnl.lemmatize(word, tag) for word, tag in wn_pos])

    return lemmatized

def Vectorize(text, vectorizer):
    #n-gram Tokenization
    print(text)
    vectorized =  vectorizer.transform([text])
    print(vectorized)
    return vectorized