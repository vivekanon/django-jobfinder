var React = require('react');
var ReactDOM = require('react-dom');
import { connect } from 'react-redux'
import axios from 'axios';
import DjangoCSRFToken from './django-csrf-token'
import {csrftoken} from '../cookie';
import {store} from '../store'
import { Link } from 'react-router-dom'

@connect((store) => {

return  {
store:store,
carrier:store.carrier,
theme:store.theme

}

})

export default class LoginRequired extends React.Component{

constructor(props){

super(props);

}


render(){

return(

<div>
<h1>LoginRequired</h1>
<Link to={'/job/signin/'} onClick={()=>{store.dispatch({type:'UPDATING_STEP',step:'signin...'})}}> sign in </Link>
<br />
<Link to={'/job/login/'} onClick={()=>{store.dispatch({type:'UPDATING_STEP',step:'login...'})}}> login  </Link>
</div>

);
}
}