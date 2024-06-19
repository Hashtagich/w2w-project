import React from 'react';
import { Swiper, SwiperClass, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import style from '../section5.module.scss';
import StarRating from './StarRating';


const BrandCard = ({info}) => {
    return (
        <div className={style.cards}>
            <StarRating/>
            <img src={info.img1.src} alt={info.img1.alt} className={style.img1} />
            <div className={style.title}>
                <p>{info.name}</p>
                <img src={info.img2.src} alt={info.img2.src} />
            </div>
            <p>{info.infoText}</p>
        </div>
    )
}


const infoCards = [
    {
        code: 0,
        img1: {
            src: './foto.svg',
            alt: 'foto'
        },
        name: 'Дарья Камышенкова',
        img2: {
            src: './nameLogo.svg',
            alt: 'nameLogo'
        },
        infoText: 'Лиза, спасибо! Я была уверена, что это только для крупных брендов коллабы эти и даже не могла подумать, что это доступно и для простых смертных. А ведь это классный способ продвижения! ',

    },
    {
        code: 1,
        img1: {
            src: './foto.svg',
            alt: 'foto'
        },
        name: 'Анна Смирнова',
        img2: {
            src: './nameLogo.svg',
            alt: 'nameLogo'
        },
        infoText: 'Я в восторге от платформы и личной работы с вами! Я вписалась в тему после трех касаний и взяла бизнес-тариф. Удивительно, как тебе удалось за такой короткий срок собрать такое большое сообщество деятельных и открытых женщин.! ',
    },
    {
        code: 2,
        img1: {
            src: './foto.svg',
            alt: 'foto'
        },
        name: 'Анастасия Славская',
        img2: {
            src: './nameLogo.svg',
            alt: 'nameLogo'
        },
        infoText: 'Делаю коллаб с брендом одежды сейчас, на очереди потом украшения) очень классный опыт) И он прямо такой многогранный, очень двигает вперед и дает возможность увидеть и себя и свой проект со стороны в том числе)',
    },
    {
        code: 3,
        img1: {
            src: './foto.svg',
            alt: 'foto'
        },
        name: 'Анастасия',
        img2: {
            src: './nameLogo.svg',
            alt: 'nameLogo'
        },
        infoText: 'Хочу внедрять качественные коллаборации в историю своего бренда, как инструмент развития! Круто, что для этого есть сервис W2W Match, я уже подала заявку.',
    },
]


const Card = () => {
    return (
        <div className={style.swipe}>
            
        <Swiper
        spaceBetween={50}
        slidesPerView={4}
        className={style.swiper}
        loop
        >
            {infoCards.map((info) => (
                <SwiperSlide>
                <BrandCard  key={info.code} info={info} />
                </SwiperSlide>
              
            ))}
        </Swiper> 
        </div>
    )
}

export default Card;