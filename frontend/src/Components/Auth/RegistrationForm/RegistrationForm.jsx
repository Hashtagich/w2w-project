import style from './registrationForm.module.scss';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const RegistrationForm = () => {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        re_password: '',
    });
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({
            ...prevFormData,
            [name]: value,
        }));
    };

    const sendData = async (event) => {
        event.preventDefault();
        http://127.0.0.1:8000/api/jwt/create/
        try {
            const response = await fetch('http://127.0.0.1:8000/api/users/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (response.ok) {
                navigate('/brand-page');
            } else {
                const errorData = await response.json();
                setError(errorData.message || 'Ошибка при регистрации');
            }
        } catch (err) {
            setError('Ошибка сети');
        }
    };

    return (
        <form className={style.registration} onSubmit={sendData}>
             <div className={style.ellipse1}>
                </div>
                <div className={style.ellipse2}>
                </div>
                <div className={style.ellipse3}>
                </div>
            <div className={style['registration__form']}>
                <img src="./M.svg" alt="logo" />
                <h1>Добро пожаловать <br />в W2W Match</h1>
                <div className={style.inputContainer}>
                    <p>Введите почту</p>
                    <input 
                        type="email" 
                        name="email" 
                        value={formData.email} 
                        onChange={handleChange} 
                    />
                    <p>Введите пароль</p>
                    <input 
                        type="password" 
                        name="password" 
                        value={formData.password} 
                        onChange={handleChange} 
                    />
                    <p>Повторите пароль</p>
                    <input 
                        type="password" 
                        name="re_password" 
                        value={formData.re_password} 
                        onChange={handleChange} 
                    />
                </div>
                {error && <p className={style.error}>{error}</p>}
                <span className={style.confirmed}>
                    <input type="checkbox" />
                    <p>Я даю согласие на обработку <br/>персональных данных</p>
                </span>
                <span className={style.links2}>
                    <a href="/registration">Регистрация</a> |
                    <a href="/login">Авторизация</a>
                </span>
                <button type="submit">Зарегистрироваться</button>
            </div>
        </form>
    );
};

export default RegistrationForm;
