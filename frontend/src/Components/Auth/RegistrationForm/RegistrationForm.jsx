import style from './registrationForm.module.scss';

const RegistrationForm = () => {
    return (
        <div className={style.registration}>
            <div className={style['registration__form']}>
                <img src="./M.svg" alt="logo" />
                <h1>Добро пожаловать <br />в W2W Match</h1>
                <div className={style.inputContainer}>
                <p>введите почту</p>
                <input></input>
                <p>введите пароль</p>
                <input></input>
                <p>повторите пароль</p>
                <input></input>
                </div>
                <span className={style.confirmed}>
                <input type="checkbox" />
                <p>я даю согласие на обработку <br/>персональных данных</p>
                </span>
                <span className={style.links2}>
                    <a href="/registration">Регистрация</a>
                    |
                    <a href="./login">Авторизация</a>
                </span>
                <button>Зарегистрироваться</button>
            </div>
        </div>
    )
}

export default RegistrationForm;