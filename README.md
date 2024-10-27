# Table Classification Web App

This is a Flask-based web application for classifying table images into three categories: bordered, borderless, and raw-bordered. The application takes an image file as input, resizes it, and processes it using a fine-tuned deep learning model based on a vision transformer. This model was trained on a custom dataset to identify distinct table styles.

## Table of Contents
- [Table Classification Web App](#table-classification-web-app)
  - [Table of Contents](#table-of-contents)
  - [Demo](#demo)
  - [Features](#features)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Install Dependencies](#step-2-install-dependencies)
    - [Step 3: Download the Model](#step-3-download-the-model)
    - [Step 4: Run the Application](#step-4-run-the-application)
  - [Additional Notes](#additional-notes)
  - [Model Details](#model-details)
  - [How to Use](#how-to-use)
  - [Prediction Output Example](#prediction-output-example)
  - [File Structure](#file-structure)
  - [Acknowledgements](#acknowledgements)

## Demo
Below are examples of the classifications the model provides:

1. **Bordered Table**  
<div style="display: flex; justify-content: space-around;">
  <img src="static/Class 0.png" alt="Example 1" width="500"/>
</div>
   
2. **Borderless Table**  
<div style="display: flex; justify-content: space-around;">
  <img src="static/Class 1.png" alt="Example 1" width="500"/>
</div>

3. **Raw-Bordered Table**  
<div style="display: flex; justify-content: space-around;">
  <img src="static/Class 2.png" alt="Example 1" width="500"/>
</div>

## Features
- **Image Upload**: Users can upload `.png`, `.jpg`, `.jpeg`, and `.gif` files.
- **Image Resizing**: Images are resized to 512x512 pixels for standard processing.
- **Classification Results**: The model predicts the table style and displays the result.
- **Downloadable Output**: Processed and resized images can be viewed and downloaded.

## Setup and Installation

### Prerequisites
- **Python** (>= 3.7)
- **Pip** for package installation

### Step 1: Clone the Repository
```bash
    git clone https://github.com/your-username/table-classification.git
    cd table-classification
```

### Step 2: Install Dependencies
```bash 
    pip install -r requirements.txt
```

### Step 3: Download the Model
The model will be automatically downloaded the first time you run the app.

### Step 4: Run the Application
```bash 
python main.py
```
The app will start at http://127.0.0.1:8081.

## Additional Notes
- The uploads folder is created automatically for storing user-uploaded images.
- Resized images and classification results are temporarily stored for quick reference.

## Model Details
The model is a fine-tuned Vision Transformer (ViT) specifically adapted for classifying table layouts. The categories are:

- Bordered
- Borderless
- Raw-Bordered
  
Model Download and Configuration
- The model is hosted on Google Drive and downloaded using gdown.
- Saved to model/vit-base for processing.

## How to Use
1. Open the app in a web browser.
2. Upload an image file of a table.
3. Click "Submit" to classify the image.
4. The predicted label and the resized image will be displayed.

## Prediction Output Example
The prediction includes:

- Class ID: Integer representing the predicted category.
- Label: String label (bordered, borderless, or raw-bordered).

## File Structure
```plaintext
.
├── main.py                 # Main Flask application
├── predict.py              # Prediction logic and model loading
├── requirements.txt        # Python package dependencies
├── static                  # Static files (CSS, JS)
├── templates
│   └── index.html          # HTML template
└── uploads                 # Folder for storing uploaded images
```
## Acknowledgements

- Hugging Face Transformers for providing the Vision Transformer (ViT) model.
- Google Drive for hosting the model checkpoint.
- Pillow for image processing.
