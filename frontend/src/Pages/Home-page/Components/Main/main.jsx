import style from './main.module.scss';

const Main = () => {

    return (
        <div className={style.main}>
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
                    <p>Объединяем бренды по ценностям<br/>и помогаем делать коллабы для <br/>роста бизнеса</p>
                    <button>Зарегистрироваться</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main;