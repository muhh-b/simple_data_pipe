# simple_data_pipe
![Test](https://github.com/muhh-b/simple_data_pipe/assets/69880179/b99c0259-f344-438f-ae74-ac8bb41c38d6)

## Description

This project is about scraping comments related to a given hashtag, in our case, `harcèlement`, from Facebook. The scraped data is stored in a CSV file. A Flask application is then used to clean this data and apply a toxicity analysis model (Dexotify) to the comments. The results of the analysis are stored in a MongoDB database. Both the web scraping application and the Flask application are containerized using Docker.

## Structure 

.
├── comments_data
│   ├── fake_data.csv
│   └── fake_data.py
├── flask_app
│   ├── clean_comments.py
│   └── flask_app.py
├── templates
│   └── upload.html
├── web_scraping_app
│   ├── app.py
│   ├── facebook_utils.py
│   ├── mongodb_utils.py
│   └── image_utils.py
├── requirements.txt
└── dockerfile

