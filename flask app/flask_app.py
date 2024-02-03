
    
    
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from detoxify import Detoxify
from clean_comment import clean_comment
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import os

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["data_scraping"]
collection = db["scraping"]
model = Detoxify('original')



@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    try:
        # Check if a file was uploaded
        if 'file' not in request.files:
            return jsonify({"error": "No file part"})

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty part without filename
        if file.filename == '':
            return jsonify({"error": "No selected file"})

        # If the file is present and has a valid filename
        if file:
            # Save the file to a folder (change folder path as needed)
            file.save(os.path.join('uploads', file.filename))
            filepath = os.path.join('uploads', file.filename)

            data = pd.read_csv(filepath)
            results = []
            for comment in data['comment']:
                clean_comment_text = clean_comment(comment)
                result = model.predict(clean_comment_text)
                # Convert numpy.float32 to native Python float
                result = {key: float(value) if isinstance(value, np.float32) else value for key, value in result.items()}
                results.append({'comment': clean_comment_text, 'analysis': result})
            db.collection.insert_many(results)
            return jsonify({"message": "Comments processed and stored in MongoDB"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    os.makedirs('uploads', exist_ok=True)  # Create a folder to store uploaded files if it doesn't exist
    app.run(debug=True)
