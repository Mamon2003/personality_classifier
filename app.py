import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
from flask import Flask, render_template, request, jsonify
import os

class PersonalityClassifier:
    def __init__(self):
        self.best_model = None
        self.scaler = None
        self.label_encoder = None
        self.feature_names = None
        
    def load_model(self, model_path='personality_model.pkl'):
        """Load the trained model"""
        try:
            model_data = joblib.load(model_path)
            self.best_model = model_data['model']
            self.scaler = model_data['scaler']
            self.label_encoder = model_data['label_encoder']
            self.feature_names = model_data['feature_names']
            print("✅ Model loaded successfully")
            return True
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            return False
    
    def predict_personality(self, features):
        """Predict personality type for new data"""
        try:
            # Convert features to DataFrame
            feature_df = pd.DataFrame([features], columns=self.feature_names)
            
            # Encode categorical variables
            categorical_cols = ['Stage_fear', 'Drained_after_socializing']
            for col in categorical_cols:
                if col in feature_df.columns:
                    feature_df[col] = self.label_encoder.transform(feature_df[col])
            
            # Scale features
            features_scaled = self.scaler.transform(feature_df)
            
            # Make prediction
            prediction = self.best_model.predict(features_scaled)[0]
            probability = self.best_model.predict_proba(features_scaled)[0]
            
            return prediction, probability
        except Exception as e:
            print(f"❌ Prediction error: {e}")
            return None, None

# Initialize Flask app
app = Flask(__name__)

# Initialize classifier
classifier = PersonalityClassifier()

# Load model on startup
def load_model():
    """Load the model before first request"""
    success = classifier.load_model()
    if not success:
        print("⚠️ Warning: Model could not be loaded. Please ensure personality_model.pkl exists.")

# Load model immediately when app starts
load_model()

@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint"""
    if classifier.best_model is None:
        return jsonify({'error': 'Model not loaded. Please check if personality_model.pkl exists.'})
    
    try:
        data = request.get_json()
        
        # Extract features
        features = [
            float(data['time_spent_alone']),
            data['stage_fear'],
            float(data['social_event_attendance']),
            float(data['going_outside']),
            data['drained_after_socializing'],
            float(data['friends_circle_size']),
            float(data['post_frequency'])
        ]
        
        # Make prediction
        prediction, probability = classifier.predict_personality(features)
        
        if prediction is None:
            return jsonify({'error': 'Prediction failed. Please try again.'})
        
        return jsonify({
            'prediction': prediction,
            'probability': {
                'Extrovert': float(probability[0]),
                'Introvert': float(probability[1])
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'Error processing request: {str(e)}'})

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': classifier.best_model is not None
    })

if __name__ == '__main__':
    # Load model immediately for local testing
    classifier.load_model()
    app.run(debug=False, host='0.0.0.0', port=5000) 