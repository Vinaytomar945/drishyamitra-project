import React, { useState } from "react";
import Sidebar from "../components/Sidebar";

function Upload() {

  const [file, setFile] = useState(null);
  const [response, setResponse] = useState("");
  const [analysis, setAnalysis] = useState(null);

  const uploadImage = async () => {

    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("photo", file);

    try {

      const res = await fetch("http://localhost:5000/photo/upload", {
        method: "POST",
        body: formData
      });

      const data = await res.json();

      setResponse(data.message);
      setAnalysis(data.analysis);

    } catch (error) {
      console.error("Upload error:", error);
    }
  };

  return (

    <div style={{display:"flex"}}>

      <Sidebar />

      <div style={{padding:"40px"}}>

        <h2>Upload Image</h2>

        <input
          type="file"
          onChange={(e)=>setFile(e.target.files[0])}
        />

        <br /><br />

        <button onClick={uploadImage}>
          Upload Image
        </button>

        <h3>{response}</h3>

        {analysis && (
          <div>
            <h3>AI Analysis</h3>
            <p>Age: {analysis.age}</p>
            <p>Gender: {analysis.gender}</p>
            <p>Emotion: {analysis.emotion}</p>
          </div>
        )}

      </div>

    </div>

  );
}

export default Upload;