import string
import re
from detoxify import Detoxify
import pandas as pd

from nltk.corpus import stopwords
import os
def clean_comment(comment):
    comment = comment.lower()
    comment = comment.translate(str.maketrans("", "", string.punctuation))
    comment = re.sub(r'\d+', '', comment)
    comment = re.sub(r'[^a-zA-Z\s]', '', comment)
    comment = re.sub(r'\s+', ' ', comment).strip()
    stop_words = set(stopwords.words('french'))
    comment = ' '.join([word for word in comment.split() if word not in stop_words])
    return comment