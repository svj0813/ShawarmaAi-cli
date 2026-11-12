import { useState } from 'react'
import './App.css'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    const chatHistory = [...messages, userMessage];
    
    setMessages(chatHistory);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:8000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: userMessage.content,
          history: messages 
        }),
      });

      const data = await response.json();
      setMessages([...chatHistory, { role: 'assistant', content: data.response }]);
    } catch (error) {
      console.error("Backend connection error:", error);
      setMessages([...chatHistory, { role: 'assistant', content: "Error connecting to backend. Is uvicorn running?" }]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px', fontFamily: 'sans-serif' }}>
      <h2>Shawarma Web AI 🌯</h2>
      
      <div style={{ height: '400px', overflowY: 'auto', border: '1px solid #ccc', padding: '10px', marginBottom: '10px', borderRadius: '8px' }}>
        {messages.map((msg, index) => (
          <div key={index} style={{ textAlign: msg.role === 'user' ? 'right' : 'left', margin: '10px 0' }}>
            <span style={{ 
              background: msg.role === 'user' ? '#007bff' : '#f1f1f1', 
              color: msg.role === 'user' ? 'white' : 'black',
              padding: '8px 12px', 
              borderRadius: '15px', 
              display: 'inline-block',
              maxWidth: '80%'
            }}>
              {msg.content}
            </span>
          </div>
        ))}
        {loading && <div style={{ textAlign: 'left', color: '#888' }}>Shawarma is thinking...</div>}
      </div>

      <div style={{ display: 'flex', gap: '10px' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Ask Shawarma something..."
          style={{ flexGrow: 1, padding: '10px', borderRadius: '4px', border: '1px solid #ccc' }}
        />
        <button 
          onClick={sendMessage} 
          disabled={loading}
          style={{ padding: '10px 20px', cursor: 'pointer', borderRadius: '4px', border: 'none', background: '#28a745', color: 'white' }}
        >
          Send
        </button>
      </div>
    </div>
  )
}

export default App