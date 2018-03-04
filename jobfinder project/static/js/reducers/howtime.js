export const WorkingTime = (state,action) => {
if(action.type == 'SETTING_WORKING_TIME'){
return {...state,step:action.time}


}
else{


return {...state}

}

}