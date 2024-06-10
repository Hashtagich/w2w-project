import style from './tariffs.module.scss';
import TariffCard from './Components/Tariffcard'

const Tariffs = (props) => {
    return (
        <div className={style.tariffs}>
            <div className={style['tariffs__container']}>
               
                <TariffCard/>
                
            </div>
        </div>
    )
}

export default Tariffs;