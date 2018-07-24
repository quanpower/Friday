import { queryProducts } from '../services/api';

export default {
  namespace: 'products',

  state: {
    products: [],
  },

  effects: {
    *fetchProducts(_, { call, put }) {
      const response = yield call(queryProducts);
      console.log('-----in effects fetchProducts-----')
      console.log(response)
      yield put({
        type: 'saveProducts',
        payload: Array.isArray(response) ? response : [],
      });
    },
  },

  reducers: {
    saveProducts(state, action) {
      return {
        ...state,
        products: action.payload,
      };
    },
  },
};
