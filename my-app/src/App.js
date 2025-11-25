import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const sendMessage = async () => {
    if (!message) return;

    try {
      const res = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();
      setReply(data.reply);
    } catch (error) {
      setReply("Error: Could not reach server");
      console.error(error);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: "sans-serif" }}>
      <h2>AI Chatbot</h2>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message..."
        rows={4}
        style={{ width: "300px", padding: "10px" }}
      />
      <br />
      <br />
      <button onClick={sendMessage} style={{ padding: "8px 16px" }}>
        Send
      </button>
      <h3>Reply:</h3>
      <p>{reply}</p>
    </div>
  );
}

export default App;
