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
  yoga: {
    background: 'rgba(0, 0, 0, 0.3)',
    padding: '15px',
    borderRadius: '10px',
    marginBottom: '12px',
    border: '1px solid rgba(255, 215, 0, 0.15)',
  },
  yogaName: {
    color: '#ffd700',
    fontWeight: 'bold',
    fontSize: '1.1rem',
  },
  yogaStrength: {
    background: 'rgba(255, 215, 0, 0.2)',
    padding: '3px 10px',
    borderRadius: '15px',
    fontSize: '0.8rem',
    color: '#ffd700',
    marginLeft: '10px',
  },
  description: {
    color: '#ccc',
    marginTop: '8px',
    lineHeight: '1.5',
  },
  noYogas: {
    color: '#888',
    textAlign: 'center',
    padding: '20px',
  },
};

function YogaList({ yogas }) {
  if (!yogas) return null;
  
  // Handle different response formats:
  // 1. yogas.all_yogas - array from our API
  // 2. yogas.detected_yogas - alternative format
  // 3. yogas itself if it's an array
  // 4. If yogas.yogas is a dict (grouped by category), flatten it
  let yogaList = [];
  
  if (yogas.all_yogas && Array.isArray(yogas.all_yogas)) {
    yogaList = yogas.all_yogas;
  } else if (yogas.detected_yogas && Array.isArray(yogas.detected_yogas)) {
    yogaList = yogas.detected_yogas;
  } else if (Array.isArray(yogas)) {
    yogaList = yogas;
  } else if (yogas.yogas && typeof yogas.yogas === 'object') {
    // yogas.yogas is a dictionary grouped by category - flatten it
    yogaList = Object.values(yogas.yogas).flat();
  }
  
  // Filter to only show present yogas
  yogaList = yogaList.filter(y => y.is_present !== false);

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>✨ Detected Yogas</h2>
      {yogaList.length === 0 ? (
        <div style={styles.noYogas}>No yogas detected</div>
      ) : (
        yogaList.map((y, i) => (
          <div key={i} style={styles.yoga}>
            <div>
              <span style={styles.yogaName}>{y.name || y.yoga_name}</span>
              {y.strength && <span style={styles.yogaStrength}>{y.strength}</span>}
            </div>
            <div style={styles.description}>
              {y.description || y.effects || y.notes || 'Auspicious yoga present in chart'}
            </div>
          </div>
        ))
      )}
    </div>
  );
}

export default YogaList;
