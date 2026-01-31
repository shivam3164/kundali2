import React, { useState } from 'react';

const styles = {
  container: {
    background: 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)',
    borderRadius: '15px',
    padding: '25px',
    marginTop: '20px',
    boxShadow: '0 10px 40px rgba(0, 0, 0, 0.3)',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '20px',
  },
  title: {
    color: '#ffd700',
    fontSize: '1.5rem',
    margin: 0,
  },
  summaryGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
    gap: '15px',
    marginBottom: '25px',
  },
  summaryCard: {
    background: 'rgba(255, 255, 255, 0.05)',
    borderRadius: '10px',
    padding: '15px',
    textAlign: 'center',
  },
  summaryLabel: {
    color: '#888',
    fontSize: '0.85rem',
    marginBottom: '5px',
  },
  summaryValue: {
    color: '#ffd700',
    fontSize: '1.2rem',
    fontWeight: 'bold',
  },
  lifeAreasGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
    gap: '12px',
    marginBottom: '25px',
  },
  lifeAreaCard: {
    background: 'rgba(255, 255, 255, 0.03)',
    borderRadius: '8px',
    padding: '12px',
    borderLeft: '3px solid',
  },
  lifeAreaName: {
    color: '#fff',
    fontSize: '0.9rem',
    marginBottom: '4px',
    textTransform: 'capitalize',
  },
  lifeAreaOutlook: {
    fontSize: '0.85rem',
    fontWeight: 'bold',
  },
  lifeAreaStrength: {
    color: '#888',
    fontSize: '0.75rem',
  },
  housesGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))',
    gap: '15px',
  },
  houseCard: {
    background: 'rgba(255, 255, 255, 0.03)',
    borderRadius: '12px',
    padding: '15px',
    border: '1px solid rgba(255, 255, 255, 0.1)',
    cursor: 'pointer',
    transition: 'all 0.3s ease',
  },
  houseCardExpanded: {
    background: 'rgba(255, 215, 0, 0.05)',
    border: '1px solid rgba(255, 215, 0, 0.3)',
  },
  houseHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: '10px',
  },
  houseNumber: {
    background: 'linear-gradient(135deg, #ffd700 0%, #ff8c00 100%)',
    color: '#000',
    width: '35px',
    height: '35px',
    borderRadius: '50%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontWeight: 'bold',
    fontSize: '1rem',
  },
  houseInfo: {
    flex: 1,
    marginLeft: '12px',
  },
  houseName: {
    color: '#ffd700',
    fontSize: '1rem',
    margin: 0,
  },
  houseSubtitle: {
    color: '#888',
    fontSize: '0.8rem',
  },
  strengthBadge: {
    padding: '4px 10px',
    borderRadius: '20px',
    fontSize: '0.75rem',
    fontWeight: 'bold',
  },
  houseBasics: {
    display: 'grid',
    gridTemplateColumns: 'repeat(3, 1fr)',
    gap: '8px',
    marginBottom: '10px',
    padding: '10px',
    background: 'rgba(0, 0, 0, 0.2)',
    borderRadius: '8px',
  },
  basicItem: {
    textAlign: 'center',
  },
  basicLabel: {
    color: '#666',
    fontSize: '0.7rem',
    display: 'block',
  },
  basicValue: {
    color: '#fff',
    fontSize: '0.85rem',
  },
  expandedContent: {
    marginTop: '15px',
    paddingTop: '15px',
    borderTop: '1px solid rgba(255, 255, 255, 0.1)',
  },
  section: {
    marginBottom: '15px',
  },
  sectionTitle: {
    color: '#ffd700',
    fontSize: '0.85rem',
    marginBottom: '8px',
    display: 'flex',
    alignItems: 'center',
    gap: '5px',
  },
  significationsList: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '6px',
  },
  tag: {
    background: 'rgba(255, 215, 0, 0.1)',
    color: '#ffd700',
    padding: '3px 8px',
    borderRadius: '4px',
    fontSize: '0.75rem',
  },
  interpretationText: {
    color: '#ccc',
    fontSize: '0.85rem',
    lineHeight: '1.5',
    marginBottom: '8px',
  },
  bphsEffect: {
    background: 'rgba(255, 215, 0, 0.08)',
    borderLeft: '3px solid #ffd700',
    padding: '10px',
    borderRadius: '0 8px 8px 0',
    marginBottom: '10px',
  },
  bphsText: {
    color: '#fff',
    fontSize: '0.85rem',
    fontStyle: 'italic',
  },
  bphsSource: {
    color: '#888',
    fontSize: '0.7rem',
    marginTop: '5px',
  },
  planetEffect: {
    background: 'rgba(100, 100, 255, 0.1)',
    borderRadius: '8px',
    padding: '10px',
    marginBottom: '8px',
  },
  planetName: {
    color: '#64b5f6',
    fontWeight: 'bold',
    fontSize: '0.9rem',
  },
  planetDetails: {
    color: '#aaa',
    fontSize: '0.8rem',
    marginTop: '4px',
  },
  resultsList: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '5px',
    marginTop: '6px',
  },
  positiveTag: {
    background: 'rgba(76, 175, 80, 0.2)',
    color: '#81c784',
    padding: '2px 6px',
    borderRadius: '3px',
    fontSize: '0.7rem',
  },
  negativeTag: {
    background: 'rgba(244, 67, 54, 0.2)',
    color: '#e57373',
    padding: '2px 6px',
    borderRadius: '3px',
    fontSize: '0.7rem',
  },
  remediesSection: {
    background: 'rgba(156, 39, 176, 0.1)',
    borderRadius: '8px',
    padding: '10px',
  },
  remedyItem: {
    color: '#ce93d8',
    fontSize: '0.8rem',
    marginBottom: '4px',
    paddingLeft: '15px',
    position: 'relative',
  },
  noData: {
    textAlign: 'center',
    color: '#666',
    padding: '40px',
  },
};

const getStrengthColor = (level) => {
  switch (level) {
    case 'Very Strong': return '#4caf50';
    case 'Strong': return '#8bc34a';
    case 'Average': return '#ffc107';
    case 'Weak': return '#ff9800';
    case 'Very Weak': return '#f44336';
    default: return '#888';
  }
};

const getOutlookColor = (outlook) => {
  switch (outlook) {
    case 'Very Favorable': return '#4caf50';
    case 'Favorable': return '#8bc34a';
    case 'Mixed': return '#ffc107';
    case 'Challenging': return '#f44336';
    default: return '#888';
  }
};

const HouseCard = ({ house, isExpanded, onToggle }) => {
  const strengthColor = getStrengthColor(house.strength?.level);
  
  return (
    <div 
      style={{
        ...styles.houseCard,
        ...(isExpanded ? styles.houseCardExpanded : {})
      }}
      onClick={onToggle}
    >
      <div style={styles.houseHeader}>
        <div style={styles.houseNumber}>{house.house_number}</div>
        <div style={styles.houseInfo}>
          <h4 style={styles.houseName}>{house.name}</h4>
          <span style={styles.houseSubtitle}>{house.english_name}</span>
        </div>
        <span style={{
          ...styles.strengthBadge,
          background: `${strengthColor}20`,
          color: strengthColor,
        }}>
          {house.strength?.percentage}%
        </span>
      </div>
      
      <div style={styles.houseBasics}>
        <div style={styles.basicItem}>
          <span style={styles.basicLabel}>Sign</span>
          <span style={styles.basicValue}>{house.sign}</span>
        </div>
        <div style={styles.basicItem}>
          <span style={styles.basicLabel}>Lord</span>
          <span style={styles.basicValue}>{house.lord}</span>
        </div>
        <div style={styles.basicItem}>
          <span style={styles.basicLabel}>Lord in</span>
          <span style={styles.basicValue}>H{house.lord_house}</span>
        </div>
      </div>
      
      {house.planets_in_house?.length > 0 && (
        <div style={{ color: '#64b5f6', fontSize: '0.8rem', marginBottom: '8px' }}>
          🪐 Planets: {house.planets_in_house.join(', ')}
        </div>
      )}
      
      {isExpanded && (
        <div style={styles.expandedContent}>
          {/* Significations */}
          <div style={styles.section}>
            <div style={styles.sectionTitle}>📋 Significations</div>
            <div style={styles.significationsList}>
              {house.significations?.primary?.map((sig, i) => (
                <span key={i} style={styles.tag}>{sig}</span>
              ))}
            </div>
            <p style={{ ...styles.interpretationText, marginTop: '8px' }}>
              {house.significations?.represents}
            </p>
          </div>
          
          {/* BPHS Lord Effect */}
          <div style={styles.section}>
            <div style={styles.sectionTitle}>📜 BPHS Lord Placement Effect</div>
            <div style={styles.bphsEffect}>
              <div style={styles.bphsText}>
                "{house.lord_analysis?.bphs_effect}"
              </div>
              <div style={styles.bphsSource}>
                — {house.lord_analysis?.source}
              </div>
            </div>
            {house.lord_analysis?.notes?.map((note, i) => (
              <p key={i} style={{ color: '#aaa', fontSize: '0.8rem', margin: '4px 0' }}>
                • {note}
              </p>
            ))}
          </div>
          
          {/* Planet Effects */}
          {house.planet_effects?.length > 0 && (
            <div style={styles.section}>
              <div style={styles.sectionTitle}>🪐 Planet Effects</div>
              {house.planet_effects.map((effect, i) => (
                <div key={i} style={styles.planetEffect}>
                  <span style={styles.planetName}>{effect.planet}</span>
                  <span style={{ color: '#888', fontSize: '0.75rem', marginLeft: '8px' }}>
                    ({effect.dignity}{effect.is_retrograde ? ', Retrograde' : ''})
                  </span>
                  <p style={styles.planetDetails}>{effect.effect}</p>
                  <div style={styles.resultsList}>
                    {effect.positive_results?.map((r, j) => (
                      <span key={j} style={styles.positiveTag}>✓ {r}</span>
                    ))}
                    {effect.negative_results?.map((r, j) => (
                      <span key={j} style={styles.negativeTag}>⚠ {r}</span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          )}
          
          {/* Interpretation */}
          <div style={styles.section}>
            <div style={styles.sectionTitle}>🔮 Interpretation</div>
            <p style={styles.interpretationText}>{house.interpretation?.overview}</p>
            <p style={styles.interpretationText}>{house.interpretation?.strength_assessment}</p>
            <p style={styles.interpretationText}>{house.interpretation?.lord_effect}</p>
          </div>
          
          {/* Remedies */}
          {house.remedies?.recommended?.length > 0 && (
            <div style={styles.section}>
              <div style={styles.sectionTitle}>💎 Remedies ({house.remedies?.required_level} priority)</div>
              <div style={styles.remediesSection}>
                {house.remedies.recommended.map((remedy, i) => (
                  <div key={i} style={styles.remedyItem}>• {remedy}</div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
      
      <div style={{ textAlign: 'center', color: '#666', fontSize: '0.75rem', marginTop: '8px' }}>
        {isExpanded ? '▲ Click to collapse' : '▼ Click to expand'}
      </div>
    </div>
  );
};

function HouseInterpretation({ houseData }) {
  const [expandedHouse, setExpandedHouse] = useState(null);
  
  if (!houseData?.data) {
    return (
      <div style={styles.container}>
        <h3 style={styles.title}>🏠 House Interpretations</h3>
        <div style={styles.noData}>No house data available</div>
      </div>
    );
  }
  
  const { houses, summary, life_areas_summary } = houseData.data;
  
  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h3 style={styles.title}>🏠 House Interpretations (BPHS)</h3>
      </div>
      
      {/* Summary Cards */}
      <div style={styles.summaryGrid}>
        <div style={styles.summaryCard}>
          <div style={styles.summaryLabel}>Strongest Houses</div>
          <div style={styles.summaryValue}>
            {summary?.strongest_houses?.join(', ')}
          </div>
        </div>
        <div style={styles.summaryCard}>
          <div style={styles.summaryLabel}>Weakest Houses</div>
          <div style={styles.summaryValue}>
            {summary?.weakest_houses?.join(', ')}
          </div>
        </div>
        <div style={styles.summaryCard}>
          <div style={styles.summaryLabel}>Kendra Strength</div>
          <div style={styles.summaryValue}>{summary?.kendra_strength}</div>
        </div>
        <div style={styles.summaryCard}>
          <div style={styles.summaryLabel}>Trikona Strength</div>
          <div style={styles.summaryValue}>{summary?.trikona_strength}</div>
        </div>
      </div>
      
      {/* Life Areas */}
      <h4 style={{ color: '#ffd700', marginBottom: '12px', fontSize: '1.1rem' }}>
        📊 Life Areas Overview
      </h4>
      <div style={styles.lifeAreasGrid}>
        {life_areas_summary && Object.entries(life_areas_summary).map(([key, area]) => (
          <div 
            key={key} 
            style={{
              ...styles.lifeAreaCard,
              borderColor: getOutlookColor(area.outlook),
            }}
          >
            <div style={styles.lifeAreaName}>
              {key.replace(/_/g, ' ')}
            </div>
            <div style={{
              ...styles.lifeAreaOutlook,
              color: getOutlookColor(area.outlook),
            }}>
              {area.outlook}
            </div>
            <div style={styles.lifeAreaStrength}>
              {area.average_strength}% • Houses {area.relevant_houses.join(', ')}
            </div>
          </div>
        ))}
      </div>
      
      {/* House Cards */}
      <h4 style={{ color: '#ffd700', marginBottom: '15px', marginTop: '25px', fontSize: '1.1rem' }}>
        🏛️ All 12 Houses (Click to expand)
      </h4>
      <div style={styles.housesGrid}>
        {houses && Object.values(houses).map((house) => (
          <HouseCard
            key={house.house_number}
            house={house}
            isExpanded={expandedHouse === house.house_number}
            onToggle={() => setExpandedHouse(
              expandedHouse === house.house_number ? null : house.house_number
            )}
          />
        ))}
      </div>
    </div>
  );
}

export default HouseInterpretation;
