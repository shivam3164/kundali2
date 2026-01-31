import React, { useState } from 'react';

function ChatBox({ onAsk, responses }) {
  const [question, setQuestion] = useState('');
  const handleSubmit = e => {
    e.preventDefault();
    onAsk(question);
    setQuestion('');
  };
  return (
    <div>
      <h2>Ask About Your Kundali</h2>
      <form onSubmit={handleSubmit}>
        <input value={question} onChange={e => setQuestion(e.target.value)} placeholder="Type your question..." />
        <button type="submit">Ask</button>
      </form>
      <div>
        {responses.map((r, i) => (
          <div key={i}><strong>Q:</strong> {r.q}<br /><strong>A:</strong> {r.a}</div>
        ))}
      </div>
    </div>
  );
}

export default ChatBox;
