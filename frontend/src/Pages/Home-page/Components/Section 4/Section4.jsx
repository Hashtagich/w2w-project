import style from './section4.module.scss';
import TariffCard from './Components/Tariffcard'

const Section4 = (props) => {
    return (
        <div className={style.tariffs}>
            <div className={style['tariffs__container']}>
                <TariffCard/>
            </div>
        </div>
    )
}

export default Section4;