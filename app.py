from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
from Preprocessing.text import Preprocessing
from Preprocessing.gensim_vectorizers import  FastText_vectorize


app = Flask(__name__)
model_path = "models/Tweet_Positive_Negative.h5"

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

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])

def predict():
    model = load_model(model_path)
    if request.method == 'POST':
        text = request.form['tweet']
        text = preprcs(text)
        text = vectorize(text)
        prediction = np.argmax(model.predict(text))
        print(prediction)
        # render_template('index.html',tweet_list = classes[prediction])
        return classes[prediction]

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=9696)