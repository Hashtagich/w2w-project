import style from './loginForm.module.scss';
import React, { useState, ChangeEvent, FormEvent, useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import UserContext from '../../../Contexts/UserContext';

const LoginForm = () => {
    const [error, setError] = useState('');
    const navigate = useNavigate();
    const { isAuth, setIsAuth } = useContext(UserContext);
    const [formData, setFormData] = useState({ username: '', password: '' });

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({
            ...prevFormData,
            [name]: value,
        }));
    };

    const sendData = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch('http://127.0.0.1:8000/api/jwt/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (response.ok) {
                const data = await response.json();
                setIsAuth(true);
                localStorage.setItem('token', data.token);
                navigate('/brand-page');
            } else {
                const errorData = await response.json();
                setError(errorData.message || 'Ошибка при авторизации');
            }
        } catch (err) {
            setError('Ошибка сети');
        }
    };

    useEffect(() => {
        if (isAuth) {
            navigate('/brand-page');
        }
    }, [isAuth, navigate]);

    return (
        <form className={style.login} onSubmit={sendData}>
            <div className={style.ellipse1}></div>
            <div className={style.ellipse2}></div>
            <div className={style.ellipse3}></div>
            <div className={style['login__form']}>
                <img src="./M.svg" alt="logo" />
                <h1>Добро пожаловать <br />в W2W Match</h1>
                <div className={style.inputContainer}>
                    <p>Введите почту</p>
                    <input 
                        type="text" 
                        name="username" 
                        value={formData.username} 
                        onChange={handleChange} 
                    />
                    <p>Введите пароль</p>
                    <input 
                        type="password" 
                        name="password" 
                        value={formData.password} 
                        onChange={handleChange} 
                    />
                </div>
                {error && <p className={style.error}>{error}</p>}
                <span className={style.links1}>
                    <a href="">Забыли пароль?</a> /
                    <a href="">Восстановить</a>
                </span>
                <span className={style.links2}>
                    <a href="/registration">Регистрация</a> |
                    <a href="/login">Авторизация</a>
                </span>
                <button type="submit">Войти</button>
            </div>
        </form>
    );
};

export default LoginForm;
