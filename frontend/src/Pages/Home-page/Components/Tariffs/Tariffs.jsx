import style from './tariffs.module.scss';
import TariffCard from './Components/Tariff'

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