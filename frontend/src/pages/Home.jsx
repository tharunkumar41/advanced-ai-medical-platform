import { useState } from "react";
import UploadCard from "../components/UploadCard";
import PredictionCard from "../components/PredictionCard";
import HistoryTable from "../components/HistoryTable";

function Home() {
  const [result, setResult] = useState(null);

  return (
    <div className="container">
      <div className="hero">
        <h1>🏥 Advanced AI Medical Intelligence Platform</h1>
        <p>AI-powered Chest X-ray Diagnosis & Clinical Decision Support</p>
      </div>

      <UploadCard onResult={setResult} />

      <PredictionCard result={result} />

      <HistoryTable />
    </div>
  );
}

<footer className="footer">
  <h3>🏥 Advanced AI Medical Intelligence Platform</h3>

  <p>AI-powered Chest X-ray Diagnosis & Clinical Decision Support</p>

  <p>
    Built with <strong>React</strong> • <strong>FastAPI</strong> •
    <strong> TensorFlow</strong> • <strong>Gemini AI</strong> •
    <strong> Grad-CAM</strong>
  </p>

  <p>© 2026 Tharun Kumar. All Rights Reserved.</p>
</footer>

export default Home;