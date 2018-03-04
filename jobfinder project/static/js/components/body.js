var React = require('react');
var ReactDOM = require('react-dom');
import {store} from '../store'
import { connect } from 'react-redux'
import { Link } from 'react-router-dom'
import {step} from '../reducers/step'
import {theme} from '../reducers/theme'




//         **** Remember different between store which imported and props store ****



export default class Body extends React.Component{

constructor(props){

super(props);

}
render(){



return(
<div>
<h1>home</h1>

<Link to={'/job/signin/'} onClick={()=>{store.dispatch({type:'UPDATING_STEP',step:'signin...'})}}> sign in </Link>
<br />
<Link to={'/job/login/'} onClick={()=>{store.dispatch({type:'UPDATING_STEP',step:'login...'})}}> login </Link>
<br />


</div>
);


        }










}
