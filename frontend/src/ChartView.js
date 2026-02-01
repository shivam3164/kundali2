import React, { useState } from 'react';
import SouthIndianChart from './SouthIndianChart';

const styles = {
  container: {
    background: 'rgba(255, 255, 255, 0.05)',
    padding: '25px',
    borderRadius: '15px',
    border: '1px solid rgba(255, 215, 0, 0.2)',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '20px',
  },
  title: {
    color: '#ffd700',
    fontSize: '1.3rem',
    margin: 0,
  },
  controls: {
    display: 'flex',
    gap: '10px',
  },
  button: {
    background: 'rgba(255, 215, 0, 0.1)',
    border: '1px solid rgba(255, 215, 0, 0.3)',
    color: '#ffd700',
    padding: '5px 10px',
    borderRadius: '5px',
    cursor: 'pointer',
    fontSize: '0.8rem',
  },
  activeButton: {
    background: 'rgba(255, 215, 0, 0.3)',
    fontWeight: 'bold',
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
};

function ChartView({ chart }) {
  const [viewMode, setViewMode] = useState('visual'); // 'visual' or 'list'

  if (!chart) return null;
  
  const planets = chart.planets || chart.planet_positions || {};
  
  // Transform planets to list format for the "List" view
  let planetList = [];
  if (Array.isArray(planets)) {
    planetList = planets;
  } else {
    planetList = Object.entries(planets).map(([key, value]) => ({
      name: key,
      ...value
    }));
  }

  const lagna = chart.lagna || chart.ascendant || {};

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h2 style={styles.title}>✨ Birth Chart (Rashi Chakra)</h2>
        <div style={styles.controls}>
          <button 
            style={{...styles.button, ...(viewMode === 'visual' ? styles.activeButton : {})}}
            onClick={() => setViewMode('visual')}
          >
            Visual
          </button>
          <button 
            style={{...styles.button, ...(viewMode === 'list' ? styles.activeButton : {})}}
            onClick={() => setViewMode('list')}
          >
            List
          </button>
        </div>
      </div>

      {viewMode === 'visual' ? (
        <SouthIndianChart chartData={chart} />
      ) : (
        <div style={styles.grid}>
          {/* Lagna Info if in list mode */}
          {lagna && (
             <div style={styles.planet} key="lagna">
               <div style={styles.planetName}>Ascendant (Lagna)</div>
               <div style={styles.detail}>Sign: {lagna.sign}</div>
               <div style={styles.detail}>Longitude: {lagna.longitude ? lagna.longitude.toFixed(2) : lagna.degree}°</div>
               <div style={styles.detail}>Nakshatra: {lagna.nakshatra}</div>
             </div>
          )}

          {planetList.map((planet, i) => (
            <div key={i} style={styles.planet}>
              <div style={styles.planetName}>{planet.name || planet.planet}</div>
              <div style={styles.detail}>Sign: {planet.sign}</div>
              <div style={styles.detail}>
                 Longitude: {typeof planet.longitude === 'number' ? planet.longitude.toFixed(2) : (planet.degree || '0')}°
              </div>
              <div style={styles.detail}>House: {planet.house}</div>
              <div style={styles.detail}>Nakshatra: {planet.nakshatra}</div>
              {(planet.is_retrograde || planet.retrograde) && <div style={{color: '#ff6b6b'}}>Retrograde</div>}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default ChartView;
