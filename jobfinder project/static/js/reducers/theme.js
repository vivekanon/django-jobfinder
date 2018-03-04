export const theme = (state,action) =>{

if (action.type == 'SETTING_THEME'){

switch(action.theme){
    case 'programming':

            return {...state,

            theme : 'programming'


}


    default:


        return {...state,

                    theme : 'programming'


                }

}


}
else{

return {...state}

}


}