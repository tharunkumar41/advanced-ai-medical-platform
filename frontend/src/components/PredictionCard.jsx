function formatReport(report) {
  const sections = report
    .split(/\n\s*\n/)
    .map((section) => section.trim())
    .filter(
      (section) => section && section !== "---" && !/^[-*#\s]+$/.test(section),
    );

  return sections.map((section, index) => {
    const lines = section.split("\n").filter((line) => line.trim());

    const title = lines[0];
    const content = lines.slice(1).join("\n");

    let icon = "📄";

    if (title.toLowerCase().includes("summary")) icon = "📋";
    else if (title.toLowerCase().includes("interpretation")) icon = "🔬";
    else if (title.toLowerCase().includes("recommendation")) icon = "💡";
    else if (title.toLowerCase().includes("disclaimer")) icon = "⚠️";

    return (
      <div className="report-section" key={index}>
        <h3>
          {icon} {title.replace(/\*/g, "")}
        </h3>
        {content && <p>{content.replace(/\*\*/g, "")}</p>}
      </div>
    );
  });
}

function PredictionCard({ result }) {
  if (!result) return null;

  const isNormal = result.prediction.toLowerCase().includes("normal");

  return (
    <div className="card prediction-card">
      <h2>🩺 AI Diagnosis</h2>

      <div className={`prediction-badge ${isNormal ? "normal" : "pneumonia"}`}>
        {isNormal ? "🟢 NORMAL" : "🔴 PNEUMONIA"}
      </div>

      <p className="confidence-text">
        Confidence: <strong>{result.confidence}%</strong>
      </p>

      <div className="progress-bar">
        <div
          className={`progress-fill ${isNormal ? "normal-fill" : "pneumonia-fill"}`}
          style={{ width: `${result.confidence}%` }}
        ></div>
      </div>

      <p className="filename">📄 {result.filename}</p>

      <hr />

      <div className="summary-grid">
        <div className="summary-card">
          <span className="summary-icon">🩺</span>
          <h4>Diagnosis</h4>
          <p className={isNormal ? "normal-text" : "pneumonia-text"}>
            {result.prediction}
          </p>
        </div>

        <div className="summary-card">
          <span className="summary-icon">🎯</span>
          <h4>Confidence</h4>
          <p>{result.confidence}%</p>
        </div>

        <div className="summary-card">
          <span className="summary-icon">📄</span>
          <h4>Filename</h4>
          <p>{result.filename}</p>
        </div>

        <div className="summary-card">
          <span className="summary-icon">🤖</span>
          <h4>AI Status</h4>
          <p>Analysis Complete</p>
        </div>
      </div>

      <div className="image-section">
        <div className="image-card">
          <h3>🖼 Original X-ray</h3>

          <img
            src={`http://localhost:8000/uploads/${result.filename}`}
            alt="Original"
          />
        </div>

        {result.gradcam_image && (
          <div className="image-card">
            <h3>🔥 Grad-CAM</h3>

            <img
              src={`http://localhost:8000${result.gradcam_image}`}
              alt="GradCAM"
            />
          </div>
        )}
      </div>

      <hr />

      <h2>🤖 AI Medical Report</h2>

      <div className="report-box">{formatReport(result.report)}</div>
    </div>
  );
}

export default PredictionCard;
