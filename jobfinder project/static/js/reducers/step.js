export const step = (state,action) => {
if(action.type == 'UPDATING_STEP'){
return {...state,user:[{step:action.step}]}


}
else{


return {...state}

}

}