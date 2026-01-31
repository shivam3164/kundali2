import React from 'react';

const styles = {
  container: {
    background: 'rgba(255, 255, 255, 0.05)',
    padding: '25px',
    borderRadius: '15px',
    border: '1px solid rgba(255, 215, 0, 0.2)',
  },
  title: {
    color: '#ffd700',
    marginBottom: '20px',
    fontSize: '1.3rem',
  },
  section: {
    marginBottom: '20px',
  },
  sectionTitle: {
    color: '#ffd700',
    fontSize: '1.1rem',
    marginBottom: '10px',
    borderBottom: '1px solid rgba(255, 215, 0, 0.2)',
    paddingBottom: '5px',
  },
  text: {
    color: '#ccc',
    lineHeight: '1.7',
  },
  item: {
    background: 'rgba(0, 0, 0, 0.3)',
    padding: '15px',
    borderRadius: '10px',
    marginBottom: '10px',
  },
  category: {
    color: '#ffd700',
    fontWeight: 'bold',
    marginBottom: '5px',
  },
};

function Interpretations({ interpretations }) {
  if (!interpretations) return null;
  
  // Handle different response formats
  if (interpretations.summary) {
    return (
      <div style={styles.container}>
        <h2 style={styles.title}>📖 Chart Interpretation</h2>
        <div style={styles.section}>
          <div style={styles.text}>{interpretations.summary}</div>
        </div>
        {interpretations.strengths && (
          <div style={styles.section}>
            <div style={styles.sectionTitle}>Strengths</div>
            <div style={styles.text}>{interpretations.strengths}</div>
          </div>
        )}
        {interpretations.challenges && (
          <div style={styles.section}>
            <div style={styles.sectionTitle}>Areas for Growth</div>
            <div style={styles.text}>{interpretations.challenges}</div>
          </div>
        )}
      </div>
    );
  }

  const interpList = Array.isArray(interpretations) ? interpretations : 
                     interpretations.interpretations || [];

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>📖 Interpretations</h2>
      {interpList.map((interp, i) => (
        <div key={i} style={styles.item}>
          <div style={styles.category}>{interp.category || interp.area}</div>
          <div style={styles.text}>{interp.text || interp.interpretation}</div>
        </div>
      ))}
    </div>
  );
}

export default Interpretations;
