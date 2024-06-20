import style from './index.module.scss';
import PhotoInput from './Components/PhotoInput/PhotoInput';

const BrandPage = () => {
    return (
        <div className={style.container}>
            <div className={style.navigation}>
                <img src="./home.svg" alt="home" />
                <img src="./user.svg" alt="user" />
                <img src="./book.svg" alt="book" />
                <img src="./mail.svg" alt="mail" />
                <img src="./magicWand.svg" alt="magic wand" />
                <img src="./form.svg" alt="form" />
                <img src="./settings.svg" alt="settings" />
                <img src="./out.svg" alt="out" />
            </div>
            <div className={style.form}>
                <div className={style.section1}>
                    <div className={style.photo}>
                        <PhotoInput/>
                    </div>
                    <div className={style.nameInput}>
                        <p>наименование*</p>
                        <input type='text'></input>
                        <p>тип*</p>
                        <input type='text'></input>
                    </div>
                </div>
                <div className={style.section2}>
                        <div className={style.column1}>
                        <p>сфера*</p>
                        <input type='text'></input>
                        <p>почта*</p>
                        <input type='text'></input>
                        <p>целевая аудитория</p>
                        <input type='text'></input>
                        <p>ценности бренда</p>
                        <input type='text'></input>
                        <p>выбери соц.сеть</p>
                        <input type='text'></input>
                        </div>
                        <div className={style.column2}>
                        <p>город*</p>
                        <input type='text'></input>
                        <p>контактное лицо</p>
                        <input type='text'></input>
                        <p>категории взаимодействия</p>
                        <input type='text'></input>
                        <p>цель коллаборации</p>
                        <input type='text'></input>
                        <p>добавь ссылку</p>
                        <input type='text'></input>
                        </div>
                </div>
                        <p className={style.more}>добавить ещё...</p>
                        <div className={style.section3}>
                        <p>опишите ваш товар или услугу</p>
                        <input type='text'></input>
                        <p>какую проблему решаете для клиента?</p>
                        <input type='text'></input>
                        <p>в чем уникальность вашего продукта?</p>
                        <input type='text'></input>
                        <p>миссия бренда</p>
                        <input type='text'></input>
                        </div>  
                        <div className={style.section4}>
                        <PhotoInput/>
                        <PhotoInput/>
                        <PhotoInput/>
                        <div className={style.saveButton}>
                            <button>Сохранить</button>
                            <p>Нажимая кнопку сохранить вы отправляете данные<br /> на модерацию, после проверки вам поступит<br /> уведомление на почту для выбора тарифа.</p>
                        </div>
                        </div>
            </div>
        </div>
    )
}

export default BrandPage;