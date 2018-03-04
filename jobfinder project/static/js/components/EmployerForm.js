var React = require('react');
var ReactDOM = require('react-dom');
import {store} from '../store'

import { Link } from 'react-router-dom'
import { connect } from 'react-redux'

const getQuestion = (storeReceived,carrier,question_number) => {

switch(carrier){

    case 'programming':

        switch(question_number){

        case "1":
           return HowTime(storeReceived);

        case "2":
            return <AbilityForm />

        default :

        return ''

}
    case 'restaurant':

     switch(question_number){

        case "1":
            return <h1>restaurant,question1</h1>



        default :

        return ''

}

default:
    return <CarrierQuestion/>


}
}



const CarrierQuestion = () => {


return(


<div className='carrier-asking'>
        <Link onClick={()=>{



        store.dispatch({
                        type:'SETTING_CARRIER',
                        carrier:'programming',
                      });

        }} to={'/job/employer/question/programming/1'}>programming</Link>


<br/>

         <Link onClick={()=>{


        store.dispatch({
                        type:'SETTING_THEME',
                        carrier:'programming',


                      });}} to={'/job/employer/question/restaurant/1'}>restaurant</Link>


<br/>


    </div>

    );


}

const HowTime = (storeReceived) => {
var workingtime = storeReceived.user.working_time;
console.log(workingtime == 'full-time');
return(


<form>
    <div className="radio">
      <label>
        <input type="radio" value="full-time" onClick={ ()=>{
        store.dispatch({
                        type:'SETTING_WORKING_TIME',
                        time:'full-time',
                      })}} checked={ workingtime == 'full-time'}  />
       تمام وقت
      </label>
    </div>
    <div className="radio">
      <label>
        <input type="radio" value="half-time"
      onClick={ ()=>{
        store.dispatch({
                        type:'SETTING_WORKING_TIME',
                        time:'half-time',
                      })}}
                      checked={ workingtime == 'half-time'}
                       />
       نیمه وقت
      </label>
    </div>
<Link to={'/job/employer/question/programming/2/'}>next Level</Link>
  </form>


);
}



class AbilityForm extends React.Component{

constructor(props){

super(props);


}

handleSubmit = (e) => {
    if(e) e.preventDefault();
    const abilities = this.input.value.split();
    console.log('Your name is', name);
    store.dispatch({
                        type:'ADDING_ABILITIES',
                        abilities:abilities,
                      })
  }


render(){

return (
<div>
    <form onSubmit={this.handleSubmit}>
    <h2> چه مهارت هایی رو برایش شرکتتون نیاز دارید</h2>
    <textarea ref={(element) => { this.input = element }} />




    <button type='submit'>submit</button>

    </form>
<Link to={'/job/employer/answers/'}>next Level</Link>
</div>
);



}
}


@connect((store) => {

return  {
store:store

}

})
export default class EmployeeForm extends React.Component{

constructor(props){

super(props);

}

componentWillMount = () => {



if(this.props.store.user.token =="NOT_GENERATED"){


this.props.history.push('/job/login-required/');


}


}


render(){
var WorkingTime = this.props.WorkingTime;

var question_number = this.props.match.params.question_number;
var carrier = this.props.match.params.carrier;

console.log(question_number);
if(question_number == 'undefined'){
    return(

    <div className='question-wrapper'>

<CarrierQuestion />
         </div>



    );

}
else{
return(
<div className='question-wrapper'>

{getQuestion(this.props.store,carrier,question_number)}
</div>
);

}


    }

}






