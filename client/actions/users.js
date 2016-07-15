import * as actionTypes from '../actionTypes/users';
import { get } from '../utils/api';


export function requestUsers() {
  return async dispatch => {
    dispatch({
      type: actionTypes.REQUEST_USERS
    });

    try {
      const result = await get('/api2/users');

      dispatch({
        type: actionTypes.REQUEST_USERS_SUCCESS,
        users: result
      });
    } catch(e) {
      dispatch({
        type: actionTypes.REQUEST_USERS_ERROR
      });
    }
  }
}
