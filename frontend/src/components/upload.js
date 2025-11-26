import React, { useState } from "react";
import axios from "axios";

export default function Upload() {
    const [file, setFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);

    const handleFile = (e) => {
        const img = e.target.files[0];
        setFile(img);
        setPreview(URL.createObjectURL(img));
        setResult(null);
    };

    const handlePredict = async () => {
        if (!file) return alert("Please upload a leaf image!");

        const formData = new FormData();
        formData.append("image", file);
        setLoading(true);

        try {
            const res = await axios.post(
                "https://crop-disease-detection-9-znu8.onrender.com",
                formData,
                { headers: { "Content-Type": "multipart/form-data" } }
            );
            setResult(res.data);
        } catch (err) {
            alert("Server disconnected or backend error.");
        }

        setLoading(false);
    };

    return (
        <div
            className="min-h-screen flex justify-center items-center bg-cover bg-center p-8"
            style={{
                backgroundImage: "url('https://i0.wp.com/razzanj.com/wp-content/uploads/2016/07/nature-landscape-nature-landscape-hd-image-download-wheat-farm-hd-wallpaper-notebook-background-wheat-farmers-wheat-farming-process-wheat-farming-in-kenya.jpg?ssl=1')",
            }}
        >
            <div className="bg-white/80 backdrop-blur-md shadow-2xl rounded-2xl p-8 max-w-xl w-full border border-white/40">
                <h1 className="text-4xl font-bold text-green-700 text-center">
                    🌱 Crop Disease Detector
                </h1>

                <p className="text-center text-gray-600 mt-2">
                    Upload a high-quality leaf image to detect disease
                </p>

                {/* Upload Section */}
                <div className="mt-6 border-2 border-dashed border-green-500/60 rounded-xl p-6 text-center hover:bg-green-50/60 transition cursor-pointer">
                    <label className="cursor-pointer">
                        <input
                            type="file"
                            accept="image/*"
                            className="hidden"
                            onChange={handleFile}
                        />
                        <span className="text-gray-700 font-medium">
                            📷 Click to Upload Leaf Image
                        </span>
                    </label>
                </div>

                {/* Image Preview */}
                {preview && (
                    <div className="flex justify-center mt-5">
                        <img
                            src={preview}
                            alt="preview"
                            className="w-56 h-56 object-cover rounded-xl shadow-lg border border-green-200"
                        />
                    </div>
                )}

                {/* Predict Button */}
                <button
                    className="w-full mt-6 py-3 text-lg font-semibold bg-green-600 hover:bg-green-700 text-white rounded-xl shadow-md transition"
                    onClick={handlePredict}
                >
                    🔍 Predict Disease
                </button>

                {/* Loading */}
                {loading && (
                    <p className="text-center text-green-700 font-semibold mt-4 animate-pulse">
                        🌾 Analyzing image...
                    </p>
                )}

                {/* Result Box */}
                {result && (
                    <div className="mt-6 bg-green-50 border border-green-200 rounded-xl p-5">
                        <h2 className="text-xl font-bold text-green-700">
                            Disease: {result.disease}
                        </h2>
                        <p className="text-gray-700 mt-1">
                            Confidence:
                            <span className="font-semibold">
                                {" "}
                                {(result.confidence * 100).toFixed(2)}%
                            </span>
                        </p>

                        <h3 className="mt-3 text-green-700 font-semibold">
                            Recommendations:
                        </h3>
                        <ul className="list-disc ml-6 text-gray-700 mt-2">
                            {result.recommendations?.map((item, index) => (
                                <li key={index}>{item}</li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        </div>
    );
}
