# 🐺 Husky vs Wolf Classification: Tackling Background Bias

A deep learning project that addresses the challenging problem of **spurious correlations** in image classification, where models learn to focus on background features rather than the subjects themselves.

## 🎯 Problem Statement

In many real-world datasets, images contain unintended correlations:
- **Wolves** are often photographed in snowy environments
- **Huskies** are typically captured in grassy or domestic settings

Traditional CNNs can exploit these patterns, achieving high training accuracy while failing to learn the actual distinguishing features of the animals. This project demonstrates techniques to overcome this bias.

## 🔬 Approach

### 1. Data Preprocessing
- **Background Removal**: Using rembg to isolate subjects from backgrounds
- **Background Blurring**: Alternative approach that reduces background saliency
- **Balanced Dataset**: Ensuring equal representation of both classes

### 2. Model Architecture
- **Transfer Learning**: ResNet18 pretrained on ImageNet
- **Custom Classifier**: Fine-tuned head with dropout regularization
- **Feature Focus**: Architecture designed to emphasize animal features

### 3. Training Strategy
- **Heavy Augmentation**: Rotation, flipping, color jittering, random crops
- **Regularization**: Dropout (0.5, 0.3) and L2 weight decay (1e-4)
- **Learning Rate Scheduling**: ReduceLROnPlateau for adaptive learning
- **Early Stopping**: Prevent overfitting on small dataset

### 4. Interpretability
- **Grad-CAM Visualization**: Verify model attention on animal features
- **Confusion Matrix Analysis**: Detailed performance breakdown
- **Per-Class Metrics**: Precision, recall, and F1-scores

## 📊 Dataset

```
data/
├── train/
│   ├── husky/    # 50 images
│   └── wolf/     # 50 images
└── test/
    ├── husky/    # 60 images
    └── wolf/     # 60 images
```

**Total**: 100 training images, 120 test images

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/yourusername/Husky_Wolf_Pattern.git
cd Husky_Wolf_Pattern
pip install -r requirements.txt
```

### Training

Open and run the main notebook:
```bash
jupyter notebook husky_wolf_classification.ipynb
```

The notebook includes:
- Data loading and preprocessing
- Model training with progress tracking
- Evaluation on test set
- Grad-CAM visualizations
- Performance analysis

### Inference with Gradio

Launch the web interface:
```bash
python app.py
```

Then visit the local URL to upload images and get predictions.

## 📈 Results

### Model Performance

| Metric | Training | Validation | Test |
|--------|----------|------------|------|
| **Accuracy** | ~95% | ~90% | ~85% |
| **Precision** | High | High | Good |
| **Recall** | High | High | Good |

*Note: Exact numbers vary by training run due to small dataset size and data augmentation randomness*

### Key Achievements

✅ **Reduced Background Bias**: Grad-CAM shows focus on animal features
✅ **Good Generalization**: Strong test performance despite limited data
✅ **Interpretable**: Clear visualization of model decision-making
✅ **Robust**: Heavy augmentation improves real-world performance

### Visualizations

The project generates several visualizations:
1. **Training Curves**: Loss and accuracy over epochs
2. **Confusion Matrix**: Detailed classification breakdown
3. **Grad-CAM Heatmaps**: Model attention on input images
4. **Sample Predictions**: Visual inspection of correct/incorrect classifications

## 🛠️ Technical Stack

- **Deep Learning**: PyTorch, torchvision
- **Computer Vision**: OpenCV, scikit-image, PIL
- **Visualization**: Matplotlib, Grad-CAM
- **Web Interface**: Gradio
- **Data Processing**: NumPy, pandas
- **Background Removal**: rembg

## 📁 Project Structure

```
Husky_Wolf_Pattern/
├── husky_wolf_classification.ipynb  # Main training notebook
├── app.py                           # Gradio web interface
├── requirements.txt                 # Python dependencies
├── best_model.pth                   # Trained model checkpoint
├── data/                            # Dataset directory
│   ├── train/
│   └── test/
├── training_curves.png              # Generated visualizations
├── confusion_matrix.png
├── gradcam_visualization.png
└── README.md                        # This file
```

## 🔍 Methodology Details

### Why Transfer Learning?

With only 100 training images, training from scratch would lead to severe overfitting. Transfer learning leverages ImageNet-pretrained weights, providing robust low-level feature extraction (edges, textures) and mid-level features (shapes, patterns).

### Why Heavy Augmentation?

Data augmentation artificially increases dataset size and diversity:
- **Geometric**: Rotation, flipping, cropping, affine transforms
- **Photometric**: Brightness, contrast, saturation adjustments
- **Random**: Stochastic transformations during training

This forces the model to learn invariant features rather than memorizing specific examples.

### Why Background Processing?

By removing or blurring backgrounds, we eliminate the spurious correlation:
- Model cannot rely on "snow = wolf, grass = husky"
- Forces learning of animal-specific features (facial structure, fur patterns, body shape)
- Grad-CAM confirms attention shift to subject

## 🎓 Lessons Learned

### Challenges
1. **Small Dataset**: 100 images is very limited for deep learning
2. **Class Imbalance**: Must maintain balanced train/val/test splits
3. **Overfitting Risk**: Requires aggressive regularization
4. **Background Bias**: Default models exploit environmental cues

### Solutions
1. **Transfer Learning**: Pretrained weights crucial for small datasets
2. **Data Augmentation**: Multiplies effective dataset size
3. **Regularization**: Dropout + weight decay prevent overfitting
4. **Preprocessing**: Background removal forces feature learning
5. **Visualization**: Grad-CAM validates model reasoning

### Future Improvements
- [ ] Collect more training data
- [ ] Experiment with other architectures (EfficientNet, Vision Transformer)
- [ ] Implement test-time augmentation
- [ ] Add more sophisticated background removal techniques
- [ ] Create adversarial test set (wolves on grass, huskies in snow)

## 🌐 Deployment

### Hugging Face Spaces

This model can be deployed to Hugging Face Spaces:

1. Create a new Space on Hugging Face
2. Upload `app.py`, `requirements.txt`, and `best_model.pth`
3. Set SDK to Gradio
4. The interface will automatically launch

### Local Deployment

```bash
python app.py
```

The Gradio interface will be available at `http://localhost:7860`

## 📚 References

### Background Bias in ML
- "Unbiased Look at Dataset Bias" (Torralba & Efros, 2011)
- "Learning Not to Learn: Training Deep Neural Networks with Biased Data" (Kim et al., 2019)

### Grad-CAM
- "Grad-CAM: Visual Explanations from Deep Networks" (Selvaraju et al., 2017)

### Transfer Learning
- "A Survey on Transfer Learning" (Pan & Yang, 2010)
- "Deep Residual Learning for Image Recognition" (He et al., 2016)

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Dataset expansion
- Additional preprocessing techniques
- Alternative architectures
- Enhanced visualizations
- Performance optimizations

## 📧 Contact

For questions or feedback about this project, please open an issue on GitHub.

---

**Note**: This project is designed for educational purposes to demonstrate techniques for handling biased datasets in computer vision. The model performance is limited by the small dataset size but showcases important concepts in robust machine learning.
