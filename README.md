

# Crop Disease Detection

An AI-powered application that detects crop diseases from leaf images and provides treatment recommendations.

## Repository

[https://github.com/meghanakongara0429/Crop-Disease-Detection](https://github.com/meghanakongara0429/Crop-Disease-Detection)

## Overview

The system uses a deep learning model (MobileNetV2) to classify diseases in tomato, potato, and pepper leaves.
Frontend allows image upload and displays detection results.
Backend predicts disease and returns recommendations.

## Tech Stack

Backend:

* Python
* TensorFlow / Keras
* Flask
* Flask-CORS
* NumPy
* Pillow

Frontend:

* React.js
* Axios
* TailwindCSS

## Dataset

PlantVillage Dataset (Kaggle)
[https://www.kaggle.com/datasets/emmarex/plantdisease](https://www.kaggle.com/datasets/emmarex/plantdisease)
*~54,000 leaf images across multiple crops & disease classes*

## Features

* Upload leaf images
* Disease prediction
* Confidence percentage
* Recommendation suggestions
* Simple responsive UI

## Project Structure

```
Crop-Disease-Detection/
│
├── backend
│   ├── app.py
│   ├── model
│   │   └── plant_model.h5
│   └── utils
│       └── recommendation.py
│
├── frontend
│   ├── src
│   │   └── components
│   │       └── Upload.js
```

## Setup

### Backend Setup

```
cd backend
pip install -r requirements.txt
python app.py
```

Backend will start at:
[http://localhost:5000](http://localhost:5000)

If you don't have a requirements file, install manually:

```
pip install flask flask-cors tensorflow pillow numpy
```

### Frontend Setup

```
cd frontend
npm install
npm start
```

Frontend runs at:
[http://localhost:3000](http://localhost:3000)

## API Endpoint

### POST /predict

Input: multipart form-data, field name "image"

Response:

```
{
  "disease": "Tomato_Early_blight",
  "confidence": 0.91,
  "recommendations": [
    "Remove infected leaves.",
    "Avoid overhead watering.",
    "Use neem oil spray."
  ]
}
```

## Supported Diseases

Examples:

* Tomato_Early_blight
* Tomato_Late_blight
* Tomato_Leaf_Mold
* Tomato_Septoria_leaf_spot
* Tomato_Spider_mites_1
* Tomato_Yellow_Leaf_Curl_Virus
* Tomato_healthy
* Potato_Early_blight
* Pepper_Bacterial_spot

## How It Works

1. User uploads a leaf image
2. Frontend sends it to Flask API
3. Model preprocesses and predicts the disease class
4. API returns predicted class, confidence, and recommendations
5. UI displays results

## Future Enhancements

* Multilingual UI (Telugu/Hindi)
* Mobile app
* Weather-based alerts
* Model optimization
* PDF report generation

## License

MIT

## Author

Meghana Kongara

