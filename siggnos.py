import requests
from bs4 import BeautifulSoup
import os

def scrape_and_download_images(url, output_folder):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        img_tags = soup.find_all("img", class_="gsc-thumbnail-inside")
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for idx, img_tag in enumerate(img_tags, start=1):
            img_url = img_tag["src"]
            img_name = f"image_{idx}.jpg" 
            img_path = os.path.join(output_folder, img_name)
            
            img_data = requests.get(img_url).content
            with open(img_path, "wb") as f:
                f.write(img_data)
            
            print(f"Imagen {idx} descargada: {img_path}")

    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)
    except Exception as e:
        print("Ocurrió un error:", e)

url = "https://www.kaggle.com/datasets/rub3ntercero/lenguaje-de-signos-espaol" #Tambien usamos este https://www.fundacioncnse.org/educa/bancolse/dactilologico.php#b&gsc.tab=0

output_folder = "sign_language_images"
scrape_and_download_images(url, output_folder)