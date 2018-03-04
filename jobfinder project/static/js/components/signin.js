var React = require('react');
var ReactDOM = require('react-dom');
import { connect } from 'react-redux'
import axios from 'axios';
import DjangoCSRFToken from './django-csrf-token'
import {csrftoken} from '../cookie';
import {store} from '../store'

@connect((store) => {

return  {
store:store,
carrier:store.carrier,
theme:store.theme

}

})

export default class SignIn extends React.Component{

constructor(props){

super(props);
this.signin = this.signin.bind(this);
this.state = {
error:""
}
}




signin(event){
 event.preventDefault();

console.log(csrftoken);

 axios({
 method:'POST',
 url:'http://127.0.0.1:8000/api/users/register/',
 headers:{
 'X-CSRFToken': csrftoken
 },
data :{
       "first_name": this.state.first_name,
       "last_name": this.state.last_name,
       "phone_number":this.state.phone_number,
       "user_type":this.state.user_type,
}
      }).then((response) =>{
console.log(response);



  })
  .catch((error) =>  {
 console.log(error);
 if(error.response.status != 201){
    this.setState({error:error.response.data.non_field_errors[0]});
}
  });

}

render(){

console.log(this.state);
var user_type = this.props.store.user.usertype;

return(

<div>
<form onSubmit={this.signin}>
<h2>{this.state.error}</h2>
<input name='first_name' placeholder='firstname'  onChange={
(event)=>{this.setState({first_name:event.target.value})}}/>
<br />
<input name='last_name' placeholder='lastname' onChange={
(event)=>{this.setState({last_name:event.target.value})}} />
<br />

<input name='phone_number' placeholder='phonenumber'  onChange={
(event)=>{this.setState({phone_number:event.target.value})}}/>



   <div className="radio">
      <label>
        <input type="radio"  onClick={()=>{
        this.setState({user_type:'employee'});
        store.dispatch({
                        type:'SETTING_USER_TYPE',
                        usertype:'employee',
                      })}} checked={ user_type == 'employee'}  />
       employee
      </label>
    </div>
    <div className="radio">
      <label>
        <input type="radio"
      onClick={ ()=>{
              this.setState({user_type:'employer'});

        store.dispatch({
                         type:'SETTING_USER_TYPE',
                        usertype:'employer',
                      })}} checked={ user_type == 'employer'}  />

       employer
      </label>
    </div>

<button onClick={this.signin} type='submit'>submit</button>
</form>
</div>

);

}








}