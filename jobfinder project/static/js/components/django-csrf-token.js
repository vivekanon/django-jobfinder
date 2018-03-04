import React, {
    PropTypes,
} from 'react';

import {csrftoken} from '../cookie'; //Here we import the previous created file

const DjangoCSRFToken = () => {
    return (
        <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
    );
};


export default DjangoCSRFToken;