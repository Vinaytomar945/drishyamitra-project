import React, {useState} from "react";
import Sidebar from "../components/Sidebar";

function Chat(){

 const [message,setMessage] = useState("");
 const [response,setResponse] = useState("");

 const sendMessage = () => {

  fetch("http://localhost:5000/chat/chat",{

    method:"POST",
    headers:{
      "Content-Type":"application/json"
    },

    body:JSON.stringify({message})

  })
  .then(res => res.json())
  .then(data => setResponse(data.ai_response))

 };

 return(

  <div style={{display:"flex"}}>

  <Sidebar />

  <div style={{padding:"30px"}}>

  <h2>AI Chat Assistant</h2>

  <input
  value={message}
  onChange={(e)=>setMessage(e.target.value)}
  placeholder="Type message..."
  />

  <button onClick={sendMessage}>Send</button>

  <p>{response}</p>

  </div>

  </div>

 );

}

export default Chat;