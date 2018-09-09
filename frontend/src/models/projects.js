import { queryProjects } from '@/services/api';

export default {
  namespace: 'projects',

  state: {
    projects: [],
  },

  effects: {
    *fetchProjects(_, { call, put }) {
      const response = yield call(queryProjects);
      console.log('-----in effects fetchProjects-----')
      console.log(response)
      yield put({
        type: 'saveProjects',
        payload: Array.isArray(response) ? response : [],
      });
    },
  },

  reducers: {
    saveProjects(state, action) {
      return {
        ...state,
        projects: action.payload,
      };
    },
  },
};
