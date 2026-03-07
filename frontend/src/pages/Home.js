import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div style={{textAlign:"center", marginTop:"100px"}}>
      <h1>DrishyaMitra</h1>
      <p>Your AI Powered Photo Assistant</p>

      <Link to="/login">
        <button>Login</button>
      </Link>

      <Link to="/register">
        <button>Sign Up</button>
      </Link>
    </div>
  );
}

export default Home;