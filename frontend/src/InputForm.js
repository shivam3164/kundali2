import React, { useState } from 'react';
import { INDIAN_CITIES } from './cities';

const sortedCities = [...INDIAN_CITIES].sort((a, b) => a.name.localeCompare(b.name));

const styles = {
  form: {
    background: 'rgba(255, 255, 255, 0.05)',
    padding: '30px',
    borderRadius: '15px',
    marginBottom: '30px',
    border: '1px solid rgba(255, 215, 0, 0.2)',
  },
  title: {
    color: '#ffd700',
    marginBottom: '20px',
    fontSize: '1.2rem',
  },
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
    gap: '15px',
  },
  inputGroup: {
    display: 'flex',
    flexDirection: 'column',
  },
  label: {
    fontSize: '0.85rem',
    color: '#aaa',
    marginBottom: '5px',
  },
  input: {
    padding: '12px',
    borderRadius: '8px',
    border: '1px solid rgba(255, 215, 0, 0.3)',
    background: 'rgba(0, 0, 0, 0.3)',
    color: '#fff',
    fontSize: '1rem',
  },
  select: {
    padding: '12px',
    borderRadius: '8px',
    border: '1px solid rgba(255, 215, 0, 0.3)',
    background: 'rgba(0, 0, 0, 0.3)',
    color: '#fff',
    fontSize: '1rem',
    cursor: 'pointer',
  },
  button: {
    gridColumn: '1 / -1',
    padding: '15px 30px',
    background: 'linear-gradient(135deg, #ffd700, #ff8c00)',
    border: 'none',
    borderRadius: '8px',
    color: '#1a1a2e',
    fontSize: '1.1rem',
    fontWeight: 'bold',
    cursor: 'pointer',
    marginTop: '10px',
  },
};

function InputForm({ onSubmit }) {
  // Default to New Delhi
  const [form, setForm] = useState({
    year: '', 
    month: '', 
    day: '', 
    hour: '', 
    minute: '', 
    lat: '28.6139', 
    lon: '77.2090', 
    place: 'New Delhi'
  });

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleCityChange = e => {
    const selectedCity = sortedCities.find(city => city.name === e.target.value);
    if (selectedCity) {
      setForm({
        ...form,
        lat: selectedCity.lat,
        lon: selectedCity.lon,
        place: selectedCity.name
      });
    } else {
        setForm({...form, place: e.target.value });
    }
  };

  const handleSubmit = e => {
    e.preventDefault();
    onSubmit(form);
  };

  return (
    <form style={styles.form} onSubmit={handleSubmit}>
      <h3 style={styles.title}>📅 Enter Birth Details</h3>
      
      <div style={{marginBottom: '20px'}}>
        <div style={styles.inputGroup}>
            <label style={styles.label}>Quick Location Select (India)</label>
            <select 
                style={styles.select} 
                value={sortedCities.some(c => c.name === form.place && Math.abs(c.lat - form.lat) < 0.01) ? form.place : ""} 
                onChange={handleCityChange}
            >
                <option value="" disabled>Select a City</option>
                {sortedCities.map((city, index) => (
                    <option key={index} value={city.name}>
                        {city.name}
                    </option>
                ))}
            </select>
        </div>
      </div>

      <div style={styles.grid}>
        <div style={styles.inputGroup}>
          <label style={styles.label}>Year</label>
          <input style={styles.input} name="year" type="number" placeholder="1990" value={form.year} onChange={handleChange} required />
        </div>
        <div style={styles.inputGroup}>
          <label style={styles.label}>Month</label>
          <input style={styles.input} name="month" type="number" placeholder="1-12" min="1" max="12" value={form.month} onChange={handleChange} required />
        </div>
        <div style={styles.inputGroup}>
          <label style={styles.label}>Day</label>
          <input style={styles.input} name="day" type="number" placeholder="1-31" min="1" max="31" value={form.day} onChange={handleChange} required />
        </div>
        <div style={styles.inputGroup}>
          <label style={styles.label}>Hour (24h)</label>
          <input style={styles.input} name="hour" type="number" placeholder="0-23" min="0" max="23" value={form.hour} onChange={handleChange} required />
        </div>
        <div style={styles.inputGroup}>
          <label style={styles.label}>Minute</label>
          <input style={styles.input} name="minute" type="number" placeholder="0-59" min="0" max="59" value={form.minute} onChange={handleChange} required />
        </div>
        <div style={styles.inputGroup}>
          <label style={styles.label}>Latitude</label>
          <input style={styles.input} name="lat" type="number" step="0.0001" placeholder="28.6139" value={form.lat} onChange={handleChange} required />
        </div>
        <div style={styles.inputGroup}>
          <label style={styles.label}>Longitude</label>
          <input style={styles.input} name="lon" type="number" step="0.0001" placeholder="77.2090" value={form.lon} onChange={handleChange} required />
        </div>
        <button style={styles.button} type="submit">🔮 Generate Kundali</button>
      </div>
    </form>
  );
}

export default InputForm;
