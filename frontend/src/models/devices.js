import { queryDevices } from '../services/api';
import { queryDeviceProfile } from '../services/api';

export default {
  namespace: 'devices',

  state: {
    devices: [],
    deviceProfile: [],
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

    *fetchDeviceProfile({ payload }, { call, put }) {
      const response = yield call(queryDeviceProfile, payload);
      console.log('-----in effects fetchDevices-----')
      console.log(response)
      yield put({
        type: 'saveDeviceProfile',
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

    saveDeviceProfile(state, action) {
      return {
        ...state,
        deviceProfile: action.payload,
      };
    },
  },
};
