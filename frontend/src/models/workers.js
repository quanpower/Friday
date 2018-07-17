import { queryWorkers } from '../services/api';

export default {
  namespace: 'workers',

  state: {
    workers: [],
    project_name: '20180704',
  },

  effects: {
    *fetchWorkers( { payload }, { call, put }) {
      console.log(payload)
      const response = yield call(queryWorkers, payload);

      console.log(response)
      yield put({
        type: 'saveWorkers',
        payload: Array.isArray(response) ? response : [],
      });
    },
  },

  reducers: {
    saveWorkers(state, action) {
      return {
        ...state,
        workers: action.payload,
      };
    },
  },
};
