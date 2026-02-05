import axios from 'axios';
import { BirthData, ChartData, DashaData, YogaData, Interpretation } from '../types';

const API_BASE_URL = 'http://127.0.0.1:8002/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000,
});

export const calculateChart = async (birthData: BirthData): Promise<ChartData> => {
  const response = await api.post('/chart/calculate', birthData);
  return response.data;
};

export const calculateDasha = async (birthData: BirthData): Promise<DashaData> => {
  const response = await api.post('/dasha/calculate', birthData);
  return response.data;
};

export const detectYogas = async (birthData: BirthData): Promise<YogaData> => {
  const response = await api.post('/yoga/detect', birthData);
  return response.data;
};

export const getInterpretation = async (birthData: BirthData): Promise<Interpretation> => {
  const response = await api.post('/interpretation/summary', birthData);
  return response.data;
};

export const getHouseInterpretation = async (birthData: BirthData): Promise<any> => {
  const response = await api.post('/interpretation/houses', birthData);
  return response.data;
};

export const getEnhancedTransit = async (birthData: BirthData, transitDate: Date): Promise<any> => {
  const response = await api.post('/transit/enhanced', {
    ...birthData,
    transit_year: transitDate.getFullYear(),
    transit_month: transitDate.getMonth() + 1,
    transit_day: transitDate.getDate(),
  });
  return response.data;
};

export const getTransitTimeline = async (birthData: BirthData, area?: string): Promise<any> => {
  const response = await api.post('/transit/timeline', {
    ...birthData,
    area,
  });
  return response.data;
};

export const askTransitQuestion = async (birthData: BirthData, question: string): Promise<any> => {
  const response = await api.post('/transit/ask', {
    ...birthData,
    question,
  });
  return response.data;
};

export const healthCheck = async (): Promise<boolean> => {
  try {
    const response = await axios.get('http://localhost:8002/health');
    return response.status === 200;
  } catch {
    return false;
  }
};
