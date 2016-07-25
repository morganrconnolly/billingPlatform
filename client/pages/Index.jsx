import React, { Component } from 'react';
import useSheet from 'react-jss';
import Kittens from '../components/Kittens';
import { connect } from 'react-redux';
import { requestKittens } from '../actions/kittens';

import Users from '../components/Users';
import { requestUsers } from '../actions/users';

var MainContainer = require('../components/MainContainer')

export default class Index extends Component {

  render() {


    return (
      <div>
        <MainContainer />
      </div>
    );
  }
}

const STYLES = {
  index: {
    width: '100%',
    height: '100%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#FFDDDD',
    color: '#660000'
  }
};

//I have no idea what this is doing (beyond exporting this page) but it's working.
export default connect(
  () => ({}),
  { requestKittens }
)(
  useSheet(Index, STYLES)
);
