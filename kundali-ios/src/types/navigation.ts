import { ChartData, DashaData, YogaData, Interpretation } from './index';

export type RootStackParamList = {
  Home: undefined;
  Results: {
    chartData: ChartData;
    dashaData: DashaData;
    yogaData: YogaData;
    interpretation: Interpretation;
  };
};
