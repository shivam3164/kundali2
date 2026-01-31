import React, { useState } from 'react';
import InputForm from './InputForm';
import ChartView from './ChartView';
import DashaTimeline from './DashaTimeline';
import YogaList from './YogaList';
import Interpretations from './Interpretations';
import HouseInterpretation from './HouseInterpretation';

const styles = {
  app: {
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '20px',
  },
  header: {
    textAlign: 'center',
    marginBottom: '30px',
    color: '#ffd700',
    textShadow: '0 0 10px rgba(255, 215, 0, 0.3)',
  },
  title: {
    fontSize: '2.5rem',
    marginBottom: '10px',
  },
  subtitle: {
    fontSize: '1rem',
    color: '#aaa',
  },
  loading: {
    textAlign: 'center',
    padding: '40px',
    color: '#ffd700',
  },
  error: {
    textAlign: 'center',
    padding: '20px',
    color: '#ff6b6b',
    background: 'rgba(255, 107, 107, 0.1)',
    borderRadius: '10px',
    margin: '20px 0',
  },
  results: {
    display: 'grid',
    gap: '20px',
  },
};

function App() {
  const [chartData, setChartData] = useState(null);
  const [dashaData, setDashaData] = useState(null);
  const [yogaData, setYogaData] = useState(null);
  const [interpretation, setInterpretation] = useState(null);
  const [houseData, setHouseData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFormSubmit = async (form) => {
    setLoading(true);
    setError(null);
    
    const birthData = {
      year: parseInt(form.year),
      month: parseInt(form.month),
      day: parseInt(form.day),
      hour: parseInt(form.hour),
      minute: parseInt(form.minute),
      second: 0,
      lat: parseFloat(form.lat),
      lon: parseFloat(form.lon),
      ayanamsa: "lahiri"
    };

    try {
      const chartRes = await fetch('/api/v1/chart/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(birthData)
      });
      if (!chartRes.ok) throw new Error('Failed to calculate chart');
      const chart = await chartRes.json();
      setChartData(chart);

      const dashaRes = await fetch('/api/v1/dasha/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(birthData)
      });
      if (dashaRes.ok) {
        const dasha = await dashaRes.json();
        setDashaData(dasha);
      }

      const yogaRes = await fetch('/api/v1/yoga/detect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(birthData)
      });
      if (yogaRes.ok) {
        const yoga = await yogaRes.json();
        setYogaData(yoga);
      }

      const interpRes = await fetch('/api/v1/interpretation/summary', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(birthData)
      });
      if (interpRes.ok) {
        const interp = await interpRes.json();
        setInterpretation(interp);
      }

      // Fetch house interpretations
      const houseRes = await fetch('/api/v1/interpretation/houses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(birthData)
      });
      if (houseRes.ok) {
        const houses = await houseRes.json();
        setHouseData(houses);
      }

    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.app}>
      <header style={styles.header}>
        <h1 style={styles.title}>🕉️ Kundali App</h1>
        <p style={styles.subtitle}>Based on Brihat Parashara Hora Shastra</p>
      </header>
      
      <InputForm onSubmit={handleFormSubmit} />
      
      {loading && <div style={styles.loading}>✨ Calculating your Kundali...</div>}
      
      {error && <div style={styles.error}>❌ {error}</div>}
      
      {chartData && (
        <div style={styles.results}>
          <ChartView chart={chartData} />
          <DashaTimeline dashas={dashaData} />
          <YogaList yogas={yogaData} />
          <HouseInterpretation houseData={houseData} />
          <Interpretations interpretations={interpretation} />
        </div>
      )}
    </div>
  );
}

export default App;
