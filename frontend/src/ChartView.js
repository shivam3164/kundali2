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
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
    gap: '15px',
  },
  planet: {
    background: 'rgba(0, 0, 0, 0.3)',
    padding: '15px',
    borderRadius: '10px',
    border: '1px solid rgba(255, 215, 0, 0.15)',
  },
  planetName: {
    color: '#ffd700',
    fontWeight: 'bold',
    marginBottom: '8px',
  },
  detail: {
    color: '#ccc',
    fontSize: '0.9rem',
    lineHeight: '1.6',
  },
  lagna: {
    background: 'linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(255, 140, 0, 0.2))',
    padding: '20px',
    borderRadius: '10px',
    marginBottom: '20px',
    textAlign: 'center',
  },
};

function ChartView({ chart }) {
  if (!chart) return null;
  
  const planets = chart.planets || chart.planet_positions || [];
  const lagna = chart.lagna || chart.ascendant || {};

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🪐 Birth Chart (Rashi)</h2>
      
      {lagna && (
        <div style={styles.lagna}>
          <div style={{color: '#ffd700', fontSize: '1.1rem'}}>Lagna (Ascendant)</div>
          <div style={{color: '#fff', fontSize: '1.3rem', marginTop: '5px'}}>
            {lagna.sign || 'N/A'} {lagna.degree ? `${lagna.degree.toFixed(2)}°` : ''}
          </div>
          {lagna.nakshatra && <div style={{color: '#aaa', marginTop: '5px'}}>Nakshatra: {lagna.nakshatra}</div>}
        </div>
      )}

      <div style={styles.grid}>
        {Array.isArray(planets) ? planets.map((p, i) => (
          <div key={i} style={styles.planet}>
            <div style={styles.planetName}>{p.planet || p.name}</div>
            <div style={styles.detail}>
              <div>{p.sign} {p.degree ? `${p.degree.toFixed(2)}°` : ''}</div>
              <div>House: {p.house}</div>
              {p.nakshatra && <div>Nakshatra: {p.nakshatra}</div>}
              {p.retrograde && <div style={{color: '#ff6b6b'}}>⟲ Retrograde</div>}
            </div>
          </div>
        )) : (
          <pre style={{color: '#aaa', fontSize: '0.8rem'}}>{JSON.stringify(chart, null, 2)}</pre>
        )}
      </div>
    </div>
  );
}

export default ChartView;
