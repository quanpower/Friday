import { queryDAQData } from '../services/api';
import { queryDAQHistory } from '../services/api';
import { queryDAQRecord } from '../services/api';

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
      const response = yield call(queryDAQData, payload);
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
      const response = yield call(queryDAQHistory, payload);
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
      const response = yield call(queryDAQRecord, payload);
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
