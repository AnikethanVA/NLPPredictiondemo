from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import os
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"]="true"

model = load_model("nextword2.h5")
tokenizer = pickle.load(open('tokenizer1.pkl', 'rb'))
seq_len = 3

def Enter_Text(input):
    input_text = input.strip().lower()
    encoded_text = tokenizer.texts_to_sequences([input_text])[0]
    pad_encoded = pad_sequences([encoded_text], maxlen=seq_len, truncating='pre')
    y = (encoded_text, pad_encoded)
    x = []
    for i in (model.predict(pad_encoded)[0]).argsort()[-3:][::-1]:
        pred_word = tokenizer.index_word[i]
        temp = (pred_word)
        x.append(temp)

    return ", ".join(x)