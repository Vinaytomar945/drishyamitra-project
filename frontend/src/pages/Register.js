import React from "react";

function Register() {
  return (
    <div style={{textAlign:"center", marginTop:"100px"}}>
      <h2>Register Page</h2>

      <input placeholder="Email" />
      <br /><br />

      <input placeholder="Username" />
      <br /><br />

      <input type="password" placeholder="Password"/>
      <br /><br />

      <button>Sign Up</button>
    </div>
  );
}

export default Register;