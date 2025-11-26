from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from io import BytesIO

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["POST", "GET", "OPTIONS"],
        "allow_headers": ["Content-Type"],
    }
})


# Load your trained model
MODEL_PATH = "model/plant_model.h5"   # DO NOT USE "backend/model/..."
model = load_model(MODEL_PATH)

# Order MUST match training dataset folder names
CLASS_NAMES = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_1",
    "Tomato_Target_Spot",
    "Tomato_Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato_Tomato_mosaic_virus",
    "Tomato_healthy"
]

# ----------------------------- RECOMMENDATION ENGINE --------------------------------
def get_recommendations(label):

    if "healthy" in label.lower():
        return [
            "Plant looks healthy 🌱",
            "Maintain watering schedule.",
            "Avoid wetting leaves.",
            "Monitor weekly."
        ]

    if "bacterial" in label.lower():
        return [
            "Remove infected leaves.",
            "Use copper-based organic fungicide.",
            "Do not spray water on leaves.",
            "Avoid touching plants after handling infected ones."
        ]

    if "blight" in label.lower():
        return [
            "Remove diseased leaves.",
            "Improve airflow between plants.",
            "Avoid overhead irrigation.",
            "Spray neem oil or organic fungicide."
        ]

    if "Leaf_Mold" in label:
        return [
            "Increase sunlight exposure.",
            "Reduce humidity.",
            "Prune densely packed leaves.",
            "Apply potassium bicarbonate spray."
        ]

    if "Septoria" in label:
        return [
            "Disinfect tools after pruning.",
            "Improve ventilation.",
            "Avoid splashing water on leaves.",
            "Apply copper fungicide."
        ]

    if "Spider" in label:
        return [
            "Spray underside of leaves with water.",
            "Use neem spray weekly.",
            "Introduce ladybugs.",
            "Keep soil moist (not wet)."
        ]

    if "virus" in label.lower():
        return [
            "Remove infected plants completely.",
            "Do NOT replant in the same soil.",
            "Disinfect tools and equipment.",
            "Use disease-resistant varieties."
        ]

    return [
        "Remove infected leaves.",
        "Improve air ventilation.",
        "Avoid direct leaf water spray.",
        "Use neem spray or organic fungicide."
    ]

# ----------------------------- PREDICTION API --------------------------------

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]

    # Convert file -> bytes -> PIL image
    img_bytes = file.read()
    img = load_img(BytesIO(img_bytes), target_size=(224, 224))

    # Preprocess
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    predictions = model.predict(img)[0]
    idx = np.argmax(predictions)
    confidence = float(predictions[idx])
    disease = CLASS_NAMES[idx]

    # Low Confidence Handling
    if confidence < 0.50:
        return jsonify({
            "disease": "Uncertain",
            "confidence": confidence,
            "recommendations": [
                "Upload a clearer leaf image.",
                "Avoid shadows or glare.",
                "Center the leaf in the frame."
            ]
        })

    return jsonify({
        "disease": disease,
        "confidence": confidence,
        "recommendations": get_recommendations(disease)
    })

# ----------------------------- TEST ROUTE --------------------------------

@app.route("/")
def home():
    return "🌱 Crop Disease Detection API Online"

# ----------------------------- RUN SERVER --------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5000)
