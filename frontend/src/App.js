import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [imageUrl, setImageUrl] = useState("");
  const [response, setResponse] = useState("");
  const [prediction, setPrediction] = useState("");

  const handleUpload = () => {
    if (!file) {
      setResponse("Please select an image first");
      return;
    }

    const formData = new FormData();
    formData.append("image", file);

    fetch("http://localhost:5000/upload", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        setResponse(data.message);
        setImageUrl(`http://localhost:5000/uploads/${file.name}`);
        setPrediction(data.prediction);
      });
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>DrishyaMitra - Image Preview 🚀</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>Upload Image</button>

      <h2>{response}</h2>
      {prediction && (
  <h2 style={{ color: "green" }}>{prediction}</h2>
)}

      {imageUrl && (
        <img
          src={imageUrl}
          alt="Uploaded"
          width="300"
          style={{ marginTop: "20px" }}
        />
      )}
    </div>
  );
}

export default App;