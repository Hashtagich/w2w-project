import style from './notfoundpage.module.scss';

const NotFoundPage = () => {
    return (
        <div className={style.container}>
              <div className={style.ellipse1}>
                </div>
                <div className={style.ellipse2}>
                </div>
                <div className={style.ellipse3}>
                </div>
            <h1>Что-то пошло не так,<br /> страница скоро<br /> заработает.</h1>
            <div className={style.images}>
            <img src="./cat.svg" alt="cat" />
            <img src="./404.svg" alt="404" />
            </div>
        </div>
    )
}

export default NotFoundPage;