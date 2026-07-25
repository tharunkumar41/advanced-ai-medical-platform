import { useEffect, useState } from "react";
import api from "../services/api";

function HistoryTable() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const response = await api.get("/history");
      setHistory(response.data);
    } catch (error) {
      console.error("Failed to load history", error);
    }
  };

  return (
    <div className="card">
      <h2>📜 Prediction History</h2>

      <table>
        <thead>
          <tr>
            <th>📄 Image</th>
            <th>🩺 Diagnosis</th>
            <th>🎯 Confidence</th>
          </tr>
        </thead>

        <tbody>
          {history.length === 0 ? (
            <tr>
              <td colSpan="3">No predictions available.</td>
            </tr>
          ) : (
            history.map((item) => {
              const isNormal = item.prediction
                .toLowerCase()
                .includes("normal");

              return (
                <tr key={item.id}>
                  <td>{item.filename}</td>

                  <td>
                    <span
                      className={`history-badge ${
                        isNormal
                          ? "history-normal"
                          : "history-pneumonia"
                      }`}
                    >
                      {isNormal ? "🟢 Normal" : "🔴 Pneumonia"}
                    </span>
                  </td>

                  <td>{item.confidence}%</td>
                </tr>
              );
            })
          )}
        </tbody>
      </table>
    </div>
  );
}

export default HistoryTable;