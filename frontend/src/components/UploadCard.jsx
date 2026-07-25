import { useState, useRef } from "react";
import { FaSpinner, FaCloudUploadAlt } from "react-icons/fa";
import api from "../services/api";

function UploadCard({ onResult }) {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [loadingText, setLoadingText] = useState("");

  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];

    if (!selectedFile) {
      handleClear();
      return;
    }

    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      setLoadingText("Preparing image...");

      setTimeout(() => {
        setLoadingText("Uploading image...");
      }, 700);

      setTimeout(() => {
        setLoadingText("Running AI model...");
      }, 1500);

      setTimeout(() => {
        setLoadingText("Generating Grad-CAM...");
      }, 2500);

      setTimeout(() => {
        setLoadingText("Generating AI Medical Report...");
      }, 3500);

      const response = await api.post("/predict", formData);

      onResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Upload failed.");
    } finally {
      setLoading(false);
      setLoadingText("");
    }
  };

  const handleClear = () => {
    setFile(null);
    setPreview(null);
    setLoading(false);
    setLoadingText("");

    onResult(null);

    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  return (
    <>
      {loading && (
        <div className="loading-overlay">
          <div className="loading-card">
            <FaSpinner className="spinner-icon" />

            <h2>AI is analyzing your Chest X-ray</h2>

            <p>{loadingText}</p>

            <div className="loading-steps">
              <p>🧠 Deep Learning Analysis</p>
              <p>🔥 Grad-CAM Generation</p>
              <p>🤖 AI Medical Report</p>
            </div>
          </div>
        </div>
      )}

      <div className="card">
        <h2 style={{ textAlign: "center" }}>Upload Chest X-ray</h2>

        {!preview && (
          <label className="upload-box">
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              onChange={handleFileChange}
              disabled={loading}
              hidden
            />

            <div className="upload-content">
              <div className="upload-icon">📁</div>

              <h3>Upload Chest X-ray</h3>

              <p>Click here or drag & drop your image</p>

              <small>Supported formats: JPG, PNG, JPEG</small>
            </div>
          </label>
        )}

        {preview && (
          <div className="preview-container">
            <div className="success-message">
              ✅ Image Selected Successfully
            </div>

            <img
              src={preview}
              alt="Preview"
              className="preview-image"
            />

            <p className="file-name">{file?.name}</p>
          </div>
        )}

        <div className="button-group">
          <button
            onClick={handleUpload}
            disabled={loading || !preview}
          >
            {loading ? (
              <>
                <FaSpinner className="btn-spinner" />
                Analyzing...
              </>
            ) : (
              <>
                <FaCloudUploadAlt />
                Analyze Image
              </>
            )}
          </button>

          <button
            className="clear-btn"
            onClick={handleClear}
            disabled={loading || !preview}
          >
            🗑 Clear
          </button>
        </div>
      </div>
    </>
  );
}

export default UploadCard;