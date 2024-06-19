import style from './loginForm.module.scss';

const LoginForm = () => {
    return (
        <div className={style.login}>
            <div className={style['login__form']}>
                <img src="./M.svg" alt="logo" />
                <h1>Добро пожаловать <br />в W2W Match</h1>
                <div className={style.inputContainer}>
                <p>введите почту</p>
                <input></input>
                <p>введите пароль</p>
                <input></input>
                </div>
                <span className={style.links1}>
                    <a href="">Забыли пароль?</a>
                    /
                    <a href="">Восстановить</a>
                </span>
                <span className={style.links2}>
                    <a href="/registration">Регистрация</a>
                    |
                    <a href="/login">Авторизация</a>
                </span>
                <button>Войти</button>
            </div>
        </div>
    )
}

export default LoginForm;
