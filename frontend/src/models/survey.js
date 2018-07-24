import { queryDeviceDaqRealtime } from '../services/api';
import { queryDeviceDaqHistory } from '../services/api';
import { queryDeviceDaqRecord } from '../services/api';

export default {
  namespace: 'survey',

  state: {
    currentPower: [],
    deviceDaqRealtime: [],
    deviceDaqHistory:[],
    deviceDaqRecord:[],
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

    *fetchDeviceDaqRealtime({ payload }, { call, put }) {
      const response = yield call(queryDAQData, payload);
      yield put({
        type: 'save',
        payload: {
          deviceDaqRealtime: response.deviceDaqRealtime,
        },
      });

      yield put({
        type: 'save',
        payload: {
          realtimeBars: response.realtimeBars,
        },
      });
    },

    *fetchDeviceDaqHistory({ payload }, { call, put }) {
      const response = yield call(queryDAQHistory, payload);
      yield put({
        type: 'save',
        payload: {
          deviceDaqHistory: response.deviceDaqHistory,
        },
      });

      yield put({
        type: 'save',
        payload: {
          historyLines: response.historyLines,
        },
      });


    },

    *fetchDeviceDaqRecord({ payload }, { call, put }) {
      const response = yield call(queryDAQRecord, payload);
      yield put({
        type: 'save',
        payload: {
          deviceDaqRecord: response.deviceDaqRecord,
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
        deviceDaqRealtime: [],
        deviceDaqHistory:[],
        deviceDaqRecord:[],
        realtimeBars:[],
        historyLines:[],
        recordColumns:[],
      };
    },
  },
};
