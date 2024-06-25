import { Routes, Route, Navigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import style from './app.module.scss';
import HomePage from './Pages/Home-page/index';
import Header from './Components/Header/header';
import LoginForm from './Components/Auth/LoginForm/LoginForm';
import RegistrationForm from './Components/Auth/RegistrationForm/RegistrationForm';
import UserContext from './Contexts/UserContext';
import BrandPage from './Pages/Brand-page/index';
import NotFoundPage from './Pages/NotFoundPage/NotFoundPage';
import Footer from './Components/Footer/Footer';

function App() {
  const [user, setUser] = useState(null);
  const [isAuth, setIsAuth] = useState(!!localStorage.getItem('token'));

  useEffect(() => {
    if (isAuth) {
      fetch('http://127.0.0.1:8000/api/users/me/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Ошибка на сервере');
        }
        return response.json();
      })
      .then((data) => {
        setUser(data);
      })
      .catch((error) => {
        console.error(error);
      });
    }
  }, [isAuth]);

  return (
    <UserContext.Provider value={{ user, isAuth, setUser, setIsAuth }}>
      <div className={style.app}>
        <Header />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/brand-page" element={<BrandPage />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/registration" element={<RegistrationForm />} />
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
        <Footer/>
      </div>
    </UserContext.Provider>
  );
}

export default App;
