import style from './header.module.scss';
import logo from './images/logo.svg';
import person from './images/person.svg';


const Header = () => {
    return (
        <header className={style.header}>
            <div className={style['header__container']}>
                <div className={style['header__logo']}>
                    <img src={logo} alt="logo" />
                </div>
                <nav className={style['header__navigation']}>
                    <ul>
                        <a href="">О сервисе</a>
                        <a href="">Тарифы</a>
                        <a href="">Вопросы</a>
                        <a href="">Отзывы</a>
                        <a href="">Контакты</a>
                    </ul>
                </nav>
                <div className={style['header__auth']}>
                    <img src={person} alt="person" />
                </div>
            </div>
        </header>
    )
}

export default Header;