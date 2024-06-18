import { useNavigate } from 'react-router-dom';
import style from './section1.module.scss';

const Section1 = () => {
    const navigate = useNavigate();

    const goToReg = () => {
        navigate('/registration');
    }


    return (
        <div className={style.main} id='service'>
            <div className={style['main__container']}>
                <div className={style['main__title']}>
                    <img src="./title.svg" alt="title" />
                </div>
                <div className={style['main__registration']}>
                    <div className={style.images}>
                    <img src="./star1.svg" alt="star1" className={style.img1}/>
                    <img src="./star2.svg" alt="star2" className={style.img2}/>
                    <img src="./star3.svg" alt="star3" className={style.img3}/>
                    </div>
                    <div className={style.registration}>
                    <p>Объединяем бренды по ценностям и<br/> помогаем делать коллабы для роста<br/> бизнеса</p>
                    <button onClick={goToReg}>Зарегистрироваться</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Section1;