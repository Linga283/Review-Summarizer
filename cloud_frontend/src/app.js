import React, { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setLoading(true);
    try {
      const res = await fetch("https://review-summarizer-backend.onrender.com/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setResult({ summary: "Error fetching summary.", like_percentage: 0, dislike_percentage: 0, sample_reviews: [] });
    }
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 30 }}>
      <h2>Product Feedback Summarizer</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Paste Amazon product link"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={{ width: "80%", padding: 8 }}
        />
        <button type="submit" style={{ padding: 8, marginLeft: 10 }}>
          Summarize
        </button>
      </form>
      {loading && <p>Loading...</p>}
      {result && (
        <div style={{ marginTop: 30 }}>
          <h3>Summary</h3>
          <p>{result.summary}</p>
          <p>
            <b>Like %:</b> {result.like_percentage} <br />
            <b>Dislike %:</b> {result.dislike_percentage}
          </p>
          <h3>Sample Reviews</h3>
          <ul>
            {result.sample_reviews.map((r, i) => (
              <li key={i}>{r}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
