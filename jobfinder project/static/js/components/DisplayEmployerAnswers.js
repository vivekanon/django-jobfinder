var React = require('react');
var ReactDOM = require('react-dom');
import {store} from '../store'
import { connect } from 'react-redux'
import { Link } from 'react-router-dom'
import {step} from '../reducers/step'
import {theme} from '../reducers/theme'
import axios from 'axios';
import {csrftoken} from '../cookie';




//         **** Remember different between store which imported and props store ****



@connect((store)=>{

return {

store:store


}
})
export default class EmployerAnswers extends React.Component{

constructor(props){

super(props);
this.user = this.props.store.user;

}

createProfile = () => {

console.log('updating ...');
 console.log(this.user.carrier);



 axios({
 method:'POST',
 url:'http://127.0.0.1:8000/api/users/job/create/',
 headers:{
 'X-CSRFToken': csrftoken
 },
data :{
       "employer": this.user.id,
       "how_time": this.user.working_time,
       "abilities_needed":this.user.abilities,
       "field_of_work":this.user.carrier
}
      }).then(function (response) {
console.log(response);
  })


  .catch(function (error) {
 console.log(error);

  });

}

Process = () =>{
console.log('processing')
this.createProfile();


}

componentWillMount = () =>{


console.log('display ');

}

render(){


return(

<div>
carrier:{this.user.carrier}
<br />
working time needed:{this.user.working_time}
<br />

abilities needed: {this.user.abilities}
<br />

<button onClick={()=>{this.Process()}}>process</button>
</div>


);
}
}