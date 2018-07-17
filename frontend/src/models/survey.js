import { queryTemperatureData } from '../services/api';
import { queryTemperatureHistory } from '../services/api';
import { queryTemperatureRecord } from '../services/api';

export default {
  namespace: 'survey',

  state: {
    currentPower: [],
    temperatureData: [],
    temperatureHistory:[],
    temperatureRecord:[],
    realtimeBars:[],
    historyLines:[],
    recordColumns:[],
    loading: false,
  },

  effects: {
    *fetch({ payload }, { call, put }) {
      const response = yield call(queryCurrentPowerData, payload);
      yield put({
        type: 'save',
        payload: response,
      });
    },

    *fetchTemperatureData({ payload }, { call, put }) {
      const response = yield call(queryTemperatureData, payload);
      yield put({
        type: 'save',
        payload: {
          temperatureData: response.temperatureData,
        },
      });

      yield put({
        type: 'save',
        payload: {
          realtimeBars: response.realtimeBars,
        },
      });
    },

    *fetchTemperatureHistory({ payload }, { call, put }) {
      const response = yield call(queryTemperatureHistory, payload);
      yield put({
        type: 'save',
        payload: {
          temperatureHistory: response.temperatureHistory,
        },
      });

      yield put({
        type: 'save',
        payload: {
          historyLines: response.historyLines,
        },
      });


    },

    *fetchTemperatureRecord({ payload }, { call, put }) {
      const response = yield call(queryTemperatureRecord, payload);
      yield put({
        type: 'save',
        payload: {
          temperatureRecord: response.temperatureRecord,
        },
      });

      yield put({
        type: 'save',
        payload: {
          recordColumns: response.recordColumns,
        },
      });
    },

    *fetchCurrentPowerData({ payload }, { call, put }) {
      const response = yield call(queryCurrentPowerData, payload);
      yield put({
        type: 'save',
        payload: {
          currentPower: response.currentPower,
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
        temperatureRecord:[],
        realtimeBars:[],
        historyLines:[],
        recordColumns:[],
      };
    },
  },
};
