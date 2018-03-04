export const token = (state,action) => {
if(action.type == 'SETTING_TOKEN'){
return {...state,token:action.token}


}
else{


return {...state}

}

}