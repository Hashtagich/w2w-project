import style from '../section4.module.scss';

const Tariff = ({info}) => {
    return (
        <div className={style.tariffsCard}>
             <h1>{info.title1}</h1>
             <h1>{info.title2}</h1>
             <p className={style.text1}>{info.text1}</p>
             <p className={style.text2}>{info.text2}</p>
             <p className={style.price}>{info.price}</p>
             <p className={style.text3}>{info.text3}</p>
             <button>{info.button}</button>
             <details>
             <summary>О тарифе</summary>
               <div className={style['drop-down-list']}>
                {/* <p>Доступ к чату в Telegram</p>
                <p>Размещение Бренда в каталоге</p>
                <p>Доступ к личному кабинету</p>
                <p>Моментальное оповещение о метчах</p>
                <p>Возможность посещать онлайн и офлайн мероприятия W2W Match</p> */}
               </div>
             </details>
        </div>
    )
}

export const tariffsInfo = [
    {
        code: 0,
        title1: 'Lite',
        title2: 'Match',
        text1: 'Становишься резидентом сервиса',
        text2: 'Стоимость за год',
        price: '12 000₽',
        text3: 'Доступна рассрочка 1 000 р в месяц',
        button: 'Оформить',
    },
    {
        code: 1,
        title1: 'Comfort ',
        title2: 'Match',
        text1: 'Знаешь, кто тебя лайкнул в моменте',
        text2: 'Стоимость за год',
        price: '24 000₽',
        text3: 'Доступна рассрочка 2 000 р в месяц',
        button: 'Оформить',
    },
    {
        code: 2,
        title1: 'Business',
        title2: 'Match',
        text1: 'Мы активно помогаем с коллабой',
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

