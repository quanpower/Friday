import { queryDAQAlarm } from '../services/api';

export default {
  namespace: 'alarm',

  state: {
    temperatureAlarm: [],
    loading: false,
  },

  effects: {

    *fetchTemperatureAlarm({ payload }, { call, put }) {
      const response = yield call(queryDAQAlarm, payload);
      yield put({
        type: 'save',
        payload: {
          temperatureAlarm: response.temperatureAlarm,
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
        temperatureAlarm: [],
      };
    },
  },
  
};
