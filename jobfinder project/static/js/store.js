import { createStore,applyMiddleware } from 'redux'
import {user} from './reducers/user'
import {theme} from './reducers/theme'
import {step} from './reducers/step'
import {token} from './reducers/token'
import {WorkingTime} from './reducers/howtime'

import logger from 'redux-logger'
import thunk from 'redux-thunk'
var Redux = require('redux');



 const jobReducer = Redux.combineReducers({
       user:user,
       theme:theme,

  });

const initialStore = {
user:{
usertype:'IS_NOT_SET',
carrier:'CARRIER_IS_NOT_SET',
step:'NOTBEGIN',
token:'NOT_GENERATED',
working_time:'NOT_GENERATED'}
,
theme:{theme:'HOMEPAGE_THEME'},

};


const middleware = applyMiddleware(logger);
 export const store = Redux.createStore(
    jobReducer,
    initialStore,
    middleware


  );

