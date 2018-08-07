import { queryChangelog } from '../services/api';
import { queryTodolist } from '../services/api';

export default {
  namespace: 'version',

  state: {
    changelog: '',
    todolist: '',
    loading: false,
  },

  effects: {

    *fetchChangelog({ payload }, { call, put }) {
      const response = yield call(queryChangelog, payload);

      yield put({
        type: 'save',
        payload: {
          changelog: response,
        },
      });
    },


    *fetchTodolist({ payload }, { call, put }) {
      const response = yield call(queryTodolist, payload);

      yield put({
        type: 'save',
        payload: {
          todolist: response,
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
        changelog: '',
        todolist: '',
      };
    },
  },
  
};
