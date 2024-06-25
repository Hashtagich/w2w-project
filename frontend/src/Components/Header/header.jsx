import { useNavigate } from 'react-router-dom';
import style from './header.module.scss';
import logo from './images/logo.svg';
import person from './images/person.svg';



const Header = () => {
    const navigate = useNavigate();

    const goToLogin = () => {
        navigate('/login');
    }

    const goToHome = () => {
        navigate('/');
    }


    return (
        <header className={style.header}>
            <div className={style['header__container']}>
                <div className={style['header__logo']}>
                    <img src={logo} alt="logo" onClick={goToHome}/>
                </div>
                <nav className={style['header__navigation']}>
                    <ul>
                        <a href="#service">О сервисе</a>
                        <a href="#tariffs">Тарифы</a>
                        <a href="#questions">Вопросы</a>
                        <a href="#reviews">Отзывы</a>
                        <a href="#contacts">Контакты</a>
                    </ul>
                </nav>
                <div className={style['header__auth']}>
                    <img src={person} alt="person" onClick={goToLogin}/>
                </div>
            </div>
        </header>
    )
}

export default Header;