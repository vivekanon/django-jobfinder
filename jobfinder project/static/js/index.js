var React = require('react');
var ReactDOM = require('react-dom');
var React = require('react')
var Redux = require('redux')
import { v4 } from 'node-uuid';
var ReactDOM = require('react-dom');
import { BrowserRouter } from 'react-router-dom'
import { browserHistory,Router, Route,Link,Switch } from 'react-router'

import { createStore } from 'redux'
import { combineReducers } from 'redux'
import { Provider } from 'react-redux'
import Body from './components/body'
import SignIn from './components/signin'
import Login from './components/login'
import Answers from './components/displayanswers'
import EmployerAnswers from './components/DisplayEmployerAnswers'

import {store} from './store'
import EmployeeForm from './components/EmployeeForm'
import EmployerForm from './components/EmployerForm'

import LoginRequired from './components/loginrequired'

//import {carrier} from './reducers/carrier'

const render = () => {

    ReactDOM.render(<Provider store={store}><BrowserRouter>
 <Switch>

     <Route exact path="/job/" component={ Body }/>
     <Route exact path="/job/employer/answers/" component={ EmployerAnswers }/>
     <Route exact path="/job/employee/answers/" component={ Answers }/>

    <Route exact path="/job/signin/" component={ SignIn }/>
    <Route exact path="/job/login/" component={ Login }/>
    <Route exact path="/job/login-required/" component={ LoginRequired }/>

    <Route exact path="/job/employee/question/:carrier?/:question_number?/" component={ EmployeeForm }/>
    <Route exact path="/job/employer/question/:carrier?/:question_number?/" component={ EmployerForm }/>

</Switch>
    </BrowserRouter></Provider>,
    document.getElementById('root'));
   // store.subscribe(carrier);

}


render();