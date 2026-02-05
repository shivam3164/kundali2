import React, { useState, useCallback, useMemo, memo } from 'react';
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  TouchableOpacity,
  SafeAreaView,
  ActivityIndicator,
  Dimensions,
  Platform,
} from 'react-native';
import { NativeStackScreenProps } from '@react-navigation/native-stack';
import { RootStackParamList } from '../types/navigation';
import { getEnhancedTransit, getTransitTimeline, getHouseInterpretation } from '../api/kundali';
import { BirthData } from '../types';

type ResultsScreenProps = NativeStackScreenProps<RootStackParamList, 'Results'>;
type TabType = 'chart' | 'dasha' | 'yoga' | 'transit' | 'houses' | 'summary';

const { width } = Dimensions.get('window');

const PLANET_SYMBOLS: { [key: string]: string } = {
  Sun: 'Su', Moon: 'Mo', Mars: 'Ma', Mercury: 'Me',
  Jupiter: 'Ju', Venus: 'Ve', Saturn: 'Sa', Rahu: 'Ra', Ketu: 'Ke',
};

const getStatusColor = (status: string) => {
  switch (status) {
    case 'Good': case 'Favorable': case 'Very Favorable': case 'Positive': case 'Excellent': return '#4ade80';
    case 'Bad': case 'Challenging': case 'Very Weak': case 'Difficult': return '#f87171';
    case 'Obstructed': case 'Mixed': case 'Average': case 'Neutral': return '#fbbf24';
    default: return '#9ca3af';
  }
};

const getStrengthColor = (pct: number) => {
  if (pct >= 70) return '#4ade80';
  if (pct >= 50) return '#fbbf24';
  if (pct >= 30) return '#fb923c';
  return '#f87171';
};

// Memoized components
const TabButton = memo(({ tab, active, onPress, label }: { tab: TabType; active: boolean; onPress: () => void; label: string }) => (
  <TouchableOpacity
    style={[styles.tab, active && styles.tabActive]}
    onPress={onPress}
    activeOpacity={0.7}
  >
    <Text style={[styles.tabText, active && styles.tabTextActive]}>{label}</Text>
  </TouchableOpacity>
));

const PlanetRow = memo(({ name, planet }: { name: string; planet: any }) => (
  <View style={styles.planetRow}>
    <View style={styles.planetName}>
      <Text style={styles.planetSymbol}>{PLANET_SYMBOLS[name]}</Text>
      <Text style={styles.planetLabel}>{name}</Text>
      {planet.is_retrograde && <Text style={styles.retrograde}>R</Text>}
    </View>
    <View style={styles.planetDetails}>
      <Text style={styles.planetSign}>{planet.sign}</Text>
      <Text style={styles.planetDegree}>{planet.degree_in_sign.toFixed(1)}°</Text>
    </View>
    <View style={styles.planetExtra}>
      <Text style={styles.nakshatraText}>{planet.nakshatra}</Text>
      <Text style={styles.houseText}>H{planet.house}</Text>
    </View>
  </View>
));

const AntardashaRow = memo(({ dasha, formatDate }: { dasha: any; formatDate: (d: string) => string }) => (
  <View style={styles.antardashaRow}>
    <View style={styles.antardashaPlanet}>
       <View style={styles.bulletPoint} />
       <Text style={[styles.antardashaPlanetText, dasha.is_current && styles.activeText]}>
         {dasha.planet}
       </Text>
    </View>
    <View style={styles.dashaDate}>
       <Text style={[styles.antardashaDateRange, dasha.is_current && styles.activeText]}>
         {formatDate(dasha.start_date)} - {formatDate(dasha.end_date)}
       </Text>
    </View>
  </View>
));

const DashaRow = memo(({ dasha, formatDate, expanded, onToggle }: { dasha: any; formatDate: (d: string) => string; expanded: boolean; onToggle: () => void }) => (
  <View>
    <TouchableOpacity 
      style={[styles.dashaRow, dasha.is_current && styles.dashaRowCurrent]} 
      onPress={onToggle}
      activeOpacity={0.7}
    >
      <View style={styles.dashaPlanet}>
        <View style={{flexDirection: 'row', alignItems: 'center'}}>
          <Text style={styles.dashaPlanetText}>{dasha.planet}</Text>
          {dasha.is_current && (
            <View style={styles.currentBadge}>
              <Text style={styles.currentBadgeText}>NOW</Text>
            </View>
          )}
        </View>
        <Text style={styles.dashaDuration}>{dasha.duration_years.toFixed(1)} years</Text>
      </View>
      <View style={styles.dashaDate}>
        <Text style={styles.dashaDateRange}>{formatDate(dasha.start_date)}</Text>
        <Text style={styles.dashaDateRange}>{formatDate(dasha.end_date)}</Text>
        <Text style={styles.expandIcon}>{expanded ? '▲' : '▼'}</Text>
      </View>
    </TouchableOpacity>
    
    {expanded && (
      <View style={styles.antardashaContainer}>
        {dasha.description && (
          <View style={styles.descriptionBox}>
            <Text style={styles.descriptionText}>{dasha.description}</Text>
          </View>
        )}
        {dasha.antardashas && (
          <>
            <Text style={styles.subPeriodTitle}>Antardashas (Sub-periods)</Text>
            {dasha.antardashas.map((ad: any, index: number) => (
               <AntardashaRow key={index} dasha={ad} formatDate={formatDate} />
            ))}
          </>
        )}
      </View>
    )}
  </View>
));

const TransitPlanetCard = memo(({ result }: { result: any }) => (
  <View style={[styles.transitCard, { borderLeftColor: getStatusColor(result.final_status) }]}>
    <View style={styles.transitHeader}>
      <Text style={styles.transitPlanet}>{result.planet}</Text>
      <View style={[styles.statusBadge, { backgroundColor: getStatusColor(result.final_status) + '30' }]}>
        <Text style={[styles.statusText, { color: getStatusColor(result.final_status) }]}>
          {result.final_status}
        </Text>
      </View>
    </View>
    <View style={styles.transitDetails}>
      <Text style={styles.transitDetail}>Sign: {result.transit_sign}</Text>
      <Text style={styles.transitDetail}>House from Moon: {result.house_from_moon}</Text>
      <Text style={[styles.transitScore, { color: result.score >= 0 ? '#4ade80' : '#f87171' }]}>
        Score: {result.score > 0 ? '+' : ''}{result.score}
      </Text>
    </View>
    {result.tara && (
      <Text style={styles.transitTara}>Tara: {result.tara.tara_name} ({result.tara.tara_quality})</Text>
    )}
    {result.vedha?.is_obstructed && (
      <Text style={styles.vedhaWarning}>Vedha: Blocked by {result.vedha.obstructing_planet}</Text>
    )}
    <Text style={styles.transitPrediction} numberOfLines={3}>{result.final_prediction}</Text>
  </View>
));

const HouseCard = memo(({ house, expanded, onToggle }: { house: any; expanded: boolean; onToggle: () => void }) => {
  const pct = house.strength?.legacy?.percentage ?? house.strength?.percentage ?? 0;

  return (
    <TouchableOpacity
      style={[styles.houseCard, expanded && styles.houseCardExpanded]}
      onPress={onToggle}
      activeOpacity={0.8}
    >
      <View style={styles.houseHeader}>
        <View style={styles.houseNumber}>
          <Text style={styles.houseNumberText}>{house.house_number}</Text>
        </View>
        <View style={styles.houseInfo}>
          <Text style={styles.houseName}>{house.name}</Text>
          <Text style={styles.houseSubtitle}>{house.sign} | Lord: {house.lord}</Text>
        </View>
        <View style={[styles.housePctBadge, { backgroundColor: getStrengthColor(pct) + '30' }]}>
          <Text style={[styles.housePctText, { color: getStrengthColor(pct) }]}>{pct}%</Text>
        </View>
      </View>

      {house.planets_in_house?.length > 0 && (
        <Text style={styles.housePlanets}>Planets: {house.planets_in_house.join(', ')}</Text>
      )}

      {expanded && (
        <View style={styles.houseExpanded}>
          {house.significations?.primary && (
            <View style={styles.houseSection}>
              <Text style={styles.houseSectionTitle}>Significations</Text>
              <View style={styles.tagContainer}>
                {house.significations.primary.slice(0, 5).map((sig: string, i: number) => (
                  <View key={i} style={styles.tag}>
                    <Text style={styles.tagText}>{sig}</Text>
                  </View>
                ))}
              </View>
            </View>
          )}

          {/* New Strength Details Section */}
          {house.strength?.recommended?.explanation && (
             <View style={styles.houseSection}>
               <Text style={styles.houseSectionTitle}>Strength Calculation</Text>
               {house.strength.recommended.explanation.map((line: string, i: number) => (
                 <Text key={i} style={styles.calculationText}>{line}</Text>
               ))}
               {house.strength?.recommended?.formula && (
                 <Text style={styles.formulaText}>Formula: {house.strength.recommended.formula}</Text>
               )}
             </View>
          )}

          {house.lord_analysis?.bphs_effect && (
            <View style={styles.houseSection}>
              <Text style={styles.houseSectionTitle}>BPHS Effect</Text>
              <Text style={styles.bphsText}>{house.lord_analysis.bphs_effect}</Text>
            </View>
          )}

          {house.interpretation?.overview && (
            <View style={styles.houseSection}>
              <Text style={styles.houseSectionTitle}>Interpretation</Text>
              <Text style={styles.interpretText}>{house.interpretation.overview}</Text>
            </View>
          )}
        </View>
      )}

      <Text style={styles.expandHint}>{expanded ? 'Tap to collapse' : 'Tap to expand'}</Text>
    </TouchableOpacity>
  );
});

export default function ResultsScreen({ navigation, route }: ResultsScreenProps) {
  const { chartData, dashaData, yogaData, interpretation } = route.params;
  const [activeTab, setActiveTab] = useState<TabType>('chart');
  
  // State for expanded Mahadasha
  const [expandedDasha, setExpandedDasha] = useState<number | null>(null);

  // Transit state
  const [transitData, setTransitData] = useState<any>(null);
  const [transitLoading, setTransitLoading] = useState(false);
  const [timelineData, setTimelineData] = useState<any>(null);
  const [selectedTransitArea, setSelectedTransitArea] = useState<string | null>(null);

  // Houses state
  const [housesData, setHousesData] = useState<any>(null);
  const [housesLoading, setHousesLoading] = useState(false);
  const [expandedHouse, setExpandedHouse] = useState<number | null>(null);

  const birthData: BirthData = useMemo(() => ({
    year: chartData.birth_data.year,
    month: chartData.birth_data.month,
    day: chartData.birth_data.day,
    hour: chartData.birth_data.hour,
    minute: chartData.birth_data.minute,
    second: 0,
    lat: chartData.birth_data.lat,
    lon: chartData.birth_data.lon,
    ayanamsa: 'lahiri',
  }), [chartData]);

  const fetchTransit = useCallback(async () => {
    setTransitLoading(true);
    try {
      const [transit, timeline] = await Promise.all([
        getEnhancedTransit(birthData, new Date()),
        getTransitTimeline(birthData, 'career'),
      ]);
      setTransitData(transit);
      setTimelineData(timeline);
    } catch (e) {
      console.error('Transit fetch error:', e);
    } finally {
      setTransitLoading(false);
    }
  }, [birthData]);

  const handleTransitAreaPress = useCallback(async (area: string) => {
    setSelectedTransitArea(area);
    try {
      const timeline = await getTransitTimeline(birthData, area);
      setTimelineData(timeline);
    } catch (e) {
      console.error('Transit timeline fetch error:', e);
    }
  }, [birthData]);

  const fetchHouses = useCallback(async () => {
    setHousesLoading(true);
    try {
      const houses = await getHouseInterpretation(birthData);
      setHousesData(houses);
    } catch (e) {
      console.error('Houses fetch error:', e);
    } finally {
      setHousesLoading(false);
    }
  }, [birthData]);

  const handleTabChange = useCallback((tab: TabType) => {
    setActiveTab(tab);
    if (tab === 'transit' && !transitData) fetchTransit();
    if (tab === 'houses' && !housesData) fetchHouses();
  }, [transitData, housesData, fetchTransit, fetchHouses]);

  const formatDate = useCallback((dateStr: string): string => {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-IN', { year: 'numeric', month: 'short' });
  }, []);

  const tabs: { key: TabType; label: string }[] = [
    { key: 'chart', label: 'Chart' },
    { key: 'dasha', label: 'Dasha' },
    { key: 'yoga', label: 'Yoga' },
    { key: 'transit', label: 'Transit' },
    { key: 'houses', label: 'Houses' },
    { key: 'summary', label: 'Summary' },
  ];

  const renderChart = () => (
    <ScrollView style={styles.content} showsVerticalScrollIndicator={false}>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Ascendant (Lagna)</Text>
        <View style={styles.ascendantInfo}>
          <Text style={styles.signLarge}>{chartData.ascendant.sign}</Text>
          <Text style={styles.detailText}>
            {chartData.ascendant.degree_in_sign.toFixed(2)}° | {chartData.ascendant.nakshatra}
          </Text>
          <Text style={styles.detailText}>Lord: {chartData.ascendant.lord}</Text>
        </View>
      </View>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Key Signs</Text>
        <View style={styles.signsRow}>
          <View style={styles.signBox}>
            <Text style={styles.signLabel}>Moon</Text>
            <Text style={styles.signValue}>{chartData.moon_sign}</Text>
          </View>
          <View style={styles.signBox}>
            <Text style={styles.signLabel}>Sun</Text>
            <Text style={styles.signValue}>{chartData.sun_sign}</Text>
          </View>
        </View>
      </View>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Planets</Text>
        {Object.entries(chartData.planets).map(([name, planet]) => (
          <PlanetRow key={name} name={name} planet={planet} />
        ))}
      </View>
    </ScrollView>
  );

  const renderDasha = () => (
    <ScrollView style={styles.content} showsVerticalScrollIndicator={false}>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>About Vimshottari Dasha</Text>
        <Text style={styles.summaryText}>
          This system divides your life into major planetary periods (Mahadashas) totaling 120 years. 
          Each major period is ruled by a specific planet and influences your life according to that planet's 
          position in your chart. Tap on any period below to see its sub-periods (Antardashas).
        </Text>
      </View>

      {dashaData.current_mahadasha && (
        <View style={[styles.card, styles.currentDashaCard]}>
          <Text style={styles.cardTitle}>Current Period</Text>
          <Text style={styles.currentDashaText}>{dashaData.current_mahadasha.planet}</Text>
          <Text style={styles.dashaDateText}>
            {formatDate(dashaData.current_mahadasha.start_date)} - {formatDate(dashaData.current_mahadasha.end_date)}
          </Text>
        </View>
      )}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Mahadasha Periods</Text>
        <Text style={styles.hintText}>Tap a row to see detailed sub-periods</Text>
        {dashaData.mahadashas.map((dasha: any, index: number) => (
          <DashaRow 
            key={index} 
            dasha={dasha} 
            formatDate={formatDate} 
            expanded={expandedDasha === index}
            onToggle={() => setExpandedDasha(expandedDasha === index ? null : index)}
          />
        ))}
      </View>
    </ScrollView>
  );

  const renderYoga = () => (
    <ScrollView style={styles.content} showsVerticalScrollIndicator={false}>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Yogas ({yogaData.all_yogas?.length || 0})</Text>
        {yogaData.all_yogas && yogaData.all_yogas.length > 0 ? (
          yogaData.all_yogas.map((yoga: any, index: number) => (
            <View key={index} style={styles.yogaItem}>
              <View style={styles.yogaHeader}>
                <Text style={styles.yogaName}>{yoga.name}</Text>
                <View style={[styles.strengthBadge, { backgroundColor: getStatusColor(yoga.strength) + '30' }]}>
                  <Text style={[styles.strengthText, { color: getStatusColor(yoga.strength) }]}>
                    {yoga.strength}
                  </Text>
                </View>
              </View>
              <Text style={styles.yogaType}>{yoga.type}</Text>
              {yoga.description && <Text style={styles.yogaDescription}>{yoga.description}</Text>}
            </View>
          ))
        ) : (
          <Text style={styles.noDataText}>No yogas detected</Text>
        )}
      </View>
    </ScrollView>
  );

  const renderTransit = () => {
    if (transitLoading) {
      return (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#ff6b35" />
          <Text style={styles.loadingText}>Analyzing transits...</Text>
        </View>
      );
    }

    if (!transitData?.success) {
      return (
        <View style={styles.content}>
          <TouchableOpacity style={styles.fetchButton} onPress={fetchTransit}>
            <Text style={styles.fetchButtonText}>Load Transit Analysis</Text>
          </TouchableOpacity>
        </View>
      );
    }

    return (
      <ScrollView style={styles.content} showsVerticalScrollIndicator={false}>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Transit Summary</Text>
          <View style={styles.transitSummary}>
            <View style={styles.summaryBox}>
              <Text style={[styles.summaryValue, { color: '#4ade80' }]}>
                {transitData.favorable_planets?.length || 0}
              </Text>
              <Text style={styles.summaryLabel}>Favorable</Text>
            </View>
            <View style={styles.summaryBox}>
              <Text style={[styles.summaryValue, { color: '#f87171' }]}>
                {transitData.unfavorable_planets?.length || 0}
              </Text>
              <Text style={styles.summaryLabel}>Challenging</Text>
            </View>
            <View style={styles.summaryBox}>
              <Text style={[styles.summaryValue, { color: '#60a5fa' }]}>
                {transitData.overall_summary?.average_score?.toFixed(0) || 0}
              </Text>
              <Text style={styles.summaryLabel}>Score</Text>
            </View>
          </View>
        </View>

        {transitData.area_impacts && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>Life Areas (Tap to analyze)</Text>
            <View style={styles.areasGrid}>
              {Object.entries(transitData.area_impacts).slice(0, 8).map(([area, data]: [string, any]) => (
                <TouchableOpacity
                  key={area}
                  style={[
                    styles.areaBox,
                    { borderLeftColor: getStatusColor(data.outlook) },
                    selectedTransitArea === area && styles.areaBoxSelected
                  ]}
                  onPress={() => handleTransitAreaPress(area)}
                >
                  <Text style={styles.areaName}>{area}</Text>
                  <Text style={[styles.areaOutlook, { color: getStatusColor(data.outlook) }]}>
                    {data.outlook}
                  </Text>
                </TouchableOpacity>
              ))}
            </View>
          </View>
        )}

        {timelineData?.monthly_data && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>
              12-Month Outlook {selectedTransitArea ? `(${selectedTransitArea})` : ''}
            </Text>
            <ScrollView horizontal showsHorizontalScrollIndicator={false}>
              <View style={styles.timelineRow}>
                {timelineData.monthly_data.map((month: any, idx: number) => (
                  <View key={idx} style={styles.monthBox}>
                    <Text style={styles.monthName}>{month.month?.slice(0, 3)}</Text>
                    <Text style={[styles.monthScore, { color: getStrengthColor(month.normalized_score) }]}>
                      {month.normalized_score?.toFixed(0)}
                    </Text>
                  </View>
                ))}
              </View>
            </ScrollView>
          </View>
        )}

        <View style={styles.card}>
          <Text style={styles.cardTitle}>Planet Analysis</Text>
          {transitData.planet_results?.map((result: any) => (
            <TransitPlanetCard key={result.planet} result={result} />
          ))}
        </View>
      </ScrollView>
    );
  };

  const renderHouses = () => {
    if (housesLoading) {
      return (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#ff6b35" />
          <Text style={styles.loadingText}>Loading houses...</Text>
        </View>
      );
    }

    if (!housesData?.data?.houses) {
      return (
        <View style={styles.content}>
          <TouchableOpacity style={styles.fetchButton} onPress={fetchHouses}>
            <Text style={styles.fetchButtonText}>Load House Analysis</Text>
          </TouchableOpacity>
        </View>
      );
    }

    const { houses, summary, life_areas_summary } = housesData.data;

    // Group areas
    const areas = Object.entries(life_areas_summary || {});
    const favorable = areas.filter(([_, a]: any) => ['Excellent', 'Very Good', 'Good', 'Favorable', 'Very Favorable'].includes(a.outlook));
    const neutral = areas.filter(([_, a]: any) => ['Neutral', 'Average', 'Mixed'].includes(a.outlook));
    const challenging = areas.filter(([_, a]: any) => ['Challenging', 'Difficult', 'Bad', 'Weak', 'Very Weak'].includes(a.outlook));

    const renderAreaGroup = (title: string, items: any[], color: string) => (
      items.length > 0 && (
        <View style={styles.houseGroupSection} key={title}>
          <Text style={[styles.groupTitle, { color }]}>{title}</Text>
          <View style={styles.lifeAreasGrid}>
            {items.map(([key, area]: [string, any]) => (
                <View key={key} style={[styles.lifeAreaCard, { borderLeftColor: getStatusColor(area.outlook) }]}>
                  <Text style={styles.lifeAreaName}>{key.replace(/_/g, ' ')}</Text>
                  <Text style={[styles.lifeAreaOutlook, { color: getStatusColor(area.outlook) }]}>
                    {area.outlook}
                  </Text>
                  <Text style={styles.lifeAreaDetail}>{area.average_strength}%</Text>
                </View>
            ))}
          </View>
        </View>
      )
    );

    return (
      <ScrollView style={styles.content} showsVerticalScrollIndicator={false}>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>House Summary</Text>
          <View style={styles.houseSummary}>
            <View style={styles.summaryItem}>
              <Text style={styles.summaryItemLabel}>Strongest</Text>
              <Text style={styles.summaryItemValue}>{summary?.strongest_houses?.join(', ')}</Text>
            </View>
            <View style={styles.summaryItem}>
              <Text style={styles.summaryItemLabel}>Kendra</Text>
              <Text style={styles.summaryItemValue}>{summary?.kendra_strength}</Text>
            </View>
          </View>
        </View>

        {life_areas_summary && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>Life Areas Analysis</Text>
            {renderAreaGroup('Favorable Areas', favorable, '#4ade80')}
            {renderAreaGroup('Neutral Areas', neutral, '#fbbf24')}
            {renderAreaGroup('Areas for Improvement', challenging, '#f87171')}
          </View>
        )}

        <Text style={styles.sectionTitle}>All 12 Houses</Text>
        {Object.values(houses).map((house: any) => (
          <HouseCard
            key={house.house_number}
            house={house}
            expanded={expandedHouse === house.house_number}
            onToggle={() => setExpandedHouse(expandedHouse === house.house_number ? null : house.house_number)}
          />
        ))}
      </ScrollView>
    );
  };

  const renderSummary = () => (
    <ScrollView style={styles.content} showsVerticalScrollIndicator={false}>
      {interpretation.summary && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Overview</Text>
          <Text style={styles.summaryText}>{interpretation.summary}</Text>
        </View>
      )}
      {interpretation.personality && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Personality</Text>
          <Text style={styles.summaryText}>{interpretation.personality}</Text>
        </View>
      )}
      {interpretation.strengths && interpretation.strengths.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Strengths</Text>
          {interpretation.strengths.map((s: string, i: number) => (
            <View key={i} style={styles.listItem}>
              <Text style={styles.bullet}>+</Text>
              <Text style={styles.listText}>{s}</Text>
            </View>
          ))}
        </View>
      )}
      {interpretation.challenges && interpretation.challenges.length > 0 && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Challenges</Text>
          {interpretation.challenges.map((c: string, i: number) => (
            <View key={i} style={styles.listItem}>
              <Text style={[styles.bullet, { color: '#f87171' }]}>-</Text>
              <Text style={styles.listText}>{c}</Text>
            </View>
          ))}
        </View>
      )}
      {interpretation.career && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Career</Text>
          <Text style={styles.summaryText}>{interpretation.career}</Text>
        </View>
      )}
    </ScrollView>
  );

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView
        horizontal
        showsHorizontalScrollIndicator={false}
        style={styles.tabScrollView}
        contentContainerStyle={styles.tabContainer}
      >
        {tabs.map((t) => (
          <TabButton
            key={t.key}
            tab={t.key}
            active={activeTab === t.key}
            onPress={() => handleTabChange(t.key)}
            label={t.label}
          />
        ))}
      </ScrollView>

      {activeTab === 'chart' && renderChart()}
      {activeTab === 'dasha' && renderDasha()}
      {activeTab === 'yoga' && renderYoga()}
      {activeTab === 'transit' && renderTransit()}
      {activeTab === 'houses' && renderHouses()}
      {activeTab === 'summary' && renderSummary()}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f5f5f5' },
  tabScrollView: { backgroundColor: '#fff', maxHeight: 50 },
  tabContainer: { flexDirection: 'row', paddingHorizontal: 8, alignItems: 'center' },
  tab: { paddingVertical: 12, paddingHorizontal: 16, marginHorizontal: 2 },
  tabActive: { borderBottomWidth: 2, borderBottomColor: '#ff6b35' },
  tabText: { fontSize: 14, color: '#888', fontWeight: '500' },
  tabTextActive: { color: '#ff6b35', fontWeight: '600' },
  content: { flex: 1, padding: 12 },
  card: { backgroundColor: '#fff', borderRadius: 12, padding: 16, marginBottom: 12, shadowColor: '#000', shadowOffset: { width: 0, height: 1 }, shadowOpacity: 0.05, shadowRadius: 3, elevation: 2 },
  cardTitle: { fontSize: 16, fontWeight: '600', color: '#1a1a2e', marginBottom: 12 },
  ascendantInfo: { alignItems: 'center', paddingVertical: 8 },
  signLarge: { fontSize: 28, fontWeight: '700', color: '#ff6b35' },
  detailText: { fontSize: 14, color: '#666', marginTop: 4 },
  signsRow: { flexDirection: 'row', gap: 12 },
  signBox: { flex: 1, backgroundColor: '#f8f8f8', borderRadius: 8, padding: 12, alignItems: 'center' },
  signLabel: { fontSize: 12, color: '#888', marginBottom: 4 },
  signValue: { fontSize: 16, fontWeight: '600', color: '#1a1a2e' },
  planetRow: { flexDirection: 'row', alignItems: 'center', paddingVertical: 10, borderBottomWidth: 1, borderBottomColor: '#f0f0f0' },
  planetName: { flexDirection: 'row', alignItems: 'center', width: 85 },
  planetSymbol: { fontSize: 13, fontWeight: '700', color: '#ff6b35', width: 24 },
  planetLabel: { fontSize: 13, color: '#1a1a2e' },
  retrograde: { fontSize: 10, color: '#e74c3c', marginLeft: 4, fontWeight: '700' },
  planetDetails: { flex: 1, alignItems: 'center' },
  planetSign: { fontSize: 13, color: '#1a1a2e', fontWeight: '500' },
  planetDegree: { fontSize: 11, color: '#888' },
  planetExtra: { alignItems: 'flex-end', width: 70 },
  nakshatraText: { fontSize: 11, color: '#666' },
  houseText: { fontSize: 10, color: '#888' },
  currentDashaCard: { backgroundColor: '#fff8f5', borderWidth: 1, borderColor: '#ff6b35' },
  currentDashaText: { fontSize: 24, fontWeight: '700', color: '#ff6b35', textAlign: 'center' },
  dashaDateText: { fontSize: 13, color: '#666', textAlign: 'center', marginTop: 4 },
  dashaRow: { flexDirection: 'row', alignItems: 'center', paddingVertical: 12, borderBottomWidth: 1, borderBottomColor: '#f0f0f0' },
  dashaRowCurrent: { backgroundColor: '#fff8f5', marginHorizontal: -16, paddingHorizontal: 16, borderRadius: 8 },
  dashaPlanet: { flex: 1 },
  dashaPlanetText: { fontSize: 15, fontWeight: '500', color: '#1a1a2e' },
  dashaDuration: { fontSize: 12, color: '#888' },
  dashaDate: { alignItems: 'flex-end' },
  dashaDateRange: { fontSize: 12, color: '#666' },
  currentBadge: { backgroundColor: '#ff6b35', paddingHorizontal: 8, paddingVertical: 4, borderRadius: 4, marginLeft: 8 },
  currentBadgeText: { color: '#fff', fontSize: 10, fontWeight: '700' },
  yogaItem: { paddingVertical: 12, borderBottomWidth: 1, borderBottomColor: '#f0f0f0' },
  yogaHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  yogaName: { fontSize: 15, fontWeight: '600', color: '#1a1a2e', flex: 1 },
  strengthBadge: { paddingHorizontal: 10, paddingVertical: 4, borderRadius: 12 },
  strengthText: { fontSize: 11, fontWeight: '600', textTransform: 'uppercase' },
  yogaType: { fontSize: 12, color: '#888', marginTop: 2 },
  yogaDescription: { fontSize: 13, color: '#666', marginTop: 6, lineHeight: 18 },
  noDataText: { fontSize: 14, color: '#888', textAlign: 'center', paddingVertical: 20 },
  summaryText: { fontSize: 14, color: '#444', lineHeight: 22 },
  listItem: { flexDirection: 'row', marginBottom: 8 },
  bullet: { fontSize: 16, color: '#4ade80', marginRight: 8, fontWeight: '700' },
  listText: { fontSize: 14, color: '#444', flex: 1, lineHeight: 20 },
  loadingContainer: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 40 },
  loadingText: { marginTop: 12, fontSize: 14, color: '#888' },
  fetchButton: { backgroundColor: '#ff6b35', padding: 16, borderRadius: 12, alignItems: 'center', margin: 20 },
  fetchButtonText: { color: '#fff', fontSize: 16, fontWeight: '600' },
  transitSummary: { flexDirection: 'row', justifyContent: 'space-around' },
  summaryBox: { alignItems: 'center' },
  summaryValue: { fontSize: 28, fontWeight: '700' },
  summaryLabel: { fontSize: 12, color: '#888', marginTop: 4 },
  areasGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 8 },
  areaBox: { width: (width - 64) / 2, backgroundColor: '#f8f8f8', borderRadius: 8, padding: 12, borderLeftWidth: 3 },
  areaBoxSelected: { backgroundColor: '#fff', borderColor: '#ff6b35', borderWidth: 1 },
  areaName: { fontSize: 13, fontWeight: '500', color: '#1a1a2e', textTransform: 'capitalize' },
  areaOutlook: { fontSize: 12, fontWeight: '600', marginTop: 4 },
  timelineRow: { flexDirection: 'row', paddingVertical: 8 },
  monthBox: { width: 50, alignItems: 'center', marginRight: 8 },
  monthName: { fontSize: 11, color: '#888' },
  monthScore: { fontSize: 18, fontWeight: '700', marginTop: 4 },
  transitCard: { backgroundColor: '#f8f8f8', borderRadius: 10, padding: 12, marginBottom: 10, borderLeftWidth: 3 },
  transitHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 },
  transitPlanet: { fontSize: 16, fontWeight: '600', color: '#1a1a2e' },
  statusBadge: { paddingHorizontal: 10, paddingVertical: 4, borderRadius: 12 },
  statusText: { fontSize: 11, fontWeight: '600' },
  transitDetails: { flexDirection: 'row', flexWrap: 'wrap', gap: 12, marginBottom: 6 },
  transitDetail: { fontSize: 12, color: '#666' },
  transitScore: { fontSize: 12, fontWeight: '600' },
  transitTara: { fontSize: 11, color: '#60a5fa', marginBottom: 4 },
  vedhaWarning: { fontSize: 11, color: '#f87171', marginBottom: 4 },
  transitPrediction: { fontSize: 12, color: '#888', lineHeight: 18, marginTop: 6 },
  houseSummary: { flexDirection: 'row', justifyContent: 'space-between' },
  summaryItem: { alignItems: 'center', flex: 1 },
  summaryItemLabel: { fontSize: 11, color: '#888' },
  summaryItemValue: { fontSize: 14, fontWeight: '600', color: '#1a1a2e', marginTop: 4 },
  lifeAreasGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 8 },
  lifeAreaCard: { width: (width - 56) / 2, backgroundColor: '#f8f8f8', borderRadius: 8, padding: 10, borderLeftWidth: 3 },
  lifeAreaName: { fontSize: 12, fontWeight: '500', color: '#1a1a2e', textTransform: 'capitalize' },
  lifeAreaOutlook: { fontSize: 11, fontWeight: '600', marginTop: 2 },
  lifeAreaDetail: { fontSize: 10, color: '#888', marginTop: 2 },
  sectionTitle: { fontSize: 16, fontWeight: '600', color: '#1a1a2e', marginTop: 8, marginBottom: 12 },
  houseCard: { backgroundColor: '#fff', borderRadius: 12, padding: 14, marginBottom: 10, shadowColor: '#000', shadowOffset: { width: 0, height: 1 }, shadowOpacity: 0.05, shadowRadius: 2, elevation: 1 },
  houseCardExpanded: { borderWidth: 1, borderColor: '#ff6b35' },
  houseHeader: { flexDirection: 'row', alignItems: 'center' },
  houseNumber: { width: 32, height: 32, borderRadius: 16, backgroundColor: '#ff6b35', justifyContent: 'center', alignItems: 'center' },
  houseNumberText: { color: '#fff', fontWeight: '700', fontSize: 14 },
  houseInfo: { flex: 1, marginLeft: 12 },
  houseName: { fontSize: 14, fontWeight: '600', color: '#1a1a2e' },
  houseSubtitle: { fontSize: 12, color: '#888', marginTop: 2 },
  housePctBadge: { paddingHorizontal: 10, paddingVertical: 4, borderRadius: 12 },
  housePctText: { fontSize: 13, fontWeight: '600' },
  housePlanets: { fontSize: 12, color: '#60a5fa', marginTop: 8 },
  houseExpanded: { marginTop: 12, paddingTop: 12, borderTopWidth: 1, borderTopColor: '#f0f0f0' },
  houseSection: { marginBottom: 12 },
  houseSectionTitle: { fontSize: 13, fontWeight: '600', color: '#ff6b35', marginBottom: 6 },
  tagContainer: { flexDirection: 'row', flexWrap: 'wrap', gap: 6 },
  tag: { backgroundColor: '#fff8f5', paddingHorizontal: 8, paddingVertical: 4, borderRadius: 4 },
  tagText: { fontSize: 11, color: '#ff6b35' },
  bphsText: { fontSize: 12, color: '#666', fontStyle: 'italic', lineHeight: 18 },
  interpretText: { fontSize: 12, color: '#666', lineHeight: 18 },
  expandHint: { fontSize: 11, color: '#ccc', textAlign: 'center', marginTop: 8 },
  calculationText: { fontSize: 11, color: '#666', marginBottom: 2, fontFamily: Platform.OS === 'ios' ? 'Courier New' : 'monospace' },
  formulaText: { fontSize: 10, color: '#999', marginTop: 4, fontStyle: 'italic' },
  houseGroupSection: { marginBottom: 16 },
  groupTitle: { fontSize: 14, fontWeight: '600', marginBottom: 8, marginLeft: 4 },
  
  // Dasha
  hintText: { fontSize: 11, color: '#999', fontStyle: 'italic', marginBottom: 10 },
  expandIcon: { fontSize: 12, color: '#ccc', marginTop: 4, textAlign: 'right' },
  antardashaContainer: { backgroundColor: '#fafafa', padding: 12, borderBottomWidth: 1, borderBottomColor: '#f0f0f0' },
  subPeriodTitle: { fontSize: 11, fontWeight: '700', color: '#888', marginBottom: 8, textTransform: 'uppercase' },
  antardashaRow: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 6, alignItems: 'center' },
  antardashaPlanet: { flexDirection: 'row', alignItems: 'center' },
  bulletPoint: { width: 6, height: 6, borderRadius: 3, backgroundColor: '#ddd', marginRight: 8 },
  antardashaPlanetText: { fontSize: 13, color: '#444' },
  antardashaDateRange: { fontSize: 12, color: '#888' },
  activeText: { color: '#ff6b35', fontWeight: '600' },
  descriptionBox: { backgroundColor: '#fff', padding: 10, borderRadius: 8, marginBottom: 12, borderLeftWidth: 3, borderLeftColor: '#ff6b35', shadowColor: '#000', shadowOffset: { width: 0, height: 1 }, shadowOpacity: 0.05, shadowRadius: 1, elevation: 1 },
  descriptionText: { fontSize: 13, color: '#555', lineHeight: 20, fontStyle: 'italic' },
});
