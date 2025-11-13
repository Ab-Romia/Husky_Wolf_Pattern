# 🚀 Deployment Guide to Hugging Face Spaces

This guide will help you deploy the Husky vs Wolf classifier to Hugging Face Spaces.

## Prerequisites

1. **Hugging Face Account**: Create a free account at [huggingface.co](https://huggingface.co)
2. **Trained Model**: You should have a `best_model.pth` file from training
3. **Git LFS**: Install Git Large File Storage for model files

## Step-by-Step Deployment

### Method 1: Web Interface (Easiest)

1. **Create a New Space**
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose a name (e.g., `husky-wolf-classifier`)
   - Select **Gradio** as the SDK
   - Choose **Public** visibility
   - Click "Create Space"

2. **Upload Files**
   - Upload the following files to your Space:
     - `app.py`
     - `requirements.txt`
     - `best_model.pth`

3. **Wait for Build**
   - Hugging Face will automatically install dependencies
   - The app will launch when build is complete
   - You'll see your Gradio interface live!

### Method 2: Git CLI (For Advanced Users)

```bash
# Clone your new Space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/husky-wolf-classifier
cd husky-wolf-classifier

# Install Git LFS (if not already installed)
git lfs install

# Copy project files
cp /path/to/app.py .
cp /path/to/requirements.txt .
cp /path/to/best_model.pth .

# Track the model file with Git LFS
git lfs track "*.pth"
git add .gitattributes

# Commit and push
git add .
git commit -m "Initial deployment of Husky vs Wolf classifier"
git push
```

## Files Required for Deployment

### 1. app.py (Already Created ✓)
Contains the Gradio interface and model inference code.

### 2. requirements.txt (Already Created ✓)
Lists all Python dependencies.

### 3. best_model.pth
Your trained model checkpoint. If you haven't trained yet:
```bash
# Run the training notebook first
jupyter notebook husky_wolf_classification.ipynb
# This will generate best_model.pth
```

### 4. Optional: README.md for the Space
You can create a custom README for your Hugging Face Space:

```markdown
---
title: Husky vs Wolf Classifier
emoji: 🐺
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

# Husky vs Wolf Classifier

Upload an image of a husky or wolf, and the model will classify it!

This model uses ResNet18 with transfer learning and addresses the background bias problem in computer vision.
```

## Testing Your Deployment

Once deployed, your app will be available at:
```
https://huggingface.co/spaces/YOUR_USERNAME/husky-wolf-classifier
```

Try uploading:
- Images from the test set
- New images from the internet
- Edge cases (puppies, foxes, mixed breeds)

## Troubleshooting

### Build Failed

**Check requirements.txt versions:**
- Make sure all package versions are compatible
- Try removing version constraints if needed

**Check model file size:**
- Hugging Face has file size limits
- Consider using smaller models if needed

### Model Not Loading

**Verify model file:**
```python
# Test locally first
python app.py
```

**Check device compatibility:**
```python
# In app.py, ensure:
device = torch.device('cpu')  # For Hugging Face deployment
```

### Slow Performance

**Optimize model:**
- Use smaller batch sizes
- Consider model quantization
- Use CPU-optimized inference

## Updating Your Deployment

To update your deployed model:

1. Train a new model → generates new `best_model.pth`
2. Upload the new file to your Space
3. Hugging Face will automatically rebuild

Or via Git:
```bash
cd husky-wolf-classifier
cp /path/to/new/best_model.pth .
git add best_model.pth
git commit -m "Update model with better accuracy"
git push
```

## Advanced Features

### Add Examples
Uncomment and modify the examples section in `app.py`:
```python
examples = [
    ["examples/husky1.jpg"],
    ["examples/wolf1.jpg"],
]
```

### Enable Sharing
In `app.py`, change:
```python
interface.launch(share=False)  # False for permanent deployment
```

### Add Analytics
Install and configure:
```bash
pip install gradio-analytics
```

### Custom Domain
Upgrade to Hugging Face Pro for custom domains.

## Local Testing Before Deployment

Always test locally first:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Test in browser at http://localhost:7860
```

## Cost

Hugging Face Spaces has a generous free tier:
- **Free**: Community hardware (CPU)
- **Upgraded**: GPU access for faster inference
- **Pro**: More resources and features

For this model, the free tier is sufficient.

## Security Notes

1. **Model File**: Safe to share (contains only weights)
2. **API Keys**: Never commit API keys or secrets
3. **User Inputs**: Gradio handles input validation
4. **Rate Limiting**: Consider adding for production use

## Next Steps

After deploying:

1. **Share**: Post on social media, forums, portfolio
2. **Monitor**: Check usage stats in Space settings
3. **Improve**: Collect feedback and retrain model
4. **Document**: Update README with demo link

## Resources

- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Gradio Documentation](https://gradio.app/docs)
- [Git LFS Guide](https://git-lfs.github.com/)

## Support

Issues with deployment? Check:
1. Space logs for error messages
2. Hugging Face forums
3. GitHub issues in this repository

---

**Ready to deploy?** Follow Method 1 above and have your model live in minutes! 🚀
