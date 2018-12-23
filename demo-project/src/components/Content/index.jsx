import React from 'react';
import SubContent from './components/SubContent';
import {printSomeNumber as onClickUtil} from './utils';

const Content = () => (
  <div>
    <h1>Content</h1>
    <SubContent />
    <button onClick={onClickUtil}>Click me</button>
  </div>
);

export default Content;
