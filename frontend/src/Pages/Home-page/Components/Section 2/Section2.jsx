import React from 'react';
import style from './section2.module.scss';

const Card = ({ frontContent, backContent1, backContent2 }) => {
    return (
        <div className={style.wrapper}>
            <div className={style.card}>
                <div className={style.front}>
                    <p className={style.content}>{frontContent}</p>
                </div>
                <div className={style.back}>
                    <p className={style.content}>{backContent1}</p>
                    {backContent2 && <p className={style.content}>{backContent2}</p>}
                </div>
            </div>
        </div>
    );
};

const Section2 = () => {
    return (
        <section className={style.container}>
            <Card
                frontContent="Тратишь много времени на поиск партнёра"
                backContent1="Вступи в активное сообщество"
                backContent2="изучи каталог резидентов"
            />
            <Card
                frontContent="Проблемы с началом коммуникации"
                backContent1="Просмотри проверенную базу"
                backContent2="и просто отправь лайк"
            />
            <Card
                frontContent="Не хватает текущих возможностей"
                backContent1="Объединись с партнёром и оптимизируй ресурсы"
            />
            <Card
                frontContent="Хочешь быть в курсе трендов и событий"
                backContent1="Присоединяйся к комьюнити"
                backContent2="вдохновляйся и креативь"
            />
        </section>
    )
} 

export default Section2;
