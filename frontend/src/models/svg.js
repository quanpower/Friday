import { queryBugs } from '../services/api';
import { postBugs } from '../services/api';

export default {
  namespace: 'svg',

  state: {
    bugLists: [],
    visible: false,

    loading: false,
  },

  effects: {

    *fetchBugs({ payload }, { call, put }) {
      const response = yield call(queryBugs, payload);

      console.log('------response-------')
      console.log(response)

      yield put({
        type: 'save',
        payload: {
          bugLists: response.bugLists,
        },
      });
    },


    *postBugs({ payload }, { call, put }) {
      const response = yield call(postBugs, payload);
      console.log(response)

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
        bugLists: [],
      };
    },
  },
  
};
