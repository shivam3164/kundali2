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
  current: {
    background: 'linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(255, 140, 0, 0.2))',
    padding: '20px',
    borderRadius: '10px',
    marginBottom: '20px',
  },
  currentLabel: {
    color: '#ffd700',
    fontSize: '0.9rem',
    marginBottom: '5px',
  },
  currentPlanet: {
    color: '#fff',
    fontSize: '1.3rem',
    fontWeight: 'bold',
  },
  timeline: {
    display: 'flex',
    flexDirection: 'column',
    gap: '8px',
  },
  dasha: {
    display: 'flex',
    alignItems: 'center',
    padding: '12px 15px',
    background: 'rgba(0, 0, 0, 0.3)',
    borderRadius: '8px',
    border: '1px solid rgba(255, 215, 0, 0.1)',
  },
  planet: {
    color: '#ffd700',
    fontWeight: 'bold',
    width: '80px',
  },
  dates: {
    color: '#aaa',
    flex: 1,
    fontSize: '0.9rem',
  },
  years: {
    color: '#888',
    fontSize: '0.85rem',
  },
};

function DashaTimeline({ dashas }) {
  if (!dashas) return null;
  
  const dashaList = dashas.mahadashas || dashas.dashas || (Array.isArray(dashas) ? dashas : []);
  const currentDasha = dashas.current_mahadasha || dashas.current;

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>📅 Vimshottari Dasha</h2>
      
      {currentDasha && (
        <div style={styles.current}>
          <div style={styles.currentLabel}>Current Mahadasha</div>
          <div style={styles.currentPlanet}>
            {currentDasha.planet || currentDasha.lord || currentDasha}
          </div>
          {currentDasha.start_date && currentDasha.end_date && (
            <div style={{color: '#aaa', marginTop: '5px', fontSize: '0.9rem'}}>
              {currentDasha.start_date} → {currentDasha.end_date}
            </div>
          )}
        </div>
      )}

      <div style={styles.timeline}>
        {dashaList.slice(0, 9).map((d, i) => (
          <div key={i} style={styles.dasha}>
            <span style={styles.planet}>{d.planet || d.lord}</span>
            <span style={styles.dates}>
              {d.start_date || d.start} → {d.end_date || d.end}
            </span>
            <span style={styles.years}>
              {d.years ? `${d.years.toFixed(1)}y` : d.duration || ''}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DashaTimeline;
