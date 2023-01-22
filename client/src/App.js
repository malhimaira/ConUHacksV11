import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router,Route,Routes} from 'react-router-dom';
import Home from './components/Home';
import Visualization from './components/Visualization';



function App() {
  return (
    <Router>
    <div className="App">
      <Routes>

      <Route path='/' element={<Visualization />} />
      </Routes>
    </div>
    </Router>
  );
}

export default App;
