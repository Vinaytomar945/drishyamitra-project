import React from "react";
import { Link } from "react-router-dom";
import Sidebar from "../components/Sidebar";

function Dashboard() {
  return (
    <div style={{ display: "flex" }}>
      
      <Sidebar />

      <div style={{ marginLeft: "40px", marginTop: "40px" }}>
        <h1>Welcome to DrishyaMitra Dashboard</h1>
        <p>Upload photos, analyze faces and manage your gallery.</p>

        <br />

        <Link to="/upload">
          <button>Upload Photo</button>
        </Link>

        <br /><br />

        <Link to="/gallery">
          <button>View Gallery</button>
        </Link>

        <br /><br />

        <Link to="/chat">
          <button>AI Chat</button>
        </Link>

      </div>

    </div>
  );
}

export default Dashboard;