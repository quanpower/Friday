import { queryProducts } from '../services/api';
import { queryProductProfile } from '../services/api';

export default {
  namespace: 'products',

  state: {
    products: [],
    productProfile: [],
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

    *fetchProductProfile({ payload }, { call, put }) {
      const response = yield call(queryProductProfile, payload);
      console.log('-----in effects queryProductProfile-----')
      console.log(response)
      yield put({
        type: 'saveProductProfile',
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

    saveProductProfile(state, action) {
      return {
        ...state,
        productProfile: action.payload,
      };
    },
  },
};
