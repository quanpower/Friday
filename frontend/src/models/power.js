import { getCurrentPowerData } from '../services/api';
import { getHistoryPowerData } from '../services/api';
import { fakeChartData } from '../services/api';

export default {
  namespace: 'power',

  state: {
    currentPower: [],
    historyPower: [],
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
    *fetchSalesData(_, { call, put }) {
      const response = yield call(fakeChartData);
      yield put({
        type: 'save',
        payload: {
          salesData: response.salesData,
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
        historyPower: [],
      };
    },
  },
};
