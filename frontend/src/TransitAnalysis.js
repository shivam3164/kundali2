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
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: '20px',
    borderBottom: '1px solid rgba(255, 215, 0, 0.2)',
    paddingBottom: '15px',
  },
  title: {
    color: '#ffd700',
    fontSize: '1.5rem',
    margin: 0,
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
  },
  subtitle: {
    color: '#888',
    fontSize: '0.9rem',
    marginTop: '5px',
  },
  dateSelector: {
    display: 'flex',
    gap: '10px',
    alignItems: 'center',
  },
  dateInput: {
    background: 'rgba(255, 255, 255, 0.1)',
    border: '1px solid rgba(255, 215, 0, 0.3)',
    borderRadius: '8px',
    padding: '8px 12px',
    color: '#fff',
    fontSize: '0.9rem',
  },
  analyzeBtn: {
    background: 'linear-gradient(135deg, #ffd700 0%, #ff8c00 100%)',
    border: 'none',
    borderRadius: '8px',
    padding: '8px 20px',
    color: '#000',
    fontWeight: 'bold',
    cursor: 'pointer',
    transition: 'transform 0.2s',
  },
  summary: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
    gap: '15px',
    marginBottom: '25px',
  },
  summaryCard: {
    background: 'rgba(255, 255, 255, 0.05)',
    borderRadius: '10px',
    padding: '15px',
    textAlign: 'center',
  },
  summaryValue: {
    fontSize: '2rem',
    fontWeight: 'bold',
    marginBottom: '5px',
  },
  summaryLabel: {
    color: '#888',
    fontSize: '0.85rem',
  },
  planetGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
    gap: '15px',
  },
  planetCard: {
    background: 'rgba(255, 255, 255, 0.05)',
    borderRadius: '12px',
    padding: '15px',
    border: '1px solid rgba(255, 255, 255, 0.1)',
    transition: 'transform 0.2s, box-shadow 0.2s',
  },
  planetHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '10px',
  },
  planetName: {
    fontSize: '1.1rem',
    fontWeight: 'bold',
    color: '#fff',
  },
  statusBadge: {
    padding: '4px 10px',
    borderRadius: '20px',
    fontSize: '0.75rem',
    fontWeight: 'bold',
    textTransform: 'uppercase',
  },
  planetDetails: {
    fontSize: '0.85rem',
    color: '#aaa',
    lineHeight: '1.6',
  },
  detailRow: {
    display: 'flex',
    justifyContent: 'space-between',
    marginBottom: '5px',
  },
  detailLabel: {
    color: '#888',
  },
  detailValue: {
    color: '#fff',
  },
  prediction: {
    marginTop: '10px',
    padding: '10px',
    background: 'rgba(0, 0, 0, 0.2)',
    borderRadius: '8px',
    fontSize: '0.85rem',
    color: '#ccc',
    lineHeight: '1.5',
  },
  vedhaWarning: {
    marginTop: '8px',
    padding: '8px',
    background: 'rgba(255, 107, 107, 0.2)',
    borderRadius: '6px',
    color: '#ff6b6b',
    fontSize: '0.8rem',
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
  },
  taraInfo: {
    marginTop: '8px',
    padding: '8px',
    background: 'rgba(100, 100, 255, 0.1)',
    borderRadius: '6px',
    fontSize: '0.8rem',
    display: 'flex',
    justifyContent: 'space-between',
  },
  loading: {
    textAlign: 'center',
    padding: '40px',
    color: '#ffd700',
  },
  error: {
    background: 'rgba(255, 107, 107, 0.2)',
    color: '#ff6b6b',
    padding: '15px',
    borderRadius: '10px',
    marginBottom: '20px',
  },
  legend: {
    display: 'flex',
    gap: '15px',
    flexWrap: 'wrap',
    marginBottom: '20px',
    padding: '10px',
    background: 'rgba(0, 0, 0, 0.2)',
    borderRadius: '8px',
  },
  legendItem: {
    display: 'flex',
    alignItems: 'center',
    gap: '6px',
    fontSize: '0.8rem',
    color: '#aaa',
  },
  legendDot: {
    width: '12px',
    height: '12px',
    borderRadius: '50%',
  },
};

const getStatusColor = (status) => {
  switch (status) {
    case 'Good': return '#4ade80';
    case 'Bad': return '#f87171';
    case 'Obstructed': return '#fbbf24';
    default: return '#9ca3af';
  }
};

const getStatusBgColor = (status) => {
  switch (status) {
    case 'Good': return 'rgba(74, 222, 128, 0.2)';
    case 'Bad': return 'rgba(248, 113, 113, 0.2)';
    case 'Obstructed': return 'rgba(251, 191, 36, 0.2)';
    default: return 'rgba(156, 163, 175, 0.2)';
  }
};

const getPlanetEmoji = (planet) => {
  const emojis = {
    Sun: '☀️',
    Moon: '🌙',
    Mars: '🔴',
    Mercury: '💚',
    Jupiter: '🟡',
    Venus: '💖',
    Saturn: '🪐',
    Rahu: '🐍',
    Ketu: '🔥',
  };
  return emojis[planet] || '⭐';
};

const TransitAnalysis = ({ birthData }) => {
  const [transitData, setTransitData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [transitDate, setTransitDate] = useState(
    new Date().toISOString().split('T')[0]
  );

  const analyzeTransits = async () => {
    if (!birthData) {
      setError('Please calculate your birth chart first');
      return;
    }

    setLoading(true);
    setError(null);

    const [year, month, day] = transitDate.split('-').map(Number);

    try {
      const response = await fetch('/api/v1/transit/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          year: birthData.year,
          month: birthData.month,
          day: birthData.day,
          hour: birthData.hour,
          minute: birthData.minute,
          lat: birthData.lat,
          lon: birthData.lon,
          transit_year: year,
          transit_month: month,
          transit_day: day,
        }),
      });

      const result = await response.json();

      if (result.success) {
        setTransitData(result.data);
      } else {
        setError(result.error || 'Failed to analyze transits');
      }
    } catch (err) {
      setError('Failed to connect to server: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <div>
          <h2 style={styles.title}>
            🌟 Transit Analysis (Gochara)
          </h2>
          <p style={styles.subtitle}>
            Based on Vedic Astrology - BPHS + P.V.R. Narasimha Rao's methods
          </p>
        </div>
        <div style={styles.dateSelector}>
          <input
            type="date"
            value={transitDate}
            onChange={(e) => setTransitDate(e.target.value)}
            style={styles.dateInput}
          />
          <button
            onClick={analyzeTransits}
            style={styles.analyzeBtn}
            disabled={loading}
          >
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
        </div>
      </div>

      {error && <div style={styles.error}>❌ {error}</div>}

      {loading && (
        <div style={styles.loading}>
          ✨ Calculating planetary transits...
        </div>
      )}

      {transitData && !loading && (
        <>
          {/* Summary Cards */}
          <div style={styles.summary}>
            <div style={styles.summaryCard}>
              <div style={{ ...styles.summaryValue, color: '#4ade80' }}>
                {transitData.summary.favorable_transits}
              </div>
              <div style={styles.summaryLabel}>Favorable</div>
            </div>
            <div style={styles.summaryCard}>
              <div style={{ ...styles.summaryValue, color: '#f87171' }}>
                {transitData.summary.unfavorable_transits}
              </div>
              <div style={styles.summaryLabel}>Unfavorable</div>
            </div>
            <div style={styles.summaryCard}>
              <div style={{ ...styles.summaryValue, color: '#fbbf24' }}>
                {transitData.summary.obstructed_transits}
              </div>
              <div style={styles.summaryLabel}>Obstructed (Vedha)</div>
            </div>
            <div style={styles.summaryCard}>
              <div style={{ ...styles.summaryValue, color: '#60a5fa' }}>
                {transitData.summary.overall_assessment.split(' ')[0]}
              </div>
              <div style={styles.summaryLabel}>Overall Period</div>
            </div>
          </div>

          {/* Legend */}
          <div style={styles.legend}>
            <div style={styles.legendItem}>
              <div style={{ ...styles.legendDot, background: '#4ade80' }} />
              Good - Favorable transit
            </div>
            <div style={styles.legendItem}>
              <div style={{ ...styles.legendDot, background: '#f87171' }} />
              Bad - Unfavorable transit
            </div>
            <div style={styles.legendItem}>
              <div style={{ ...styles.legendDot, background: '#fbbf24' }} />
              Obstructed - Vedha blocks good results
            </div>
          </div>

          {/* Planet Cards */}
          <div style={styles.planetGrid}>
            {transitData.analysis_results.map((result) => (
              <div
                key={result.planet}
                style={{
                  ...styles.planetCard,
                  borderColor: getStatusColor(result.final_status),
                  borderWidth: '2px',
                }}
              >
                <div style={styles.planetHeader}>
                  <span style={styles.planetName}>
                    {getPlanetEmoji(result.planet)} {result.planet}
                  </span>
                  <span
                    style={{
                      ...styles.statusBadge,
                      background: getStatusBgColor(result.final_status),
                      color: getStatusColor(result.final_status),
                    }}
                  >
                    {result.final_status}
                  </span>
                </div>

                <div style={styles.planetDetails}>
                  <div style={styles.detailRow}>
                    <span style={styles.detailLabel}>Transit Sign:</span>
                    <span style={styles.detailValue}>
                      {result.transit_sign_name}
                    </span>
                  </div>
                  <div style={styles.detailRow}>
                    <span style={styles.detailLabel}>House from Moon:</span>
                    <span style={styles.detailValue}>
                      {result.house_from_moon}
                    </span>
                  </div>
                  <div style={styles.detailRow}>
                    <span style={styles.detailLabel}>Nakshatra:</span>
                    <span style={styles.detailValue}>
                      {result.transit_nakshatra_name}
                    </span>
                  </div>
                  <div style={styles.detailRow}>
                    <span style={styles.detailLabel}>Confidence:</span>
                    <span style={styles.detailValue}>{result.confidence}</span>
                  </div>
                </div>

                {/* Tara Info */}
                <div style={styles.taraInfo}>
                  <span>
                    🌟 Tara: <strong>{result.tara.tara_name}</strong>
                  </span>
                  <span
                    style={{
                      color:
                        result.tara.tara_quality === 'Good'
                          ? '#4ade80'
                          : result.tara.tara_quality === 'Bad'
                          ? '#f87171'
                          : '#fbbf24',
                    }}
                  >
                    ({result.tara.tara_quality})
                  </span>
                </div>

                {/* Vedha Warning */}
                {result.vedha.is_obstructed && (
                  <div style={styles.vedhaWarning}>
                    ⚠️ Vedha: Blocked by {result.vedha.obstructing_planet} in
                    house {result.vedha.vedha_house}
                  </div>
                )}

                {/* Prediction */}
                <div style={styles.prediction}>{result.final_prediction}</div>
              </div>
            ))}
          </div>

          {/* Footer Info */}
          <div
            style={{
              marginTop: '20px',
              padding: '15px',
              background: 'rgba(0, 0, 0, 0.2)',
              borderRadius: '10px',
              fontSize: '0.85rem',
              color: '#888',
            }}
          >
            <strong>Natal Moon:</strong> {transitData.natal_moon_sign} |{' '}
            <strong>Nakshatra:</strong> {transitData.natal_moon_nakshatra} |{' '}
            <strong>Transit Date:</strong> {transitData.transit_date}
          </div>
        </>
      )}

      {!transitData && !loading && !error && (
        <div style={{ textAlign: 'center', color: '#888', padding: '40px' }}>
          Select a date and click "Analyze" to see planetary transits
        </div>
      )}
    </div>
  );
};

export default TransitAnalysis;
