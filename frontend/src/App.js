import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";
import Gallery from "./pages/Gallery";
import Chat from "./pages/Chat";

function App() {
  return (
    <Router>
      <Routes>

        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/gallery" element={<Gallery />} />
        <Route path="/chat" element={<Chat />} />

      </Routes>
    </Router>
  );
}

export default App;
// import React, { useState } from "react";

// function App() {
//   const [file, setFile] = useState(null);
//   const [preview, setPreview] = useState(null);
//   const [response, setResponse] = useState("");
//   const [analysis, setAnalysis] = useState(null);

//   const handleFileChange = (e) => {
//     const selectedFile = e.target.files[0];
//     setFile(selectedFile);

//     // show preview before upload
//     if (selectedFile) {
//       setPreview(URL.createObjectURL(selectedFile));
//     }
//   };

//   const handleUpload = async () => {
//     if (!file) {
//       setResponse("Please select an image first");
//       return;
//     }

//     const formData = new FormData();

//     // IMPORTANT: backend expects "photo"
//     formData.append("photo", file);

//     try {
//       const res = await fetch("http://localhost:5000/photo/upload", {
//         method: "POST",
//         body: formData,
//       });

//       const data = await res.json();

//       setResponse(data.message);

//       if (data.analysis) {
//         setAnalysis(data.analysis);
//       }
//     } catch (error) {
//       console.error("Upload failed:", error);
//       setResponse("Upload failed");
//     }
//   };

//   return (
//     <div style={{ textAlign: "center", marginTop: "50px" }}>
//       <h1>DrishyaMitra - Image Preview 🚀</h1>

//       <input type="file" onChange={handleFileChange} />

//       <br />
//       <br />

//       <button onClick={handleUpload}>Upload Image</button>

//       <h2>{response}</h2>

//       {/* Image Preview */}
//       {preview && (
//         <img
//           src={preview}
//           alt="Preview"
//           width="300"
//           style={{ marginTop: "20px", border: "3px solid red" }}
//         />
//       )}

//       {/* AI Analysis Result */}
//       {analysis && (
//         <div style={{ marginTop: "20px" }}>
//           <h2>AI Analysis</h2>
//           <p><b>Age:</b> {analysis.age}</p>
//           <p><b>Gender:</b> {analysis.gender}</p>
//           <p><b>Emotion:</b> {analysis.emotion}</p>
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;