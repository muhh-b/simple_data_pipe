import urllib.request

def download_image(img_url, filename):
    try:
        opener = urllib.request.build_opener()
        urllib.request.install_opener(opener)
        img_data = opener.open(img_url)
        with open(filename, 'wb') as f:
            f.write(img_data.read())
    except Exception as e:
        print(f"Erreur lors du téléchargement de l'image: {e}")
