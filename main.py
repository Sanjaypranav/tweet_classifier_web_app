#argument parser
import argparse
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import sys
import time
import numpy as np
from tensorflow.keras.models import load_model
#for datetime module
from time import time
from Preprocessing.text import Preprocessing
from Preprocessing.gensim_vectorizers import  FastText_vectorize
#import the necessary packages

classes = {0: 'Positive',
           1: 'Negative',
           2: 'Neutral',
           }
def preprcs(text):
    #preprocess the text
    p =Preprocessing(lemmatize=True)
    text = p.text_normalize(text)
    text = p.text_tokenize(text)
    return text
def vectorize(tweet):
    vec = FastText_vectorize("fasttext/wiki-news-300d-1M.vec")
    vec._build_vector()
    tweet = vec._get_vector_list(tweet)
    tweet = tweet.reshape(1, tweet.shape[0], tweet.shape[1])
    tweet = vec.padding_truncate_lists(tweet, max_length=20)
    return tweet

def predict(text):
    model = load_model(model_path)
    if text_file is None:
        text = preprcs(text)
        text = vectorize(text)
        return classes[np.argmax(model.predict(text))]

    else:
        with open(text_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                text = preprcs(line)
                text = vectorize(text)
                return classes[np.argmax(model.predict(text))]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help = " Input folder containing the text file",default=None ,required = False)
    parser.add_argument('--model', help = " Path to the trained model", default= "models/Tweet_Positive_Negative.h5")
    parser.add_argument('--output', help = " Path to the output file",required = False)
    parser.add_argument('--text', help = " Provide text to save path ", default= "Hi im Sanjaypranav")
    args = parser.parse_args()
    text_file = args.path
    model_path= args.model
    output = args.output
    text = args.text
    print(predict(text = text))


