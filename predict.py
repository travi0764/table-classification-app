import os
import shutil
import gdown
import torch
from PIL import Image
from transformers import AutoModelForImageClassification, AutoImageProcessor

DOWNLOAD_URL = f'https://drive.google.com/drive/folders/1z0kB1TWQOTMWvgOERGbE8jaW1tzo71tz?usp=sharing'
# Path to save the downloaded model
MODEL_PATH = 'model'

def download_model():
    if os.path.exists(MODEL_PATH):
        shutil.rmtree(MODEL_PATH)
    os.makedirs(MODEL_PATH)
    
    gdown.download_folder(url=DOWNLOAD_URL, output=MODEL_PATH, quiet=True, use_cookies=False)
    print("Model folder downloaded successfully.")

download_model()
# Load your fine-tuned model (make sure to update the path and model loading mechanism)
model_path = "model/vit-base"
image_processor = AutoImageProcessor.from_pretrained(model_path)
model = AutoModelForImageClassification.from_pretrained(model_path)
model.eval()

def predict_image(image_path):
    # Define image transformations
    image = Image.open(image_path)
    encoding = image_processor(image.convert("RGB"), return_tensors="pt")
    
    # Open and transform the image
    with torch.no_grad():
        outputs = model(**encoding)
        logits = outputs.logits
    
    predicted_class_idx = logits.argmax(-1).item()
    labels = ['bordered', 'borderless', 'raw-bordered']
    label = labels[predicted_class_idx]
    
    return {"class": predicted_class_idx, "label": label}