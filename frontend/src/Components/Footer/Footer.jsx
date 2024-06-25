import style from './footer.module.scss';

const Footer = () => {
    return (
        <footer className={style.footer} id="contacts">
            <div className={style['footer__container']}>
                <div className={style.info1}>
                    <p>Услуги оказывает <br/>ИП Баранова Елизавета Дмитриевна</p>
                    <p>ИНН 502724507201</p>
                    <p>ОГРНИП 324508100003686</p>
                    <p>womentowomen@gmail.com</p>
                </div>
                <div className={style.logo}>
                    <img src="./footer-logo.svg" alt="logo" />
                </div>
                <div className={style.info2}>
                    <p>Подпишись на рассылку</p>
                    <div >
                        <img src="./whatsapp.svg" alt="whatsapp" />
                        <img src="./tg.svg" alt="telegram" />
                        <img src="./inst.svg" alt="instagram" />
                        <img src="./vk.svg" alt="vk" />
                        <img src="./youtube.svg" alt="youtube" />
                    </div>
                    <p>Менеджеры: <br/>8(800)444-44-44</p>
                    <p>Линия тех.поддержки: <br/>8(800)444-44-44</p>
                </div>
            </div>
        </footer>
    )
}

export default Footer;