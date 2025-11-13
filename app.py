import gradio as gr
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import numpy as np

# Model definition
class HuskyWolfClassifier(nn.Module):
    def __init__(self, num_classes=2):
        super(HuskyWolfClassifier, self).__init__()
        self.resnet = models.resnet18(pretrained=False)
        num_features = self.resnet.fc.in_features
        self.resnet.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(num_features, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        return self.resnet(x)

# Load model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = HuskyWolfClassifier(num_classes=2)

try:
    checkpoint = torch.load('best_model.pth', map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    print("Model loaded successfully!")
except Exception as e:
    print(f"Warning: Could not load model weights: {e}")
    print("Using randomly initialized model for demo purposes.")

model = model.to(device)
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

class_names = ['Husky', 'Wolf']

def predict(image):
    """
    Predict whether the image contains a Husky or a Wolf.

    Args:
        image: PIL Image or numpy array

    Returns:
        dict: Confidence scores for each class
    """
    if image is None:
        return {"Error": 1.0}

    try:
        # Convert to PIL Image if needed
        if isinstance(image, np.ndarray):
            image = Image.fromarray(image)

        # Ensure RGB
        image = image.convert('RGB')

        # Preprocess
        img_tensor = transform(image).unsqueeze(0).to(device)

        # Predict
        with torch.no_grad():
            outputs = model(img_tensor)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)[0]

        # Create results dictionary
        results = {
            class_names[i]: float(probabilities[i])
            for i in range(len(class_names))
        }

        return results

    except Exception as e:
        return {"Error": f"Prediction failed: {str(e)}"}

# Example images info
examples = [
    ["data/train/husky/husky_1.jpg"] if __name__ == "__main__" else None,
    ["data/train/wolf/wolf_1.jpg"] if __name__ == "__main__" else None,
]

# Create Gradio interface
title = "🐺 Husky vs Wolf Classifier"
description = """
## Tackling Background Bias in Image Classification

This model classifies images as either **Husky** or **Wolf**.

### The Challenge
Traditional models often learn spurious correlations - for example, associating snowy backgrounds with wolves
and grassy backgrounds with huskies, rather than focusing on the actual animal features.

### Our Solution
- **Transfer Learning**: ResNet18 pretrained on ImageNet
- **Data Augmentation**: Extensive augmentation to prevent overfitting
- **Background Processing**: Training with background-removed images to force feature learning
- **Regularization**: Dropout and weight decay for better generalization

### Usage
Upload an image of a husky or wolf, and the model will predict the class with confidence scores.
"""

article = """
### Technical Details
- **Architecture**: ResNet18 with custom classifier head
- **Training**: 100 images (50 per class) with heavy augmentation
- **Validation**: Cross-validated with balanced test set
- **Visualization**: Grad-CAM confirms focus on animal features, not backgrounds

### Limitations
- Small training dataset (100 images) may limit generalization
- Best performance on images similar to training distribution
- Model may struggle with unusual angles or partial views

### About
This project demonstrates techniques for addressing dataset bias in computer vision.
The model was trained to focus on discriminative animal features rather than environmental context.
"""

interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.Label(num_top_classes=2, label="Predictions"),
    title=title,
    description=description,
    article=article,
    examples=examples if any(examples) else None,
    theme=gr.themes.Soft(),
    allow_flagging="never"
)

if __name__ == "__main__":
    interface.launch(share=True)
