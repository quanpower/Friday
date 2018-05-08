import { getCurrentPowerData } from '../services/api';
import { getHistoryPowerData } from '../services/api';
import { getTemperatureData } from '../services/api';
import { getTemperatureHistory } from '../services/api';

export default {
  namespace: 'power',

  state: {
    currentPower: [],
    temperatureData: [],
    temperatureHistory:[],
    loading: false,
  },

  effects: {
    *fetch(_, { call, put }) {
      const response = yield call(getCurrentPowerData);
      yield put({
        type: 'save',
        payload: response,
      });
    },
    *fetchTemperatureData(_, { call, put }) {
      const response = yield call(getTemperatureData);
      yield put({
        type: 'save',
        payload: {
          temperatureData: response.temperatureData,
        },
      });
    },
  },

  reducers: {
    save(state, { payload }) {
      return {
        ...state,
        ...payload,
      };
    },
    clear() {
      return {
        currentPower: [],
        temperatureData: [],
        temperatureHistory:[],
      };
    },
  },
};
