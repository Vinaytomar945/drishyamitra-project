import React from "react";
import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div style={{
      width:"200px",
      height:"100vh",
      background:"#2c3e50",
      color:"white",
      padding:"20px"
    }}>
      <h3>DrishyaMitra</h3>

      <p><Link to="/dashboard" style={{color:"white"}}>Dashboard</Link></p>
      <p><Link to="/upload" style={{color:"white"}}>Upload</Link></p>
      <p><Link to="/gallery" style={{color:"white"}}>Gallery</Link></p>
      <p><Link to="/chat" style={{color:"white"}}>AI Chat</Link></p>
    </div>
  );
}

export default Sidebar;