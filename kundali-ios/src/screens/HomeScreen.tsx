import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  Alert,
  ActivityIndicator,
  KeyboardAvoidingView,
  Platform,
  Modal,
  FlatList,
} from 'react-native';
import { NativeStackScreenProps } from '@react-navigation/native-stack';
import { INDIAN_CITIES } from '../data/cities';
import { calculateChart, calculateDasha, detectYogas, getInterpretation } from '../api/kundali';
import { BirthData } from '../types';
import { RootStackParamList } from '../types/navigation';

type HomeScreenProps = NativeStackScreenProps<RootStackParamList, 'Home'>;

export default function HomeScreen({ navigation }: HomeScreenProps) {
  const [year, setYear] = useState('');
  const [month, setMonth] = useState('');
  const [day, setDay] = useState('');
  const [hour, setHour] = useState('');
  const [minute, setMinute] = useState('');
  const [selectedCity, setSelectedCity] = useState(INDIAN_CITIES.find(c => c.name === 'New Delhi')!);
  const [loading, setLoading] = useState(false);
  const [showCityPicker, setShowCityPicker] = useState(false);
  const [citySearch, setCitySearch] = useState('');

  const filteredCities = INDIAN_CITIES.filter(city =>
    city.name.toLowerCase().includes(citySearch.toLowerCase())
  );

  const validateInputs = (): boolean => {
    const y = parseInt(year);
    const m = parseInt(month);
    const d = parseInt(day);
    const h = parseInt(hour);
    const min = parseInt(minute);

    if (!year || !month || !day || !hour || !minute) {
      Alert.alert('Error', 'Please fill in all birth details');
      return false;
    }

    if (y < 1900 || y > 2100) {
      Alert.alert('Error', 'Please enter a valid year (1900-2100)');
      return false;
    }

    if (m < 1 || m > 12) {
      Alert.alert('Error', 'Month must be between 1 and 12');
      return false;
    }

    if (d < 1 || d > 31) {
      Alert.alert('Error', 'Day must be between 1 and 31');
      return false;
    }

    if (h < 0 || h > 23) {
      Alert.alert('Error', 'Hour must be between 0 and 23');
      return false;
    }

    if (min < 0 || min > 59) {
      Alert.alert('Error', 'Minute must be between 0 and 59');
      return false;
    }

    return true;
  };

  const handleSubmit = async () => {
    if (!validateInputs()) return;

    setLoading(true);

    const birthData: BirthData = {
      year: parseInt(year),
      month: parseInt(month),
      day: parseInt(day),
      hour: parseInt(hour),
      minute: parseInt(minute),
      second: 0,
      lat: parseFloat(selectedCity.lat),
      lon: parseFloat(selectedCity.lon),
      ayanamsa: 'lahiri',
    };

    try {
      const [chartData, dashaData, yogaData, interpretation] = await Promise.all([
        calculateChart(birthData),
        calculateDasha(birthData),
        detectYogas(birthData),
        getInterpretation(birthData),
      ]);

      navigation.navigate('Results', {
        chartData,
        dashaData,
        yogaData,
        interpretation,
      });
    } catch (error: any) {
      console.error('API Error:', error);
      Alert.alert(
        'Connection Error',
        `Unable to connect to the server. ${error.message}\n\nPlease ensure the backend is running on port 8002.`
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <ScrollView
        contentContainerStyle={styles.scrollContent}
        keyboardShouldPersistTaps="handled"
      >
        <View style={styles.header}>
          <Text style={styles.title}>Kundali</Text>
          <Text style={styles.subtitle}>Vedic Birth Chart Calculator</Text>
        </View>

        <View style={styles.form}>
          <Text style={styles.sectionTitle}>Birth Date</Text>
          <View style={styles.row}>
            <View style={styles.inputGroup}>
              <Text style={styles.label}>Year</Text>
              <TextInput
                style={styles.input}
                value={year}
                onChangeText={setYear}
                placeholder="1990"
                placeholderTextColor="#999"
                keyboardType="number-pad"
                maxLength={4}
              />
            </View>
            <View style={styles.inputGroup}>
              <Text style={styles.label}>Month</Text>
              <TextInput
                style={styles.input}
                value={month}
                onChangeText={setMonth}
                placeholder="1-12"
                placeholderTextColor="#999"
                keyboardType="number-pad"
                maxLength={2}
              />
            </View>
            <View style={styles.inputGroup}>
              <Text style={styles.label}>Day</Text>
              <TextInput
                style={styles.input}
                value={day}
                onChangeText={setDay}
                placeholder="1-31"
                placeholderTextColor="#999"
                keyboardType="number-pad"
                maxLength={2}
              />
            </View>
          </View>

          <Text style={styles.sectionTitle}>Birth Time</Text>
          <View style={styles.row}>
            <View style={[styles.inputGroup, { flex: 1 }]}>
              <Text style={styles.label}>Hour (24h)</Text>
              <TextInput
                style={styles.input}
                value={hour}
                onChangeText={setHour}
                placeholder="0-23"
                placeholderTextColor="#999"
                keyboardType="number-pad"
                maxLength={2}
              />
            </View>
            <View style={[styles.inputGroup, { flex: 1 }]}>
              <Text style={styles.label}>Minute</Text>
              <TextInput
                style={styles.input}
                value={minute}
                onChangeText={setMinute}
                placeholder="0-59"
                placeholderTextColor="#999"
                keyboardType="number-pad"
                maxLength={2}
              />
            </View>
          </View>

          <Text style={styles.sectionTitle}>Birth Place</Text>
          <TouchableOpacity
            style={styles.citySelector}
            onPress={() => setShowCityPicker(true)}
          >
            <Text style={styles.citySelectorText}>{selectedCity.name}</Text>
            <Text style={styles.citySelectorArrow}>▼</Text>
          </TouchableOpacity>
          <Text style={styles.coordsText}>
            Lat: {selectedCity.lat}, Lon: {selectedCity.lon}
          </Text>

          <TouchableOpacity
            style={[styles.button, loading && styles.buttonDisabled]}
            onPress={handleSubmit}
            disabled={loading}
          >
            {loading ? (
              <ActivityIndicator color="#fff" />
            ) : (
              <Text style={styles.buttonText}>Generate Kundali</Text>
            )}
          </TouchableOpacity>
        </View>

        <Modal
          visible={showCityPicker}
          animationType="slide"
          presentationStyle="pageSheet"
        >
          <View style={styles.modalContainer}>
            <View style={styles.modalHeader}>
              <Text style={styles.modalTitle}>Select City</Text>
              <TouchableOpacity onPress={() => setShowCityPicker(false)}>
                <Text style={styles.modalClose}>Done</Text>
              </TouchableOpacity>
            </View>
            <TextInput
              style={styles.searchInput}
              value={citySearch}
              onChangeText={setCitySearch}
              placeholder="Search cities..."
              placeholderTextColor="#999"
              autoFocus
            />
            <FlatList
              data={filteredCities}
              keyExtractor={(item) => item.name}
              renderItem={({ item }) => (
                <TouchableOpacity
                  style={[
                    styles.cityItem,
                    item.name === selectedCity.name && styles.cityItemSelected,
                  ]}
                  onPress={() => {
                    setSelectedCity(item);
                    setShowCityPicker(false);
                    setCitySearch('');
                  }}
                >
                  <Text
                    style={[
                      styles.cityItemText,
                      item.name === selectedCity.name && styles.cityItemTextSelected,
                    ]}
                  >
                    {item.name}
                  </Text>
                </TouchableOpacity>
              )}
            />
          </View>
        </Modal>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
  scrollContent: {
    padding: 20,
  },
  header: {
    alignItems: 'center',
    marginBottom: 30,
    marginTop: 20,
  },
  title: {
    fontSize: 36,
    fontWeight: '700',
    color: '#1a1a2e',
    letterSpacing: 1,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginTop: 4,
  },
  form: {
    backgroundColor: '#fff',
    borderRadius: 16,
    padding: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 4,
  },
  sectionTitle: {
    fontSize: 14,
    fontWeight: '600',
    color: '#666',
    marginBottom: 12,
    marginTop: 8,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  row: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 16,
  },
  inputGroup: {
    flex: 1,
  },
  label: {
    fontSize: 13,
    color: '#888',
    marginBottom: 6,
  },
  input: {
    backgroundColor: '#f5f5f5',
    borderRadius: 10,
    padding: 14,
    fontSize: 16,
    color: '#1a1a2e',
    borderWidth: 1,
    borderColor: '#e0e0e0',
  },
  citySelector: {
    backgroundColor: '#f5f5f5',
    borderRadius: 10,
    padding: 14,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#e0e0e0',
  },
  citySelectorText: {
    fontSize: 16,
    color: '#1a1a2e',
  },
  citySelectorArrow: {
    fontSize: 12,
    color: '#888',
  },
  coordsText: {
    fontSize: 12,
    color: '#888',
    marginTop: 6,
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#ff6b35',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
    marginTop: 10,
  },
  buttonDisabled: {
    opacity: 0.7,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '600',
  },
  modalContainer: {
    flex: 1,
    backgroundColor: '#fff',
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  modalTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#1a1a2e',
  },
  modalClose: {
    fontSize: 16,
    color: '#ff6b35',
    fontWeight: '600',
  },
  searchInput: {
    backgroundColor: '#f5f5f5',
    margin: 16,
    padding: 14,
    borderRadius: 10,
    fontSize: 16,
    color: '#1a1a2e',
  },
  cityItem: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#f0f0f0',
  },
  cityItemSelected: {
    backgroundColor: '#fff5f0',
  },
  cityItemText: {
    fontSize: 16,
    color: '#1a1a2e',
  },
  cityItemTextSelected: {
    color: '#ff6b35',
    fontWeight: '600',
  },
});
