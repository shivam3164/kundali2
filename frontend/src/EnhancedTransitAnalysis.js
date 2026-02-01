import React, { useState } from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ReferenceLine,
  ResponsiveContainer,
  Area,
  ComposedChart,
} from 'recharts';

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
    flexWrap: 'wrap',
    gap: '10px',
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
  controls: {
    display: 'flex',
    gap: '10px',
    alignItems: 'center',
    flexWrap: 'wrap',
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
  tabs: {
    display: 'flex',
    gap: '10px',
    marginBottom: '20px',
    flexWrap: 'wrap',
  },
  tab: {
    padding: '10px 20px',
    borderRadius: '8px',
    border: 'none',
    cursor: 'pointer',
    fontSize: '0.9rem',
    transition: 'all 0.2s',
  },
  tabActive: {
    background: 'linear-gradient(135deg, #ffd700 0%, #ff8c00 100%)',
    color: '#000',
    fontWeight: 'bold',
  },
  tabInactive: {
    background: 'rgba(255, 255, 255, 0.1)',
    color: '#aaa',
  },
  summaryGrid: {
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
    gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
    gap: '15px',
  },
  planetCard: {
    background: 'rgba(255, 255, 255, 0.05)',
    borderRadius: '12px',
    padding: '15px',
    border: '2px solid rgba(255, 255, 255, 0.1)',
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
  detailRow: {
    display: 'flex',
    justifyContent: 'space-between',
    marginBottom: '5px',
    fontSize: '0.85rem',
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
  ashtakavargaInfo: {
    marginTop: '8px',
    padding: '8px',
    background: 'rgba(255, 215, 0, 0.1)',
    borderRadius: '6px',
    fontSize: '0.8rem',
  },
  specialNakshatraInfo: {
    marginTop: '8px',
    padding: '8px',
    background: 'rgba(147, 51, 234, 0.2)',
    borderRadius: '6px',
    fontSize: '0.8rem',
    color: '#c084fc',
  },
  lattaWarning: {
    marginTop: '8px',
    padding: '8px',
    background: 'rgba(251, 146, 60, 0.2)',
    borderRadius: '6px',
    color: '#fb923c',
    fontSize: '0.8rem',
  },
  // Area Analysis styles
  areaSection: {
    marginTop: '25px',
  },
  areaGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
    gap: '15px',
  },
  areaCard: {
    background: 'rgba(255, 255, 255, 0.05)',
    borderRadius: '12px',
    padding: '15px',
    cursor: 'pointer',
    transition: 'all 0.2s',
    border: '1px solid rgba(255, 255, 255, 0.1)',
  },
  areaCardHover: {
    transform: 'translateY(-2px)',
    boxShadow: '0 5px 20px rgba(0, 0, 0, 0.3)',
  },
  areaIcon: {
    fontSize: '2rem',
    marginBottom: '10px',
  },
  areaName: {
    color: '#fff',
    fontWeight: 'bold',
    marginBottom: '5px',
  },
  areaOutlook: {
    fontSize: '0.85rem',
    padding: '4px 8px',
    borderRadius: '4px',
    display: 'inline-block',
  },
  // Question section styles
  questionSection: {
    marginTop: '25px',
  },
  questionInput: {
    width: '100%',
    padding: '15px',
    background: 'rgba(255, 255, 255, 0.1)',
    border: '1px solid rgba(255, 215, 0, 0.3)',
    borderRadius: '10px',
    color: '#fff',
    fontSize: '1rem',
    marginBottom: '10px',
  },
  questionSuggestions: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '10px',
    marginBottom: '15px',
  },
  suggestionChip: {
    padding: '8px 15px',
    background: 'rgba(255, 255, 255, 0.1)',
    borderRadius: '20px',
    color: '#aaa',
    fontSize: '0.85rem',
    cursor: 'pointer',
    border: 'none',
    transition: 'all 0.2s',
  },
  answerBox: {
    background: 'rgba(0, 0, 0, 0.3)',
    borderRadius: '12px',
    padding: '20px',
    marginTop: '15px',
  },
  answerText: {
    color: '#fff',
    fontSize: '1rem',
    lineHeight: '1.6',
    marginBottom: '15px',
  },
  confidenceBadge: {
    padding: '5px 12px',
    borderRadius: '20px',
    fontSize: '0.8rem',
    fontWeight: 'bold',
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
  // Health Analysis styles
  healthSection: {
    marginTop: '25px',
  },
  healthGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: '15px',
  },
  healthCard: {
    background: 'rgba(255, 255, 255, 0.05)',
    borderRadius: '12px',
    padding: '15px',
    border: '1px solid rgba(255, 255, 255, 0.1)',
  },
  regionTitle: {
    color: '#ffd700',
    fontWeight: 'bold',
    marginBottom: '10px',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
  },
  bodyPartList: {
    fontSize: '0.85rem',
    color: '#aaa',
    listStyle: 'none',
    padding: 0,
    margin: 0,
  },
};

const getStatusColor = (status) => {
  switch (status) {
    case 'Good': return '#4ade80';
    case 'Bad': return '#f87171';
    case 'Obstructed': return '#fbbf24';
    case 'Positive': return '#4ade80';
    case 'Challenging': return '#f87171';
    default: return '#9ca3af';
  }
};

const getStatusBgColor = (status) => {
  switch (status) {
    case 'Good': return 'rgba(74, 222, 128, 0.2)';
    case 'Bad': return 'rgba(248, 113, 113, 0.2)';
    case 'Obstructed': return 'rgba(251, 191, 36, 0.2)';
    case 'Positive': return 'rgba(74, 222, 128, 0.2)';
    case 'Challenging': return 'rgba(248, 113, 113, 0.2)';
    default: return 'rgba(156, 163, 175, 0.2)';
  }
};

const getPlanetEmoji = (planet) => {
  const emojis = {
    Sun: '☀️', Moon: '🌙', Mars: '🔴', Mercury: '💚',
    Jupiter: '🟡', Venus: '💖', Saturn: '🪐', Rahu: '🐍', Ketu: '🔥',
  };
  return emojis[planet] || '⭐';
};

const EnhancedTransitAnalysis = ({ birthData }) => {
  const [transitData, setTransitData] = useState(null);
  const [enhancedData, setEnhancedData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('planets');
  const [transitDate, setTransitDate] = useState(new Date().toISOString().split('T')[0]);
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState(null);
  const [questionLoading, setQuestionLoading] = useState(false);
  // New: Timeline state
  const [timelineData, setTimelineData] = useState(null);
  const [timelineLoading, setTimelineLoading] = useState(false);
  const [selectedTimelineArea, setSelectedTimelineArea] = useState('career');

  const analyzeTransits = async (enhanced = false) => {
    if (!birthData) {
      setError('Please calculate your birth chart first');
      return;
    }

    setLoading(true);
    setError(null);

    const [year, month, day] = transitDate.split('-').map(Number);

    try {
      // Use enhanced endpoint
      const response = await fetch('/api/v1/transit/enhanced', {
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
        setEnhancedData(result);
        // Create compatible format for basic view
        setTransitData({
          natal_moon_sign: result.native_data.natal_moon_sign,
          natal_moon_nakshatra: result.native_data.natal_moon_nakshatra,
          transit_date: result.transit_date,
          analysis_results: result.planet_results,
          summary: result.overall_summary,
          favorable_planets: result.favorable_planets,
          unfavorable_planets: result.unfavorable_planets,
        });
      } else {
        setError(result.error || 'Failed to analyze transits');
      }
    } catch (err) {
      setError('Failed to connect to server: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  const askQuestion = async () => {
    if (!question.trim() || !birthData) return;

    setQuestionLoading(true);

    try {
      const response = await fetch('/api/v1/transit/ask', {
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
          question: question,
        }),
      });

      const result = await response.json();

      if (result.success) {
        setAnswer(result);
      } else {
        setError(result.error || 'Failed to process question');
      }
    } catch (err) {
      setError('Failed to connect to server: ' + err.message);
    } finally {
      setQuestionLoading(false);
    }
  };

  // New: Fetch 12-month timeline data
  const fetchTimeline = async (area = null) => {
    if (!birthData) {
      setError('Please calculate your birth chart first');
      return;
    }

    setTimelineLoading(true);

    try {
      const response = await fetch('/api/v1/transit/timeline', {
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
          area: area,
        }),
      });

      const result = await response.json();

      if (result.success) {
        setTimelineData(result);
      } else {
        setError(result.error || 'Failed to fetch timeline');
      }
    } catch (err) {
      setError('Failed to connect to server: ' + err.message);
    } finally {
      setTimelineLoading(false);
    }
  };

  const renderPlanetsTab = () => (
    <>
      {/* Summary Cards */}
      <div style={styles.summaryGrid}>
        <div style={styles.summaryCard}>
          <div style={{ ...styles.summaryValue, color: '#4ade80' }}>
            {enhancedData?.favorable_planets?.length || 0}
          </div>
          <div style={styles.summaryLabel}>Favorable</div>
        </div>
        <div style={styles.summaryCard}>
          <div style={{ ...styles.summaryValue, color: '#f87171' }}>
            {enhancedData?.unfavorable_planets?.length || 0}
          </div>
          <div style={styles.summaryLabel}>Unfavorable</div>
        </div>
        <div style={styles.summaryCard}>
          <div style={{ ...styles.summaryValue, color: '#60a5fa' }}>
            {enhancedData?.overall_summary?.average_score?.toFixed(1) || '0'}
          </div>
          <div style={styles.summaryLabel}>Avg Score</div>
        </div>
        <div style={styles.summaryCard}>
          <div style={{ ...styles.summaryValue, color: '#fbbf24' }}>
            {enhancedData?.ashtakavarga_summary?.overall_quality || '-'}
          </div>
          <div style={styles.summaryLabel}>Ashtakavarga</div>
        </div>
      </div>

      {/* Planet Cards */}
      <div style={styles.planetGrid}>
        {enhancedData?.planet_results?.map((result) => (
          <div
            key={result.planet}
            style={{
              ...styles.planetCard,
              borderColor: getStatusColor(result.final_status),
            }}
          >
            <div style={styles.planetHeader}>
              <span style={styles.planetName}>
                {getPlanetEmoji(result.planet)} {result.planet}
              </span>
              <span style={{
                ...styles.statusBadge,
                background: getStatusBgColor(result.final_status),
                color: getStatusColor(result.final_status),
              }}>
                {result.final_status}
              </span>
            </div>

            <div>
              <div style={styles.detailRow}>
                <span style={styles.detailLabel}>Transit Sign:</span>
                <span style={styles.detailValue}>{result.transit_sign}</span>
              </div>
              <div style={styles.detailRow}>
                <span style={styles.detailLabel}>House from Moon:</span>
                <span style={styles.detailValue}>{result.house_from_moon}</span>
              </div>
              <div style={styles.detailRow}>
                <span style={styles.detailLabel}>House from Lagna:</span>
                <span style={styles.detailValue}>{result.house_from_lagna}</span>
              </div>
              <div style={styles.detailRow}>
                <span style={styles.detailLabel}>Score:</span>
                <span style={{
                  ...styles.detailValue,
                  color: result.score >= 0 ? '#4ade80' : '#f87171'
                }}>
                  {result.score > 0 ? '+' : ''}{result.score}
                </span>
              </div>
            </div>

            {/* Tara Info */}
            {result.tara && (
              <div style={styles.taraInfo}>
                <span>🌟 Tara: <strong>{result.tara.tara_name}</strong></span>
                <span style={{ color: getStatusColor(result.tara.tara_quality === 'Good' ? 'Good' : 'Bad') }}>
                  ({result.tara.tara_quality})
                </span>
              </div>
            )}

            {/* Ashtakavarga Info */}
            {result.ashtakavarga && (
              <div style={styles.ashtakavargaInfo}>
                📊 BAV: <strong>{result.ashtakavarga.bav_score}</strong> bindus |
                Quality: <strong>{result.ashtakavarga.quality}</strong>
              </div>
            )}

            {/* Special Nakshatra */}
            {result.special_nakshatra?.is_special && (
              <div style={styles.specialNakshatraInfo}>
                ✨ Special: {result.special_nakshatra.name} ({result.special_nakshatra.quality})
              </div>
            )}

            {/* Latta Warning */}
            {result.latta && (
              <div style={styles.lattaWarning}>
                ⚡ Latta (Kick): {result.latta.planet} kicks your birth star
              </div>
            )}

            {/* Vedha Warning */}
            {result.vedha?.is_obstructed && (
              <div style={styles.vedhaWarning}>
                ⚠️ Vedha: Blocked by {result.vedha.obstructing_planet}
              </div>
            )}

            {/* Prediction */}
            <div style={styles.prediction}>{result.final_prediction}</div>
          </div>
        ))}
      </div>
    </>
  );

  const renderAreasTab = () => (
    <div style={styles.areaSection}>
      <h3 style={{ color: '#ffd700', marginBottom: '15px' }}>
        📊 Life Area Impacts
      </h3>
      <div style={styles.areaGrid}>
        {enhancedData?.area_impacts && Object.entries(enhancedData.area_impacts).map(([area, data]) => (
          <div
            key={area}
            style={{
              ...styles.areaCard,
              borderColor: getStatusColor(data.outlook),
            }}
          >
            <div style={styles.areaName}>
              {area.charAt(0).toUpperCase() + area.slice(1)}
            </div>
            <div style={{
              ...styles.areaOutlook,
              background: getStatusBgColor(data.outlook),
              color: getStatusColor(data.outlook),
            }}>
              {data.outlook}
            </div>
            <div style={{ marginTop: '10px', fontSize: '0.85rem', color: '#aaa' }}>
              Score: {data.score}
            </div>
            {data.influencing_planets?.length > 0 && (
              <div style={{ marginTop: '5px', fontSize: '0.8rem', color: '#888' }}>
                Key: {data.influencing_planets.map(p => p.planet).join(', ')}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );

  const renderHealthTab = () => (
    <div style={styles.healthSection}>
      <h3 style={{ color: '#ffd700', marginBottom: '15px' }}>
        ❤️ Health & Body Analysis
      </h3>
      
      {/* Latta Analysis */}
      {enhancedData?.latta_analysis && (
        <div style={{ marginBottom: '20px' }}>
          <h4 style={{ color: '#fb923c', marginBottom: '10px' }}>
            ⚡ Latta (Planetary Kicks) - Severity: {enhancedData.latta_analysis.severity}
          </h4>
          <div style={{ color: '#aaa', fontSize: '0.9rem', marginBottom: '10px' }}>
            {enhancedData.latta_analysis.interpretation}
          </div>
          {enhancedData.latta_analysis.latta_on_janma?.length > 0 && (
            <div style={{ color: '#fb923c', fontSize: '0.85rem' }}>
              Kicks on Birth Star: {enhancedData.latta_analysis.latta_on_janma.map(l => l.planet).join(', ')}
            </div>
          )}
        </div>
      )}

      {/* Health Risk */}
      {enhancedData?.health_analysis?.sensitive_transits && (
        <div style={styles.healthCard}>
          <div style={styles.regionTitle}>
            🏥 Health Risk Level: {enhancedData.health_analysis.sensitive_transits.health_risk_level}
          </div>
          {enhancedData.health_analysis.sensitive_transits.body_parts_to_watch?.length > 0 && (
            <div style={{ color: '#aaa', fontSize: '0.85rem' }}>
              Body parts to watch: {enhancedData.health_analysis.sensitive_transits.body_parts_to_watch.join(', ')}
            </div>
          )}
          {enhancedData.health_analysis.sensitive_transits.recommendations?.map((rec, i) => (
            <div key={i} style={{ color: '#888', fontSize: '0.85rem', marginTop: '5px' }}>
              💡 {rec}
            </div>
          ))}
        </div>
      )}

      {/* Regional Health */}
      {enhancedData?.health_analysis?.regional_health && (
        <div style={styles.healthGrid}>
          {Object.entries(enhancedData.health_analysis.regional_health).map(([region, data]) => (
            <div key={region} style={styles.healthCard}>
              <div style={styles.regionTitle}>
                {region === 'Head' ? '🧠' : region === 'Upper Body' ? '💪' : region === 'Middle Body' ? '🫁' : '🦵'}
                {region} - {data.status}
              </div>
              {data.malefics?.length > 0 && (
                <div style={{ color: '#f87171', fontSize: '0.85rem' }}>
                  Malefics: {data.malefics.join(', ')}
                </div>
              )}
              {data.benefics?.length > 0 && (
                <div style={{ color: '#4ade80', fontSize: '0.85rem' }}>
                  Benefics: {data.benefics.join(', ')}
                </div>
              )}
              <div style={{ color: '#888', fontSize: '0.8rem', marginTop: '5px' }}>
                {data.advice}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );

  const renderAskTab = () => (
    <div style={styles.questionSection}>
      <h3 style={{ color: '#ffd700', marginBottom: '15px' }}>
        💬 Ask About Your Chart
      </h3>
      
      <input
        type="text"
        placeholder="Ask a question... e.g., 'How is my career looking?'"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && askQuestion()}
        style={styles.questionInput}
      />

      <div style={styles.questionSuggestions}>
        {['How is my career?', 'Will I get married soon?', 'What about my health?', 'Is this good for travel?', 'How is my financial outlook?'].map((q) => (
          <button
            key={q}
            onClick={() => { setQuestion(q); }}
            style={styles.suggestionChip}
          >
            {q}
          </button>
        ))}
      </div>

      <button
        onClick={askQuestion}
        disabled={questionLoading || !question.trim()}
        style={{
          ...styles.analyzeBtn,
          opacity: questionLoading || !question.trim() ? 0.5 : 1,
        }}
      >
        {questionLoading ? 'Thinking...' : 'Ask'}
      </button>

      {answer && (
        <div style={styles.answerBox}>
          {/* Parse markdown-style formatting */}
          <div style={styles.answerText}>
            {answer.answer.split('\n\n').map((section, idx) => {
              // Handle headers with **
              if (section.startsWith('**') && section.includes('**')) {
                const headerMatch = section.match(/^\*\*(.+?)\*\*(.*)$/s);
                if (headerMatch) {
                  return (
                    <div key={idx} style={{ marginBottom: '15px' }}>
                      <h4 style={{ color: '#ffd700', marginBottom: '8px', fontSize: '1.1rem' }}>
                        {headerMatch[1]}
                      </h4>
                      {headerMatch[2] && <div style={{ color: '#ccc' }}>{headerMatch[2]}</div>}
                    </div>
                  );
                }
              }
              // Handle numbered lists
              if (/^\d+\./.test(section)) {
                return (
                  <div key={idx} style={{ marginLeft: '15px', marginBottom: '10px', color: '#aaa' }}>
                    {section.split('\n').map((line, i) => (
                      <div key={i} style={{ marginBottom: '5px' }}>{line}</div>
                    ))}
                  </div>
                );
              }
              // Handle bullet points
              if (section.includes('• ')) {
                return (
                  <div key={idx} style={{ marginLeft: '15px', marginBottom: '10px' }}>
                    {section.split('\n').map((line, i) => {
                      if (line.includes('✅') || line.includes('✓')) {
                        return <div key={i} style={{ color: '#4ade80', marginBottom: '5px' }}>{line}</div>;
                      } else if (line.includes('⚠️') || line.includes('✗')) {
                        return <div key={i} style={{ color: '#f87171', marginBottom: '5px' }}>{line}</div>;
                      } else if (line.includes('📚')) {
                        return <div key={i} style={{ color: '#60a5fa', marginBottom: '5px' }}>{line}</div>;
                      } else if (line.includes('💡')) {
                        return <div key={i} style={{ color: '#fbbf24', marginBottom: '5px' }}>{line}</div>;
                      }
                      return <div key={i} style={{ color: '#aaa', marginBottom: '5px' }}>{line}</div>;
                    })}
                  </div>
                );
              }
              // Regular text
              return <div key={idx} style={{ marginBottom: '10px', color: '#ccc' }}>{section}</div>;
            })}
          </div>
          <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'center', marginTop: '15px', borderTop: '1px solid rgba(255,215,0,0.2)', paddingTop: '15px' }}>
            <span style={{
              ...styles.confidenceBadge,
              background: answer.confidence === 'High' ? 'rgba(74, 222, 128, 0.2)' : 'rgba(251, 191, 36, 0.2)',
              color: answer.confidence === 'High' ? '#4ade80' : '#fbbf24',
            }}>
              Confidence: {answer.confidence}
            </span>
            {answer.area && (
              <span style={{ color: '#888', fontSize: '0.85rem' }}>
                Area: {answer.area}
              </span>
            )}
          </div>
          
          {answer.follow_up_suggestions?.length > 0 && (
            <div style={{ marginTop: '15px' }}>
              <div style={{ color: '#888', fontSize: '0.85rem', marginBottom: '8px' }}>
                Follow-up questions:
              </div>
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                {answer.follow_up_suggestions.map((sug, i) => (
                  <button
                    key={i}
                    onClick={() => setQuestion(sug)}
                    style={styles.suggestionChip}
                  >
                    {sug}
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );

  // New: 12-Month Timeline Graph Tab
  const renderTimelineTab = () => {
    const areas = [
      { key: 'career', name: 'Career', icon: '💼' },
      { key: 'finance', name: 'Finance', icon: '💰' },
      { key: 'health', name: 'Health', icon: '❤️' },
      { key: 'marriage', name: 'Marriage', icon: '💍' },
      { key: 'relationships', name: 'Relationships', icon: '💕' },
      { key: 'education', name: 'Education', icon: '📚' },
      { key: 'travel', name: 'Travel', icon: '✈️' },
      { key: 'property', name: 'Property', icon: '🏠' },
      { key: 'family', name: 'Family', icon: '👨‍👩‍👧‍👦' },
      { key: 'spirituality', name: 'Spirituality', icon: '🙏' },
    ];

    const getOutlookColor = (score) => {
      if (score >= 70) return '#4ade80';  // Green - Favorable
      if (score >= 50) return '#fbbf24';  // Yellow - Above average
      if (score >= 30) return '#fb923c';  // Orange - Below average
      return '#f87171';  // Red - Challenging
    };

    const getOutlookLabel = (score) => {
      if (score >= 70) return 'Favorable';
      if (score >= 50) return 'Above Average';
      if (score >= 30) return 'Below Average';
      return 'Challenging';
    };

    return (
      <div style={{ padding: '10px 0' }}>
        <h3 style={{ color: '#ffd700', marginBottom: '15px' }}>
          📈 12-Month Transit Outlook
        </h3>
        <p style={{ color: '#888', fontSize: '0.9rem', marginBottom: '20px' }}>
          Plan your year with a monthly outlook score (0-100). 50 is neutral - above is favorable, below requires caution.
        </p>

        {/* Area Selector */}
        <div style={{ marginBottom: '20px' }}>
          <label style={{ color: '#aaa', marginRight: '10px' }}>Select Life Area:</label>
          <select
            value={selectedTimelineArea}
            onChange={(e) => setSelectedTimelineArea(e.target.value)}
            style={{
              background: 'rgba(255, 255, 255, 0.1)',
              border: '1px solid rgba(255, 215, 0, 0.3)',
              borderRadius: '8px',
              padding: '8px 15px',
              color: '#fff',
              fontSize: '0.9rem',
              marginRight: '15px',
            }}
          >
            {areas.map((area) => (
              <option key={area.key} value={area.key} style={{ background: '#1a1a2e' }}>
                {area.icon} {area.name}
              </option>
            ))}
          </select>
          <button
            onClick={() => fetchTimeline(selectedTimelineArea)}
            disabled={timelineLoading}
            style={{
              ...styles.analyzeBtn,
              opacity: timelineLoading ? 0.5 : 1,
            }}
          >
            {timelineLoading ? 'Loading...' : 'Generate Timeline'}
          </button>
        </div>

        {/* Timeline Graph */}
        {timelineData && timelineData.monthly_data && (
          <>
            {/* Summary Stats */}
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
              gap: '15px',
              marginBottom: '25px',
            }}>
              <div style={{
                background: 'rgba(255, 255, 255, 0.05)',
                borderRadius: '10px',
                padding: '15px',
                textAlign: 'center',
              }}>
                <div style={{ fontSize: '2rem', fontWeight: 'bold', color: getOutlookColor(timelineData.summary?.average_score || 50) }}>
                  {(timelineData.summary?.average_score || 0).toFixed(0)}
                </div>
                <div style={{ color: '#888', fontSize: '0.85rem' }}>Average Score</div>
              </div>
              <div style={{
                background: 'rgba(74, 222, 128, 0.1)',
                borderRadius: '10px',
                padding: '15px',
                textAlign: 'center',
              }}>
                <div style={{ fontSize: '1rem', fontWeight: 'bold', color: '#4ade80' }}>
                  {timelineData.summary?.best_months?.length > 0 
                    ? timelineData.summary.best_months.map(m => timelineData.monthly_data[m-1]?.month?.slice(0,3) || m).join(', ')
                    : timelineData.summary?.peak_score || '-'}
                </div>
                <div style={{ color: '#888', fontSize: '0.85rem' }}>Best Period (Peak: {timelineData.summary?.peak_score || '-'})</div>
              </div>
              <div style={{
                background: 'rgba(248, 113, 113, 0.1)',
                borderRadius: '10px',
                padding: '15px',
                textAlign: 'center',
              }}>
                <div style={{ fontSize: '1rem', fontWeight: 'bold', color: '#f87171' }}>
                  {timelineData.summary?.challenging_months?.length > 0 
                    ? timelineData.summary.challenging_months.map(m => timelineData.monthly_data[m-1]?.month?.slice(0,3) || m).join(', ')
                    : timelineData.summary?.lowest_score || '-'}
                </div>
                <div style={{ color: '#888', fontSize: '0.85rem' }}>Challenging (Low: {timelineData.summary?.lowest_score || '-'})</div>
              </div>
              <div style={{
                background: 'rgba(255, 215, 0, 0.1)',
                borderRadius: '10px',
                padding: '15px',
                textAlign: 'center',
              }}>
                <div style={{ fontSize: '1.2rem', fontWeight: 'bold', color: '#ffd700' }}>
                  {timelineData.summary?.overall_trend || '-'}
                </div>
                <div style={{ color: '#888', fontSize: '0.85rem' }}>Overall Trend</div>
              </div>
            </div>

            {/* Line Chart */}
            <div style={{
              background: 'rgba(0, 0, 0, 0.3)',
              borderRadius: '12px',
              padding: '20px',
              marginBottom: '20px',
            }}>
              <ResponsiveContainer width="100%" height={350}>
                <ComposedChart data={timelineData.monthly_data}>
                  <defs>
                    <linearGradient id="colorScore" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#ffd700" stopOpacity={0.3}/>
                      <stop offset="95%" stopColor="#ffd700" stopOpacity={0}/>
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                  <XAxis 
                    dataKey="month" 
                    stroke="#888"
                    tick={{ fill: '#aaa', fontSize: 12 }}
                  />
                  <YAxis 
                    domain={[0, 100]} 
                    stroke="#888"
                    tick={{ fill: '#aaa', fontSize: 12 }}
                    tickFormatter={(value) => `${value}`}
                  />
                  <Tooltip
                    contentStyle={{
                      background: 'rgba(26, 26, 46, 0.95)',
                      border: '1px solid rgba(255, 215, 0, 0.3)',
                      borderRadius: '8px',
                      color: '#fff',
                    }}
                    formatter={(value, name) => {
                      if (name === 'normalized_score') {
                        return [`${value.toFixed(0)} - ${getOutlookLabel(value)}`, 'Score'];
                      }
                      return [value, name];
                    }}
                    labelFormatter={(label) => `📅 ${label}`}
                  />
                  <Legend />
                  {/* Neutral line at 50 */}
                  <ReferenceLine y={50} stroke="#fbbf24" strokeDasharray="5 5" label={{ value: 'Neutral', fill: '#fbbf24', fontSize: 12 }} />
                  {/* Favorable zone line at 70 */}
                  <ReferenceLine y={70} stroke="#4ade80" strokeDasharray="3 3" strokeOpacity={0.5} />
                  {/* Challenging zone line at 30 */}
                  <ReferenceLine y={30} stroke="#f87171" strokeDasharray="3 3" strokeOpacity={0.5} />
                  <Area
                    type="monotone"
                    dataKey="normalized_score"
                    stroke="#ffd700"
                    fill="url(#colorScore)"
                    name="Score"
                  />
                  <Line
                    type="monotone"
                    dataKey="normalized_score"
                    stroke="#ffd700"
                    strokeWidth={3}
                    dot={{ fill: '#ffd700', strokeWidth: 2, r: 5 }}
                    activeDot={{ r: 8, fill: '#fff', stroke: '#ffd700' }}
                    name="Monthly Score"
                  />
                </ComposedChart>
              </ResponsiveContainer>
            </div>

            {/* Monthly Details */}
            <div style={{ marginTop: '20px' }}>
              <h4 style={{ color: '#ffd700', marginBottom: '15px' }}>📋 Monthly Breakdown</h4>
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))',
                gap: '10px',
              }}>
                {timelineData.monthly_data.map((month, idx) => (
                  <div
                    key={idx}
                    style={{
                      background: 'rgba(255, 255, 255, 0.05)',
                      borderRadius: '10px',
                      padding: '12px',
                      borderLeft: `4px solid ${getOutlookColor(month.normalized_score)}`,
                    }}
                  >
                    <div style={{ 
                      fontWeight: 'bold', 
                      color: '#fff',
                      marginBottom: '5px',
                    }}>
                      {month.month} {month.year}
                    </div>
                    <div style={{
                      fontSize: '1.5rem',
                      fontWeight: 'bold',
                      color: getOutlookColor(month.normalized_score),
                    }}>
                      {month.normalized_score?.toFixed(0) || 0}
                    </div>
                    <div style={{
                      fontSize: '0.8rem',
                      color: getOutlookColor(month.normalized_score),
                      marginBottom: '5px',
                    }}>
                      {month.outlook || getOutlookLabel(month.normalized_score)}
                    </div>
                    {month.key_influences?.length > 0 && (
                      <div style={{ fontSize: '0.75rem', color: '#888' }}>
                        {month.key_influences.slice(0, 2).join(', ')}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>

            {/* Legend */}
            <div style={{
              marginTop: '20px',
              padding: '15px',
              background: 'rgba(0, 0, 0, 0.2)',
              borderRadius: '10px',
              fontSize: '0.85rem',
            }}>
              <strong style={{ color: '#ffd700' }}>Score Guide:</strong>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '15px', marginTop: '10px' }}>
                <span><span style={{ color: '#4ade80' }}>●</span> 70-100: Favorable</span>
                <span><span style={{ color: '#fbbf24' }}>●</span> 50-69: Above Average</span>
                <span><span style={{ color: '#fb923c' }}>●</span> 30-49: Below Average</span>
                <span><span style={{ color: '#f87171' }}>●</span> 0-29: Challenging</span>
              </div>
            </div>
          </>
        )}

        {!timelineData && !timelineLoading && (
          <div style={{ 
            textAlign: 'center', 
            color: '#888', 
            padding: '40px',
            background: 'rgba(0, 0, 0, 0.2)',
            borderRadius: '12px',
          }}>
            Select a life area and click "Generate Timeline" to see your 12-month outlook
          </div>
        )}
      </div>
    );
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <div>
          <h2 style={styles.title}>🌟 Enhanced Transit Analysis</h2>
          <p style={styles.subtitle}>
            8-Layer Analysis: BPHS + Vedha + Tara + Murthi + Special Nakshatras + Latta + Body Parts + Ashtakavarga
          </p>
        </div>
        <div style={styles.controls}>
          <input
            type="date"
            value={transitDate}
            onChange={(e) => setTransitDate(e.target.value)}
            style={styles.dateInput}
          />
          <button
            onClick={() => analyzeTransits(true)}
            style={styles.analyzeBtn}
            disabled={loading}
          >
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
        </div>
      </div>

      {error && <div style={styles.error}>❌ {error}</div>}

      {loading && (
        <div style={styles.loading}>✨ Running 8-layer transit analysis...</div>
      )}

      {enhancedData && !loading && (
        <>
          {/* Tabs */}
          <div style={styles.tabs}>
            {['planets', 'areas', 'health', 'timeline', 'ask'].map((tab) => (
              <button
                key={tab}
                onClick={() => setActiveTab(tab)}
                style={{
                  ...styles.tab,
                  ...(activeTab === tab ? styles.tabActive : styles.tabInactive),
                }}
              >
                {tab === 'planets' && '🪐 Planets'}
                {tab === 'areas' && '📊 Life Areas'}
                {tab === 'health' && '❤️ Health'}
                {tab === 'timeline' && '📈 Timeline'}
                {tab === 'ask' && '💬 Ask'}
              </button>
            ))}
          </div>

          {/* Tab Content */}
          {activeTab === 'planets' && renderPlanetsTab()}
          {activeTab === 'areas' && renderAreasTab()}
          {activeTab === 'health' && renderHealthTab()}
          {activeTab === 'timeline' && renderTimelineTab()}
          {activeTab === 'ask' && renderAskTab()}

          {/* Footer */}
          <div style={{
            marginTop: '20px',
            padding: '15px',
            background: 'rgba(0, 0, 0, 0.2)',
            borderRadius: '10px',
            fontSize: '0.85rem',
            color: '#888',
          }}>
            <strong>Overall:</strong> {enhancedData.overall_summary?.assessment} |{' '}
            <strong>Natal Moon:</strong> {enhancedData.native_data?.natal_moon_sign} |{' '}
            <strong>Transit Date:</strong> {enhancedData.transit_date}
          </div>
        </>
      )}

      {!enhancedData && !loading && !error && (
        <div style={{ textAlign: 'center', color: '#888', padding: '40px' }}>
          Select a date and click "Analyze" for comprehensive transit analysis
        </div>
      )}
    </div>
  );
};

export default EnhancedTransitAnalysis;
