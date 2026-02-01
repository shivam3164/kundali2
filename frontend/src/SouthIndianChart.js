import React from 'react';

const styles = {
  container: {
    fontFamily: 'serif',
    maxWidth: '500px',
    margin: '0 auto',
    color: '#3e2723', // Dark brown for traditional look
    userSelect: 'none',
  },
  grid: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr 1fr 1fr',
    gridTemplateRows: '1fr 1fr 1fr 1fr',
    gap: '2px',
    background: '#8d6e63', // Border color
    border: '2px solid #5d4037',
    aspectRatio: '1 / 1',
  },
  cell: {
    background: '#fff3e0', // Light parchment
    padding: '4px',
    position: 'relative',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '80px',
    fontSize: '0.8rem',
  },
  center: {
    gridColumn: '2 / span 2',
    gridRow: '2 / span 2',
    background: '#fff3e0',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center',
    padding: '10px',
  },
  signName: {
    position: 'absolute',
    top: '2px',
    right: '2px',
    fontSize: '0.6rem',
    color: '#aaa',
    textTransform: 'uppercase',
  },
  planetList: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: '2px',
  },
  planet: {
    fontSize: '0.75rem',
    fontWeight: 'bold',
    color: '#000',
  },
  retrograde: {
    color: '#d32f2f', // Red for retrograde
  },
  ascendant: {
    color: '#d50000',
    fontWeight: '900',
    borderBottom: '1px solid #d50000',
  }
};

// Sign mapping for South Indian Chart (Fixed Layout)
// 0-11 indices (1-12 signs)
// Pis Ari Tau Gem
// Aqu         Can
// Cap         Leo
// Sag Sco Lib Vir

const SIGN_ORDER = [
  'Pisces', 'Aries', 'Taurus', 'Gemini',
  'Aquarius', null, null, 'Cancer',
  'Capricorn', null, null, 'Leo',
  'Sagittarius', 'Scorpio', 'Libra', 'Virgo'
];

const SIGN_NAMES_MAP = {
  'Aries': 'Mesh',
  'Taurus': 'Vrish',
  'Gemini': 'Mith',
  'Cancer': 'Kark',
  'Leo': 'Simha',
  'Virgo': 'Kanya',
  'Libra': 'Tula',
  'Scorpio': 'Vrishc',
  'Sagittarius': 'Dhanu',
  'Capricorn': 'Makar',
  'Aquarius': 'Kumbh',
  'Pisces': 'Meen'
};

const PLANET_ABBR = {
  'Sun': 'Su',
  'Moon': 'Mo',
  'Mars': 'Ma',
  'Mercury': 'Me',
  'Jupiter': 'Ju',
  'Venus': 'Ve',
  'Saturn': 'Sa',
  'Rahu': 'Ra',
  'Ketu': 'Ke',
  'Uranus': 'Ur',
  'Neptune': 'Ne',
  'Pluto': 'Pl',
  'Ascendant': 'Asc'
};

const SouthIndianChart = ({ chartData, title = "Rashi Chakra" }) => {
  if (!chartData) return null;

  const { planets, lagna } = chartData;
  
  // Group planets by sign
  const planetsBySign = {};
  
  // Initialize
  Object.keys(SIGN_NAMES_MAP).forEach(sign => {
    planetsBySign[sign] = [];
  });

  // Add Lagna (Ascendant)
  if (lagna && lagna.sign) {
     planetsBySign[lagna.sign].push({ 
       name: 'Ascendant', 
       isLagna: true 
     });
  }

  // Add Planets
  if (planets) {
    Object.entries(planets).forEach(([name, data]) => {
      if (planetsBySign[data.sign]) {
        planetsBySign[data.sign].push({
          name,
          ...data
        });
      }
    });
  }

  const renderCell = (signName, index) => {
    if (!signName) {
      if (index === 5) { // Center box (first of the nulls we hit in iteration)
         return (
           <div key="center" style={styles.center}>
             <h3 style={{ margin: 0, color: '#5d4037' }}>{title}</h3>
             <small>South Indian Style</small>
           </div>
         );
      }
      return null;
    }

    const planetsInSign = planetsBySign[signName] || [];

    return (
      <div key={signName} style={styles.cell}>
        <span style={styles.signName}>{SIGN_NAMES_MAP[signName]}</span>
        <div style={styles.planetList}>
          {planetsInSign.map((p, i) => (
            <span key={i} style={{
              ...styles.planet,
              ...(p.isRetrograde ? styles.retrograde : {}),
              ...(p.isLagna ? styles.ascendant : {})
            }}>
              {PLANET_ABBR[p.name] || p.name.substring(0, 2)}
              {p.isRetrograde ? 'R' : ''}
              {i < planetsInSign.length - 1 ? ',' : ''}&nbsp;
            </span>
          ))}
        </div>
      </div>
    );
  };

  return (
    <div style={styles.container}>
      <div style={styles.grid}>
        {SIGN_ORDER.map((sign, i) => renderCell(sign, i))}
      </div>
    </div>
  );
};

export default SouthIndianChart;
