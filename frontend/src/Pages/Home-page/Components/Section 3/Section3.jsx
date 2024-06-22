import style from './section3.module.scss'
import constellation from './images/constellation.svg'

const Section3 = () => {
    return (
        <div className={style.section3}>
            <div className={style['section3__container']}>
                <img src={constellation} alt="constellation" className={style.constellation}/>
                <p>Стань <br />резидентом</p>
                <p>Изучи <br />каталог</p>
                <p>Ставь лайки <br />и получай <br />мэтчи</p>
                <p>Придумывай <br />и креативь</p>
                <p>Создай <br />коллабу</p>
                <button>Создать коллабу</button>
                <div className={style.ellipse1}></div>
                <div className={style.ellipse2}></div>
                <div className={style.ellipse3}></div>
            </div>
        </div>
    )
}

export default Section3;