import { queryDevices } from '../services/api';

export default {
  namespace: 'devices',

  state: {
    devices: [],
  },

  effects: {
    *fetchDevices(_, { call, put }) {
      const response = yield call(queryDevices);
      console.log('-----in effects fetchDevices-----')
      console.log(response)
      yield put({
        type: 'saveDevices',
        payload: Array.isArray(response) ? response : [],
      });
    },
  },

  reducers: {
    saveDevices(state, action) {
      return {
        ...state,
        devices: action.payload,
      };
    },
  },
};
