import React from 'react';
import Kitten from './Kitten';
import useSheet from 'react-jss';
import { connect } from 'react-redux';
import { addKitten, deleteKitten } from '../actions/kittens';

const Kittens = ({ sheet, kittens, addKitten, deleteKitten }) =>
  <div className={sheet.classes.kittens}>
    {!!kittens.length &&
      <h1>Look, there are kittens in this basket:</h1>
    }
    {!!kittens.length &&
      <div className={sheet.classes.basket}>
        {kittens.map(kitten => (
          <Kitten key={`kitten-${kitten.id}`}
                  kitten={kitten}
                  onDeleteKitten={deleteKitten} />
        ))}
      </div>
    }
    {!kittens.length &&
      <h1>This backet has no kittens in it :(</h1>
    }
    <a className={sheet.classes.button} onClick={addKitten}>
      Put another kitten into basket
    </a>
    
  </div>;

const STYLES = {
  credits: {
    fontSize: 10
  },

  link: {
    textDecoration: 'none'
  },

  basket: {
    display: 'flex',
    flexDirection: 'row',
    alignSelf: 'stretch',
    flexWrap: 'wrap'
  },

  kittens: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    width: '60%'
  },

  button: {
    padding: '1rem 1.5rem',
    background: '#FFAAAA',
    '&:hover': {
      background: '#FFBBBB'
    },
    border: 0,
    borderRadius: '0.5rem',
    cursor: 'pointer',
    margin: '2rem',
    textAlign: 'center',
    userSelect: 'none'
  }
};

export default connect(
  state => ({ kittens: state.kittens }),
  { addKitten, deleteKitten }
)(
  useSheet(Kittens, STYLES)
);
