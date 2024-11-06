import React from 'react'
import {propTypes} from 'prop-types'

function Button({size,onClick,backgroundColor,position,className,content}) {
  return (
    <div className={{className,size,backgroundColor,position}} onClick={onClick}>{content}</div>
  )
}

export default Button

Button.DefaultProps={
    size: 'small',
    onClick: '',
    backgroundColor: '#fff0000',
    position: 'normal',
    className: '',
    content : 'the Button'
}

Button.propTypes={
    size: propTypes.string,
    onClick: propTypes.func(),
    backgroundColor: propTypes.string,
    position: propTypes.string,
    className: propTypes.string,
    content :propTypes.string
}

// this is how we will create the re-usable components