import { queryDeviceDaqAlarm } from '../services/api';

export default {
  namespace: 'alarm',

  state: {
    deviceDaqAlarm: [],
    loading: false,
  },

  effects: {

    *fetchDaqAlarm({ payload }, { call, put }) {
      const response = yield call(queryDAQAlarm, payload);
      yield put({
        type: 'save',
        payload: {
          deviceDaqAlarm: response.deviceDaqAlarm,
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
        deviceDaqAlarm: [],
      };
    },
  },
  
};
