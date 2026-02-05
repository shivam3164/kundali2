export interface BirthData {
  year: number;
  month: number;
  day: number;
  hour: number;
  minute: number;
  second: number;
  lat: number;
  lon: number;
  ayanamsa: string;
}

export interface Planet {
  planet: string;
  longitude: number;
  sign: string;
  nakshatra: string;
  nakshatra_pada: number;
  house: number;
  is_retrograde: boolean;
  dignity: string;
  degree_in_sign: number;
}

export interface Ascendant {
  longitude: number;
  sign: string;
  degree_in_sign: number;
  nakshatra: string;
  nakshatra_pada: number;
  lord: string;
}

export interface ChartData {
  birth_data: BirthData;
  ascendant: Ascendant;
  planets: { [key: string]: Planet };
  houses: { [key: string]: any };
  lagna_sign: string;
  moon_sign: string;
  sun_sign: string;
}

export interface DashaPeriod {
  planet: string;
  start_date: string;
  end_date: string;
  duration_years: number;
  is_current: boolean;
  antardashas?: DashaPeriod[];
  description?: string;
}

export interface DashaData {
  mahadashas: DashaPeriod[];
  current_mahadasha: DashaPeriod;
  current_antardasha?: DashaPeriod;
}

export interface Yoga {
  name: string;
  type: string;
  strength: string;
  description: string;
  effects: string;
}

export interface YogaData {
  yogas: { [key: string]: Yoga[] };
  all_yogas: Yoga[];
  summary?: string;
  birth_data?: any;
}

export interface Interpretation {
  summary: string;
  personality: string;
  strengths: string[];
  challenges: string[];
  career: string;
  relationships: string;
}

export interface City {
  name: string;
  lat: string;
  lon: string;
}
