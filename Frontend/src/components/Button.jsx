import React from 'react';
import PropTypes from 'prop-types';

function Button({ size, onClick, backgroundColor, position, className, content }) {
  return (
    <div
      className={className}
      onClick={onClick}
      style={{
        backgroundColor,
        position,
        fontSize: size === 'small' ? '12px' : size === 'large' ? '18px' : '16px',
      }}
    >
      {content}
    </div>
  );
}

Button.defaultProps = {
  // size: 'large',
  onClick: () => {},
  backgroundColor: '#79BB66',
  position: 'relative',
  className: '',
  content: 'The Button',
};

Button.propTypes = {
  size: PropTypes.string,
  onClick: PropTypes.func,
  backgroundColor: PropTypes.string,
  position: PropTypes.string,
  className: PropTypes.string,
  content: PropTypes.string,
};

export default Button;
