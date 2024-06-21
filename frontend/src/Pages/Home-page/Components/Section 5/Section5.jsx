import { useRef } from 'react';
import Card from './Components/BrandCards';
import style from './section5.module.scss';

const Section5 = () => {
    const swiperRef = useRef(null);

    const handlePrev = () => {
        if (swiperRef.current && swiperRef.current.swiper) {
            swiperRef.current.swiper.slidePrev();
        }
    };
    
    const handleNext = () => {
        if (swiperRef.current && swiperRef.current.swiper) {
            swiperRef.current.swiper.slideNext();
        }
    };

    return (
        <div className={style.section5} id='reviews'>
            <div className={style.prevButton} onClick={handlePrev}>
                <img src="./prev-button.svg" alt="prev-button" className={style.prevButtonImg} />
            </div>
            <div className={style.container}>
                <Card ref={swiperRef}/>
            </div>
            <div className={style.nextButton} onClick={handleNext}>
                <img src="./next-button.svg" alt="next-button" className={style.nextButtonImg} />
            </div>
        </div>
    )
}

export default Section5;