import * as actionTypes from '../actionTypes/users';
import { get, post } from '../utils/api';


export function addUser() {
  return async dispath => {
    dispath({
      type: actionTypes.ADD_USER
    });
  

    try {
      const result = await post('/users');

      dispatch({
        type: actionTypes.ADD_USER_SUCCESS,
        user: result

      });
    } catch(e) {
      dispatch({
        type: actionTypes.ADD_USER_ERROR
      });
    }
  }
}
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
