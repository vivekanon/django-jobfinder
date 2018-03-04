var React = require('react');
var ReactDOM = require('react-dom');
import { connect } from 'react-redux'
import axios from 'axios'
import DjangoCSRFToken from './django-csrf-token'
import {csrftoken} from '../cookie'
import {store} from '../store'
import { Link } from 'react-router-dom'

@connect((store) => {

return  {
store:store,
carrier:store.carrier,
theme:store.theme

}

})

export default class Login extends React.Component{

constructor(props){

super(props);
this.state = {
error:""
}
}


takeToken = (e) => {
e.preventDefault();
 axios({
 method:'POST',
 url:'http://127.0.0.1:8000/api/auth-jwt/',

 data :{
    "phone_number":this.state.phone_number

 }

      }).then((response) => {

        console.log(response);

      if(response.data.token != 'undefined'){


      return response.data.token

      }




      }).then((token) => {
      console.log(token);
      store.dispatch({
      type:'SETTING_TOKEN',
      token:token
      });
      return token

})

.then((token)=>{
console.log(token);
axios({url:'http://127.0.0.1:8000/api/users/?q='+this.state.phone_number,
method:'GET',
headers : {

            'Content-Type':'application/json',
            'Authorization' : 'beer '+token,
  }})

.then((response) => {
store.dispatch({
      type:'ADDING_ID',
      id:response.data[0].id
      });
      console.log(response);
      store.dispatch({
      type:'SETTING_USER_TYPE',
      usertype:response.data[0].user_type
      });
      console.log(this.props.store.user.usertype);

      if (this.props.store.user.usertype == 'employee'){
            store.dispatch({type:'UPDATING_STEP',step:'choose carrier '});
            this.props.history.push('/job/employee/question/');


      }
      else if (this.props.store.user.usertype == 'employer'){
            store.dispatch({type:'UPDATING_STEP',step:'choose carrier '});
            this.props.history.push('/job/employer/question/');
            }
     })


})

  .catch((error) =>  {
 console.log(error);
 if(error.response.status != 201){
    this.setState({error:error.response.data.non_field_errors[0]});
}
  });



}

sendCode =()=>{

console.log('code');

}

render(){
return(

<form onSubmit={(e)=>{this.takeToken(e)}}>
<h2>{this.state.error}</h2>

<input onChange={(e)=>{this.setState({phone_number:e.target.value})}} />
<button>takeToken</button>
</form>

);

}
}