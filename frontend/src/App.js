import { Routes, Route, Navigate } from 'react-router-dom';
import style from './app.module.scss';
import HomePage from './Pages/Home-page/index';
import Header from './Components/Header/header';
import LoginForm from './Components/Auth/LoginForm/LoginForm';
import RegistrationForm from './Components/Auth/RegistrationForm/RegistrationForm';


function App() {
  return (
    <div className={style.app}>
    <Header/>
      <Routes>
    <Route path="/" element={<HomePage/>}/>
    <Route path="/login" element={<LoginForm/>}/>
    <Route path="/registration" element={<RegistrationForm/>}/>
    </Routes>
    </div>
  );
}

export default App;
