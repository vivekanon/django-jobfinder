
export const user = (state,action) => {

if (action.type == 'SETTING_CARRIER'){
switch(action.carrier){

    case 'programming':
    console.log('here we are');
            return {...state,carrier:'programming'}

    case 'restaurant':

    return {...state,

            carrier : 'restaurant'


        }
    default:
          return{ ...state,

            carrier : 'programming'


        }


}
}
else if(action.type == 'UPDATING_STEP'){
return {...state,step:action.step}


}
else if(action.type == 'SETTING_WORKING_TIME'){
return {...state,working_time:action.time}


}
else if(action.type == 'SETTING_TOKEN'){
return {...state,token:action.token}


}
else if(action.type == 'ADDING_ID'){
return {...state,id:action.id}


}


else if(action.type == 'ADDING_ABILITIES'){
return {...state,abilities:action.abilities}


}

else if(action.type == 'SETTING_USER_TYPE'){
return {...state,usertype:action.usertype}


}




else{

return {...state}

}

}

