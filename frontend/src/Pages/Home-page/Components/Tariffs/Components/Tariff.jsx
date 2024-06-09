import style from '../tariffs.module.scss';

const Tariff = ({info}) => {
    return (
        <div className={style['tariffsCard']}>
             <h1>{info.title1}</h1>
             <h1>{info.title2}</h1>
             <p className={style.text1}>{info.text1}</p>
             <p className={style.text2}>{info.text2}</p>
             <p className={style.price}>{info.price}</p>
             <p className={style.text3}>{info.text3}</p>
             <button>{info.button}</button>
             <details>
             <summary>Что входит:</summary>
               <div className={style['drop-down-list']}>
               </div>
             </details>
        </div>
    )
}

export const tariffsInfo = [
    {
        code: 0,
        title1: 'Тариф',
        title2: '"Базовый"',
        text1: 'Знаешь, кто тебя лайкнул в моменте.',
        text2: 'Стоимость за год',
        price: '12 000₽',
        text3: 'Доступна рассрочка 1 000 р в месяц',
        button: 'Оформить',
    },
    {
        code: 1,
        title1: 'Тариф',
        title2: '"Комфорт"',
        text1: 'Знаешь, кто тебя лайкнул в моменте',
        text2: 'Стоимость за год',
        price: '24 000₽',
        text3: 'Доступна рассрочка 2 000 р в месяц',
        button: 'Оформить',
    },
    {
        code: 2,
        title1: 'Тариф',
        title2: '"Премиум"',
        text1: 'Знаешь, кто тебя лайкнул в моменте.',
        text2: 'Стоимость за год',
        price: '60 000₽',
        text3: 'Доступна рассрочка 5 000 р в месяц',
        button: 'Оформить',
    }
]


const TariffCard = () => {
    return (
        <>
            {tariffsInfo.map((info) => (
                <Tariff key={info.code} info={info}/>
            ))}
        </>
    )
}

export default TariffCard;

