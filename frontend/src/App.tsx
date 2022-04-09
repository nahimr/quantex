import React, { Component } from 'react';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home/Home';
import Toolbar from './components/Toolbar/Toolbar';

class App extends Component<any, any> 
{
  constructor(props: any) {
    super(props)

  }

  render(): React.ReactNode {
    return (
      <div className="App">
        <Toolbar margin={16} />
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    )
  }

}

export default App;
