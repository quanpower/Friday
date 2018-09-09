import { queryDevices } from '@/services/api';
import { queryDeviceProfile } from '@/services/api';

export default {
  namespace: 'devices',

  state: {
    devices: [],
    deviceProfile: [{
      name:'name',
      owner:'owner',
      device_name:'device_name',
      device_secret:'device_secret',
      firmware_version:'firmware_version',
      node_type:'node_type',
      ip_address:'ip_address',
      status:'status',
      gmt_create:'gmt_create',
      gmt_active:'gmt_active',
      gmt_online:'gmt_online',
    }],

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
