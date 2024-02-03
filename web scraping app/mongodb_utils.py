from pymongo import MongoClient

def store_to_mongodb(pubs, mongodb_url):
    try:
        client = MongoClient(mongodb_url)
        mydb = client.get_default_database()  # Sélectionnez la base de données par défaut
        mycol = mydb["posts"]  # Sélectionnez la collection des publications
        mycol.insert_many(pubs)  # Insérez les données dans la collection
    except Exception as e:
        print(f"Erreur lors de l'enregistrement dans MongoDB: {e}")
