import torch
from PIL import Image
from transformers import AutoModelForImageClassification, AutoImageProcessor

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