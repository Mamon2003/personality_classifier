# 🚀 PythonAnywhere Deployment Guide

## 📋 Prerequisites

1. **PythonAnywhere Account**: Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. **Trained Model**: Ensure `personality_model.pkl` is ready
3. **Files Ready**: All project files should be prepared

## 📁 Files to Upload

Upload these files to your PythonAnywhere account:

```
📦 Deployment Files:
├── app.py                    # Main Flask application
├── personality_model.pkl     # Trained model (CRITICAL!)
├── requirements_deploy.txt   # Minimal dependencies
├── templates/
│   └── index.html           # Web interface
└── DEPLOYMENT_GUIDE.md      # This guide
```

## 🛠️ Step-by-Step Deployment

### 1. **Upload Files to PythonAnywhere**

1. Go to your PythonAnywhere dashboard
2. Navigate to **Files** tab
3. Create a new directory: `personality_classifier`
4. Upload all files to this directory

### 2. **Install Dependencies**

1. Go to **Consoles** tab
2. Open a **Bash console**
3. Navigate to your project directory:
   ```bash
   cd personality_classifier
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements_deploy.txt
   ```

### 3. **Configure Web App**

1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose **Flask**
4. Select **Python 3.9** or higher
5. Set **Source code**: `/home/yourusername/personality_classifier`
6. Set **Working directory**: `/home/yourusername/personality_classifier`

### 4. **Configure WSGI File**

1. Click on your web app
2. Go to **Code** section
3. Click **WSGI configuration file**
4. Replace the content with:

```python
import sys
path = '/home/yourusername/personality_classifier'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

**Important**: Replace `yourusername` with your actual PythonAnywhere username!

### 5. **Set Environment Variables**

1. In the **Web** tab, go to **Environment variables**
2. Add if needed:
   - `FLASK_ENV=production`
   - `FLASK_DEBUG=0`

### 6. **Reload Web App**

1. Click **Reload** button
2. Wait for the green checkmark
3. Your app should be live at: `yourusername.pythonanywhere.com`

## 🔍 Testing Your Deployment

### 1. **Health Check**
Visit: `yourusername.pythonanywhere.com/health`
Should return: `{"status": "healthy", "model_loaded": true}`

### 2. **Main Interface**
Visit: `yourusername.pythonanywhere.com`
Should show the personality classifier interface

### 3. **Test Prediction**
Use the web interface to make a prediction

## 🚨 Troubleshooting

### **Common Issues & Solutions**

#### 1. **Model Loading Error**
```
❌ Error: Model file not found
```
**Solution**: Ensure `personality_model.pkl` is uploaded to the correct directory

#### 2. **Import Errors**
```
❌ Error: No module named 'sklearn'
```
**Solution**: Install dependencies:
```bash
pip install -r requirements_deploy.txt
```

#### 3. **WSGI Configuration Error**
```
❌ Error: Import error in WSGI file
```
**Solution**: Check the WSGI file path and username

#### 4. **500 Internal Server Error**
**Solution**: Check the error logs in the **Web** tab

### **Debugging Steps**

1. **Check Logs**: Go to **Web** tab → **Log files**
2. **Test Console**: Use Bash console to test imports
3. **Verify Files**: Ensure all files are uploaded correctly

## 📊 Performance Optimization

### **For Better Performance**

1. **Enable HTTPS**: In **Web** tab → **HTTPS** section
2. **Set up Custom Domain**: If needed
3. **Monitor Usage**: Check **Account** tab for resource usage

### **Memory Optimization**

- The model file is ~1-2MB
- Minimal dependencies reduce memory usage
- Flask app is lightweight

## 🔒 Security Considerations

1. **HTTPS**: Enable in PythonAnywhere settings
2. **Input Validation**: Already implemented in the app
3. **Error Handling**: Comprehensive error handling included
4. **Rate Limiting**: Consider adding if needed

## 📈 Monitoring

### **Health Check Endpoint**
- URL: `/health`
- Returns model status
- Use for monitoring

### **Error Logs**
- Check **Web** tab → **Log files**
- Monitor for errors

## 🎯 Success Checklist

- [ ] Files uploaded to PythonAnywhere
- [ ] Dependencies installed
- [ ] Web app configured
- [ ] WSGI file updated
- [ ] App reloaded successfully
- [ ] Health check passes
- [ ] Main interface loads
- [ ] Predictions work

## 🆘 Support

### **If You Need Help**

1. **Check Logs**: Always check error logs first
2. **PythonAnywhere Docs**: [help.pythonanywhere.com](https://help.pythonanywhere.com)
3. **Community**: PythonAnywhere forums

### **Useful Commands**

```bash
# Check if model file exists
ls -la personality_model.pkl

# Test Python imports
python -c "import joblib; import sklearn; print('OK')"

# Check app.py syntax
python -m py_compile app.py
```

---

## 🎉 Your App is Ready!

Once deployed, your personality classifier will be available at:
**`https://yourusername.pythonanywhere.com`**

The app includes:
- ✅ Beautiful web interface
- ✅ Real-time predictions
- ✅ Confidence scores
- ✅ Error handling
- ✅ Health monitoring
- ✅ Mobile-responsive design

**Happy deploying! 🚀** 