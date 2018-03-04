
export const carrier = (state,action) => {


switch(action.type){

    case 'programming':

            return {...state,

            carrier : 'programming'


        }

    default:
          return{ ...state,

            carrier : 'programming'


        }


}



