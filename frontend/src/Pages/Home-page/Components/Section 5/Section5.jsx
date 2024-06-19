import style from './section5.module.scss';
import Card from './Components/BrandCards';

const Section5 = () => {
    return (
        <div className={style.section5} id='reviews'>
            <img src="./prev-button.svg" alt="prev-button" className={style.img1}/>
            <div className={style.container}>
                <Card/>
            </div>
            <img src="./next-button.svg" alt="next-button" className={style.img2}/>

        </div>
    )
}

export default Section5;